from django.urls import path
from .views import *

urlpatterns = [
    path('geners/',GenreListCreateAPIView.as_view()),
    path('geners/<slug:slug>/', GenreRetirieveUPdateDeleteAPIView.as_view()),
    path('author/',AuthorListCreateAPIView.as_view()),
    path('book/<int:pk>/',BookRetireveUpdateDestroyAPIView.as_view()),
    path('author/<int:pk>/',AuyhorRetireveUpdateDestroyAPIView.as_view()),
    path('post/<int:pk>/',PostRetireveUpdateDestroyAPIView.as_view()),
    path('post/',PostListCreateAPIView.as_view()),
    path('auth/',ExampleAuthentication.as_view()),
    path('',BookListCreteAPIView.as_view()),

]

4