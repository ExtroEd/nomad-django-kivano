from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.exceptions import ValidationError
from .models import CustomUser


User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6,
                                     required=True)
    confirm_password = serializers.CharField(write_only=True, min_length=6,
                                             required=True)


    class Meta:
        model = CustomUser
        fields = [
            'username', 'password', 'confirm_password', 'first_name',
            'last_name', 'middle_name', 'email', 'phone', 'address',
            'newsletter_subscription'
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise ValidationError({"password": "Пароли не совпадают."})

        if len(attrs['password']) < 6:
            raise ValidationError(
                {"password": "Пароль должен содержать минимум 6 символов."})

        if not attrs.get('email'):
            raise ValidationError({"email": "Email обязателен."})

        if CustomUser.objects.filter(email=attrs['email']).exists():
            raise ValidationError({"email": "Этот email уже используется."})

        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = CustomUser.objects.create_user(**validated_data)
        return user


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['first_name'] = self.user.first_name
        return data


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name',
                  'middle_name', 'phone', 'address', 'newsletter_subscription')
