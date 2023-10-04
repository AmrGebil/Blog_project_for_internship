from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import Account, Profile


class AccountSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize CustomUser model.
    """

    class Meta:
        model = Account
        fields = ('email','frist_name','last_name','username')


class UserRegisterationSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize registration requests and create a new user.
    """

    class Meta:
        model = Account
        fields = ("id",'email','frist_name','last_name','username' "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer class to authenticate users with email and password.
    """
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("you should enter email or user name correct")


class ProfileSerializer(AccountSerializer):
    """
    Serializer class to serialize the user Profile model
    """

    class Meta:
        model = Profile
        fields = ("bio",)


class ProfileAvatarSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize the avatar
    """

    class Meta:
        model = Profile
        fields = ("avatar",)