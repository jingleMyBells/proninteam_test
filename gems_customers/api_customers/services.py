import csv
import io
from datetime import datetime

from api_customers.models import Customer, Deal, Item

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S.%f'


class DealsInputDispatcher:
    """
    Диспетчер входящих сделок.
    Распаковыает входящий csv,
    создает записи о покпателях и камнях, если их нет,
    добавляет записи о сделках.
    """

    def __init__(self):
        self.deals = []

    @staticmethod
    def _unpack_file(csvfile):
        input_csv = io.StringIO(csvfile.read().decode('utf-8'))
        return csv.DictReader(input_csv)

    def temporary_save_deals(self, file):
        reader = self._unpack_file(file)

        for row in reader:
            deal = {
                'customer': row['customer'],
                'item': row['item'],
                'total': row['total'],
                'quantity': row['quantity'],
                'date': row['date'],
            }
            self.deals.append(deal)

    def save_items_to_db(self):
        queryset = []

        for deal in self.deals:
            queryset.append(
                Item(title=deal.get('item'))
            )

        Item.objects.bulk_create(
            queryset,
            ignore_conflicts=True,
        )

    def save_customers_to_db(self):
        queryset = []

        for deal in self.deals:
            queryset.append(
                Customer(username=deal.get('customer'))
            )

        Customer.objects.bulk_create(
            queryset,
            ignore_conflicts=True,
        )

    def save_deals_to_db(self):
        queryset = []

        for deal in self.deals:
            customer = Customer.objects.filter(
                username=deal.get('customer'),
            ).first()
            money = int(deal.get('total'))
            customer.spent_money += money
            customer.save()
            queryset.append(
                Deal(
                    money_total=money,
                    quantity=deal.get('quantity'),
                    perform_date=datetime.strptime(
                        deal.get('date'),
                        DATETIME_FORMAT,
                    ),
                    customer=customer,
                    item=Item.objects.filter(
                        title=deal.get('item'),
                    ).first()
                )
            )

        Deal.objects.bulk_create(queryset)


def process_input_data(file):
    """
    :param file: результат чтение inMemoryUploaded File
    :return: None
    """
    dispatcher = DealsInputDispatcher()
    dispatcher.temporary_save_deals(file)
    dispatcher.save_items_to_db()
    dispatcher.save_customers_to_db()
    dispatcher.save_deals_to_db()


def generate_gems_info(queryset):
    """
    Функция для формирования контекста для сериализатора.
    Формирует словарь камней, популярных у топовых покупателей.
    :param queryset: queryset пользователей
    :return: dict с популярными камнями
    """
    popular_gems = dict()

    for user in queryset:
        deals = list(user.deals.values_list('item__title'))
        without_tuples = list(map(lambda elem: elem[0], deals))
        for gem in without_tuples:
            if popular_gems.get(gem) is None:
                popular_gems[gem] = []
            if user.id not in popular_gems[gem]:
                popular_gems[gem].append(user.id)
    return popular_gems
