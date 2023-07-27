import csv
import io

from datetime import datetime

from api_customers.models import Customer, Deal, Item

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S.%f'


class DealsInputDispatcher:

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
            queryset.append(
                Deal(
                    money_total=deal.get('total'),
                    quantity=deal.get('quantity'),
                    perform_date=datetime.strptime(deal.get('date'), DATETIME_FORMAT),
                    customer=Customer.objects.filter(
                        username=deal.get('customer')
                    ).first(),
                    item=Item.objects.filter(
                        title=deal.get('item')
                    ).first()
                )
            )

        Deal.objects.bulk_create(queryset)



