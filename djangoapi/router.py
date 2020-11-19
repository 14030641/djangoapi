from rest_framework import routers
from apiDjango.viewsets import CategoryViewset
from apiDjango.viewsets import ProductViewset
from apiDjango.viewsets import CustomerViewset
from apiDjango.viewsets import OrderViewset
from apiDjango.viewsets import OrdDetailViewset

router = routers.DefaultRouter()
router.register('category',CategoryViewset)
router.register('product',ProductViewset)
router.register('customer',CustomerViewset)
router.register('order',OrderViewset)
router.register('detail',OrdDetailViewset)