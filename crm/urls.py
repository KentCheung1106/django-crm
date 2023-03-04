from django.urls import path

from .views.customer import CustomerView
from .views.sale import SaleView
from .views.sale_customer import SaleCustomerView

urlpatterns = [
    path('customers', CustomerView.as_view()),
    path('customers/<int:id>', CustomerView.as_view()),

    path('sales', SaleView.as_view()),
    path('sales/<int:sale_id>', SaleView.as_view()),

    path('sales/<int:sale_id>/customers', SaleCustomerView.as_view())
]