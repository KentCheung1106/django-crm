from django.urls import path

from .views.customer import CustomerView
from .views.customer_detail import CustomerDetailView
from .views.sale import SaleView
from .views.sale_customer import SaleCustomerView
from .views.sale_detail import SaleDetailView
from .views.team import TeamView
from .views.team_detail import TeamDetailView
from .views.team_sale import TeamSaleView

urlpatterns = [
    path('customers', CustomerView.as_view()),
    path('customers/<int:id>', CustomerDetailView.as_view()),

    path('sales', SaleView.as_view()),
    path('sales/<int:sale_id>', SaleDetailView.as_view()),

    path('sales/<int:sale_id>/customers', SaleCustomerView.as_view()),


    path('teams', TeamView.as_view()),
    path('teams/<str:code>', TeamDetailView.as_view()),

    path('teams/<str:code>/sales', TeamSaleView.as_view())
]