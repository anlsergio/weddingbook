from django.urls import path

from gallery.views import ImageListView, ImageCreateView, ImageDetailView

from . import views

urlpatterns = [
    path('', ImageListView.as_view(), name='gallery-home')
]