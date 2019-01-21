from .views import GraphView

from django.conf.urls import url


urlpatterns = [
    url(r'^$', GraphView.as_view(), name='graph'),
]
