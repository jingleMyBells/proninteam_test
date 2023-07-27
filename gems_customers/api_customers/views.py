import csv
import io

from http import HTTPStatus

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from api_customers.services import DealsInputDispatcher


class CustomerView(APIView):
    pass


class DealsView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):

        #FIXME! тут где-то надо не забыть почистить кеш

        if len(request.FILES) == 0:
            return Response('Приложите файл', HTTPStatus.BAD_REQUEST)
        input_csv = request.FILES.get('deals')

        dispatcher = DealsInputDispatcher()
        dispatcher.temporary_save_deals(input_csv)
        dispatcher.save_items_to_db()
        dispatcher.save_customers_to_db()
        dispatcher.save_deals_to_db()

        return Response('OK', HTTPStatus.OK)
