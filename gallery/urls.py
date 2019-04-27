from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

from gallery.views import ImageListView, ImageCreateView, ImageDetailView, ImageLikeAPIToggle, ImageNonApprovedListView, ImageUpdateView, ImageDeleteView, ImageByLikesListView
from users import views as user_views



urlpatterns = [
    path('', ImageListView.as_view(), name='gallery_home'),
    path('filterbylikes/', ImageByLikesListView.as_view(), name='filtered_gallery_home'),
    path('gallery/<int:pk>/', ImageDetailView.as_view(), name='image_detail'),
    path('gallery/api/<int:pk>/like/', ImageLikeAPIToggle.as_view(), name='api_image_like'),
    path('gallery/new/', ImageCreateView.as_view(), name='image_create'),
    path('gallery/waiting_approval/', ImageNonApprovedListView.as_view(), name='waiting_approval'),
    path('gallery/<int:pk>/update/', ImageUpdateView.as_view(), name='image_update'), 
    path('gallery/<int:pk>/delete/', ImageDeleteView.as_view(), name='image_delete'),
    path('register/', user_views.register, name='register'), 
    path('profile/', user_views.profile, name='profile'), 
    path('about/', views.about, name='about'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', 
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete')
]
