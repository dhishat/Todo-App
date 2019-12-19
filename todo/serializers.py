# todo/serializers.py

from rest_framework import serializers
from .models import Todo, SignUp

class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = ('id', 'title', 'description', 'completed')


class SignUpSerializer(serializers.ModelSerializer):
  class Meta:
    model = SignUp
    fields = ('uname', 'apt', 'email', 'pwd')
