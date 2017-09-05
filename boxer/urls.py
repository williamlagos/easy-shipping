from django.conf.urls import url, include
from boxer.api import DeliveryResource
from boxer.views import SputnikView, ThanksPageView

urlpatterns = [
    url(r'^$', SputnikView.as_view(), name='home'),
    url(r'^thanks/', ThanksPageView.as_view(), name='advantages'),
    url(r'^deliveries$', DeliveryResource.as_list(), name="kombi_deliveries"),
    url(r'^deliveries/(?P<pk>\d+)$', DeliveryResource.as_detail(), name="kombi_delivery"),
]
