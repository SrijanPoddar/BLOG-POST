from django.urls import path
from .views import BlogPostListCreate, BlogPostRetrieveUpdateDestroy

urlpatterns = [
    path('', BlogPostListCreate.as_view(), name='blogpost-list-create'),
    path('<int:pk>/', BlogPostRetrieveUpdateDestroy.as_view(), name='blogpost-retrieve-update-destroy'),
]