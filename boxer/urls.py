from django.conf.urls import url, include
from boxer.api import DeliveryResource

urlpatterns = [
    url(r'^deliveries$', DeliveryResource.as_list(), name="kombi_deliveries"),
    url(r'^deliveries/(?P<pk>\d+)$', DeliveryResource.as_detail(), name="kombi_delivery"),
]
