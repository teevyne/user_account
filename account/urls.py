from django.urls import path

from account.views import AccountUserCreateView, GetAccountNumberByCredentialsView, CreateCustomerIdentityView, \
    get_customer_identity_by_account_number, get_customer_balance_by_account_number

urlpatterns =[
    path('register', AccountUserCreateView.as_view()),
    path('get_account_number', GetAccountNumberByCredentialsView.as_view()),
    path('create_account', CreateCustomerIdentityView.as_view()),
    path('get_customer_identity/<str:account_number>/', get_customer_identity_by_account_number),
    path('get_customer_balance/<str:account_number>/', get_customer_balance_by_account_number),
]