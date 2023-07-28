from django.conf import settings
from rest_framework import serializers

from api_customers.models import Customer


class TopCustomersSerializer(serializers.ModelSerializer):

    gems = serializers.SerializerMethodField(method_name='generate_gems')

    def generate_gems(self, obj):
        """
        :param obj: сериализуемый покупатель
        :return: список камней, которые покупали
        2 и более топовых покупателя.
        """
        current_user_gems = []
        for gem, users in self.context['gems'].items():
            if len(users) > settings.GEM_POPULARITY_NUMBER and obj.id in users:
                current_user_gems.append(gem)
        return current_user_gems

    class Meta:
        model = Customer
        fields = ('username', 'spent_money', 'gems')
