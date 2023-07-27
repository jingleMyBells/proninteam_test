from django.urls import path

from api_customers.views import CustomerView, DealsView

app_name = 'api_customers'

urlpatterns = [
    path('customers/', CustomerView.as_view(), name='customers'),
    path('deals/', DealsView.as_view(), name='customers'),
]
