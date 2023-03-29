from django.shortcuts import render,get_object_or_404
from .serializers import *
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from library.models import *
from rest_framework import status,generics
from rest_framework.permissions import *
from .permissions import IsAuthorOrReadOnly,CustomDjangoModelPermission
from rest_framework.authentication import *
from .pagination import CustomPaagination
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie ,vary_on_headers



class GenreListCreateAPIView(APIView):
    """BU yerda Genre Ro'yhati"""
    serializer_class = GenreSerializers

    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_cookie)
    def get(self,request,*args,**kwargs):
        genre = Genre.objects.all()
        serializer =self.serializer_class(genre,many=True)
        return Response(data=serializer.data)

    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)


class GenreRetirieveUPdateDeleteAPIView(APIView):
    serializer_class = GenreSerializers
    def get(self,request,slug):
        ganre = get_object_or_404(Genre, slug=slug)
        serializer = self.serializer_class(ganre)
        return Response(data=serializer.data)
    def put(self, request,slug):
        data= request.data
        ganre = get_object_or_404(Genre, slug=slug)
        serializer =self.serializer_class(instance=ganre,data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
        

    def patch(self, request,slug):
        data= request.data
        ganre = get_object_or_404(Genre, slug=slug)
        serializer =self.serializer_class(instance=ganre,data=data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


    def delete(self, request,slug):
        ganre = get_object_or_404(Genre, slug=slug)
        ganre.delete()
        return Response(data={"deleted":"Genre"},status=status.HTTP_204_NO_CONTENT)
        


class BookListCreteAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    pagination_class = CustomPaagination


class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    pagination_class = CustomPaagination

class BookRetireveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    pagination_class = CustomPaagination

class AuyhorRetireveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    pagination_class = CustomPaagination

class PostListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.published.all()
    permission_classes = [DjangoModelPermissions]

class PostRetireveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.published.all()
    permission_classes = [IsAuthorOrReadOnly]


class ExampleAuthentication(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    def get(self,request):
        context = {
            "Email":str(request.user),
            "auth":str(request.auth),   
        }
        return Response(context)


# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class =BookSerializers

# class BookCretedAPIView(generics.CreateAPIView):
#     serializer_class =BookSerializers
#     queryset = Book.objects.all()
