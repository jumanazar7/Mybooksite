from rest_framework import serializers
from library.models import *
from .models import Post


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"