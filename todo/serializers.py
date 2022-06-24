from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from todo.models import Profile

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields = ('email','password')