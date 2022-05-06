from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = '__all__'
        