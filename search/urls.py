
from django.urls import path
from django.conf.urls import url

from .views import (
    SearchProductView,
)

app_name = 'products'

urlpatterns = [
    path('', SearchProductView.as_view(), name='query'),
]
