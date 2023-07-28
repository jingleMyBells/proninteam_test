from http import HTTPStatus

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from api_customers.models import Customer
from api_customers.serializers import TopCustomersSerializer
from api_customers.services import generate_gems_info, process_input_data


class CustomerView(APIView):

    def get(self, request):
        queryset = Customer.objects.all()[:5]
        serializer = TopCustomersSerializer(queryset, many=True)
        serializer.context['gems'] = generate_gems_info(queryset)
        return Response(serializer.data, HTTPStatus.OK)


class DealsView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):

        #FIXME! тут где-то надо не забыть почистить кеш

        if len(request.FILES) == 0:
            return Response('Приложите файл', HTTPStatus.BAD_REQUEST)
        input_csv = request.FILES.get('deals')

        try:
            process_input_data(input_csv)
            return Response('OK', HTTPStatus.OK)
        except Exception as e:
            return Response(f'Error, Desc: {e.args}', HTTPStatus.INTERNAL_SERVER_ERROR)
