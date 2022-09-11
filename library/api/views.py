from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from library_app.models import *
from .serializers import BookSerializer


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailBook(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateBook(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteBook(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

