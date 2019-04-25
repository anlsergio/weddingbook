from django.urls import path

from gallery.views import ImageListView, ImageCreateView, ImageDetailView, ImageLikeRedirect, ImageLikeAPIToggle

from . import views

urlpatterns = [
    path('', ImageListView.as_view(), name='gallery-home'),
    path('gallery/<int:pk>/', ImageDetailView.as_view(), name='image_detail'),
    path('gallery/<int:pk>/like/', ImageLikeRedirect.as_view(), name='image_like'),
    path('gallery/api/<int:pk>/like/', ImageLikeAPIToggle.as_view(), name='api_image_like'),
    path('gallery/new/', ImageCreateView.as_view(), name='image_create'),
]
