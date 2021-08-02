from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
from .models import AccountUser, UserBiography
from .serializer import AccountUserSerializer, GetAccountSerializer, UserBiographySerializer


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
