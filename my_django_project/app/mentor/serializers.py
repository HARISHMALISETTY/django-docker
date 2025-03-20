from rest_framework import serializers
from .models import Mentor
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class MentorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Mentor
        fields = ('id', 'user', 'bio', 'expertise', 'years_of_experience', 
                 'hourly_rate', 'is_available', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at') 