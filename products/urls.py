
from django.urls import path
from django.conf.urls import url

from .views import (
    ProductListView,
    ProductDetailSlugView,
)

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
]
