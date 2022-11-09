# from django.contrib.auth.password_validation import validate_password
# from django.core import exceptions
# from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


# class UserCreateSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = User
#     fields = ['id', 'username', 'email', 'phone','role' ,'password','created_at']

#   def validate(self, data):
#     user = User(**data)
#     password = data.get('password')

#     try:
#       validate_password(password, user)
#     except exceptions.ValidationError as e:
#       serializer_errors = serializers.as_serializer_error(e)
#       raise exceptions.ValidationError(
#         {'password': serializer_errors['non_field_errors']}
#       )

#     return data


#   def create(self, validated_data):
#     user = User.objects.create_user(
#       username=validated_data['username'],
#       role=validated_data['role'],
#       phone=validated_data['phone'],
#       email=validated_data['email'],
#       password=validated_data['password'],
#     )

#     return user


# class UserSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = User
#     fields = ('username', 'phone', 'email',)
from rest_framework import serializers
from .models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'username', 'email', 'phone','role' ,'password','created_at']
    #     extra_kwargs = {
    #         'password': {'write_only': True}
    #     }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['username', 'email' , 'phone' ]

