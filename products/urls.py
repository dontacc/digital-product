from django.urls import path
from . import views



urlpatterns = [
    path("products/" , views.ProductListView.as_view() , name="products-page"),
    path("products/<int:pk>" , views.ProductDetail.as_view() , name="detail-page")
]


