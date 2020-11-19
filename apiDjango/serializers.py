from rest_framework import serializers
from .models import Product
from .models import Category
from .models import Customer
from .models import Order
from .models import OrderDetail

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CustSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'

