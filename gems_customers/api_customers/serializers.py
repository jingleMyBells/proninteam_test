from rest_framework import serializers

from api_customers.models import Customer, Deal, Item


class TopCustomersSerializer(serializers.ModelSerializer):

    gems = serializers.SerializerMethodField(method_name='generate_gems')

    def generate_gems(self, obj):
        current_user_gems = []
        for gem, users in self.context['gems'].items():
            if len(users) > 1 and obj.id in users:
                current_user_gems.append(gem)
        return current_user_gems

    class Meta:
        model = Customer
        fields = ('username', 'spent_money', 'gems')
