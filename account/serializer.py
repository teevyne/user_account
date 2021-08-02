from rest_framework import serializers
from .models import AccountUser, UserBiography


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
