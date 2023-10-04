# from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Account,Profile


class AccountSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize CustomUser model.
    """
    class Meta:
        model = Account
        fields = ('email','username')


class AccountRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)





class ProfileSerializer(AccountSerializer):
    """
    Serializer class to serialize the user Profile model
    """

    class Meta:
        model = Profile
        fields = ("bio","frist_name","last_name")


class ProfileAvatarSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize the avatar
    """

    class Meta:
        model = Profile
        fields = ("avatar",)