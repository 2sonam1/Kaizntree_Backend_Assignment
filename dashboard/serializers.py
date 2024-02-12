from rest_framework import serializers
from dashboard.models import User,Item
from django.db import models

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password']
   
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name', 'email']


class ItemAdditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['SKU','name', 'tags','category','inStock','availableStock','created_at']

