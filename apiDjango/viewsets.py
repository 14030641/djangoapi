from rest_framework import viewsets
from . import models
from . import serializers

class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CatSerializer

class ProductViewset(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProdSerializer

class CustomerViewset(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustSerializer

class OrderViewset(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

class OrdDetailViewset(viewsets.ModelViewSet):
    queryset = models.OrderDetail.objects.all()
    serializer_class = serializers.OrdDetailSerializer