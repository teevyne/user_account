import uuid
from uuid import UUID
import datetime
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
from .models import AccountUser, UserBiography, UserTransaction
from .serializer import AccountUserSerializer, GetAccountSerializer, UserBiographySerializer, UserTransactionSerializer


class AccountUserCreateView(generics.CreateAPIView):
    queryset = AccountUser.objects.all()
    serializer_class = AccountUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "There was a problem. Please, try again!"}, status=status.HTTP_400_BAD_REQUEST)

        account_number = random.randint(1000000000, 9999999999)
        print(account_number)

        if serializer.is_valid():
            serializer.save(
                account_number=account_number
            )

        return Response({"message": "Account successfully created"}, status=status.HTTP_201_CREATED)


class GetAccountNumberByCredentialsView(generics.CreateAPIView):
    queryset = AccountUser.objects.all()
    serializer_class = GetAccountSerializer

    def post(self, request, *args, **kwargs):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            queryset = AccountUser.objects.get(username=username, password=password)
            account = queryset.account_number

            return Response({
                "Customer Account Number": account
            })
        except:
            return Response({"message": "Wrong credentials supplied. Please supply correct credentials"})


class CreateCustomerIdentityView(generics.CreateAPIView):
    queryset = UserBiography.objects.all()
    serializer_class = UserBiographySerializer


@api_view((['GET']))
def get_customer_identity_by_account_number(self, account_number):
    try:
        queryset = UserBiography.objects.get(account_user__account_number=account_number)
        serializer = UserBiographySerializer(queryset)
        return Response(serializer.data)
    except:
        return Response({"message": "Wrong account number. Please check and try again"})


@api_view((['GET']))
def get_customer_balance_by_account_number(self, account_number):
    try:
        queryset = UserBiography.objects.get(account_user__account_number=account_number)
        serializer = UserBiographySerializer(queryset)
        return Response({"Customer account balance": serializer.data['account_balance']}, status=status.HTTP_200_OK)
    except:
        return Response({"message": "Wrong account number. Please check and try again"})


class UserTransactionCreateView(generics.CreateAPIView):
    queryset = UserTransaction.objects.all()
    serializer_class = UserTransactionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Something went wrong. Please try later"}, status=status.HTTP_400_BAD_REQUEST)

        txn_id = "5fd132s" + str(uuid.uuid4().hex[:7])

        if serializer.is_valid:
            serializer.save(
                transaction_id=txn_id
            )

        return Response(serializer.data)


@api_view(['GET'])
def get_all_transactions_by_account_number(self, account_number):
    try:
        query = list(UserTransaction.objects.filter(account_user__account_number=account_number).values())
        return Response({
            "status": "success",
            "data": query
        })
    except:
        return Response({"message": "Wrong account number entered"})


def get_transactions_by_month(account_number, month):
    queryset = list(UserTransaction.objects.filter(transaction_date__month=month,
                                                   account_user__account_number=account_number).values())
    return queryset


@api_view(['GET'])
def get_transaction_range_for_an_account(self, account_number, month_range):

    now = datetime.datetime.now()
    starting_month = now.month
    all_transactions = []

    for month in range(month_range):
        actual_month = starting_month - month
        transactions = {
            "transactions": get_transactions_by_month(account_number, actual_month)
        }

        all_transactions.append(transactions)
    return Response({
        "status": "success",
        "data": all_transactions
    })
