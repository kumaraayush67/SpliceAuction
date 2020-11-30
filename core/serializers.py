from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Customer

class UserSerializer(serializers.ModelSerializer):
    confirm_email = serializers.EmailField(write_only=True, label='Confirm Email Address')
    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True, label='Confirm Password')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'confirm_email',
                  'password', 'confirm_password']


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = '__all__'
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data.pop('confirm_password')
        user_data.pop('confirm_email')
        user_data['username'] = user_data['email']
        user = User.objects.create_user(**user_data)
        validated_data['user'] = user
        customer = Customer.objects.create(**validated_data)
        return customer
