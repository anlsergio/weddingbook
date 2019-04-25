from django.urls import path

from gallery.views import ImageListView, ImageCreateView, ImageDetailView

from . import views

urlpatterns = [
    path('', ImageListView.as_view(), name='gallery-home'),
    path('gallery/<int:pk>/', ImageDetailView.as_view(), name='image_detail'),
    path('gallery/new/', ImageCreateView.as_view(), name='image_create'),
]