from django.urls import path

from account.views import AccountUserCreateView, GetAccountNumberByCredentialsView, CreateCustomerIdentityView, \
    get_customer_identity_by_account_number, get_customer_balance_by_account_number, UserTransactionCreateView, \
    get_all_transactions_by_account_number, get_transaction_range_for_an_account

urlpatterns =[
    path('register', AccountUserCreateView.as_view()),
    path('get_account_number', GetAccountNumberByCredentialsView.as_view()),
    path('create_account', CreateCustomerIdentityView.as_view()),
    path('get_customer_identity/<str:account_number>', get_customer_identity_by_account_number),
    path('get_customer_balance/<str:account_number>', get_customer_balance_by_account_number),

    path('create_transaction', UserTransactionCreateView.as_view()),
    path('get_account_transaction/<str:account_number>', get_all_transactions_by_account_number),
    path('get_all_transactions/<str:account_number>/<int:month_range>/', get_transaction_range_for_an_account),
]