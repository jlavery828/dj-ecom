
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import home_page, about_page, contact_page, login_page

from products.views import ProductListView, product_list_view, ProductDetailView, product_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('login/', login_page, name='login'),
    path('products/', ProductListView.as_view(), name='products'),
    path('products-fbv/', product_list_view),
    url(r'^products/(?P<pk>\d+)$/', ProductDetailView.as_view()),
    url(r'^products-fbv/(?P<pk>\d+)$/', product_detail_view),
]
