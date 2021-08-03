from rest_framework import serializers
from .models import AccountUser, UserBiography, UserTransaction


class AccountUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = '__all__'


class GetAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = ('username', 'password')


class UserBiographySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBiography
        fields = '__all__'


class UserTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTransaction
        fields = '__all__'
