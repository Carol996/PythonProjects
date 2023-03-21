from django.urls import path
from . import views

urlpatterns = [
    # sets the url path to home page index.hrml
    path('', views.home, name='index'),
    # sets the url path to Create New Accnt page CreateNewAccount.html
    path('create/', views.create_account, name='create'),
    # sets the url path to Balance Sheet page BalanceSheet.html
    path('<int:pk>/balance/', views.balance, name='balance'),
    # sets the url path to Add New Transaction page AddNewTransaction.html
    path('transaction/', views.transaction, name='transaction')
]
