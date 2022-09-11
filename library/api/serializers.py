from rest_framework import serializers
from library_app.models import *
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author')


