from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import TodoSerializer, SignUpSerializer      # add this
from .models import Todo, SignUp                     # add this

class TodoView(viewsets.ModelViewSet):       # add this
  serializer_class = TodoSerializer          # add this
  queryset = Todo.objects.all()              # add this


class SignUpView(viewsets.ModelViewSet):       # add this
  serializer_class = SignUpSerializer          # add this
  queryset = SignUp.objects.all()
