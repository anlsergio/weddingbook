from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, RedirectView

from gallery.models import Image

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

# Create your views here.


def home(request):
    context: {
        'images': Image.objects.all()
    }
    return render(request, 'gallery/home.html', context)


class ImageListView(ListView):
    model = Image
    template_name = 'gallery/home.html'
    context_object_name = 'images'
    ordering = ['-date_posted']
    paginate_by = '6'


class ImageDetailView(DetailView):
    model = Image


class ImageCreateView(CreateView):
    model = Image
    fields = [
        'title',
        'image'
    ]


class ImageLikeRedirect(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'image_detail'

    def get_redirect_url(self, *args, **kwargs):
        image_obj = get_object_or_404(Image, pk=kwargs['pk'])

        user = self.request.user

        if user.is_authenticated:
            if user in image_obj.likes.all():
                image_obj.likes.remove(user)
            else:
                image_obj.likes.add(user)

        return image_obj.get_absolute_url()



class ImageLikeAPIToggle(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None, *args, **kwargs):
        image_obj = get_object_or_404(Image, pk=kwargs['pk'])
        user = self.request.user
        updated = False 
        liked = False

        if user.is_authenticated:
            if user in image_obj.likes.all():
                liked = False
                image_obj.likes.remove(user)
            else:
                liked = True
                image_obj.likes.add(user)
            updated = True

        counts=image_obj.likes.count()

        data = {
            "updated": updated,
            "liked": liked,
            "likescount": counts
        }

        return Response(data)
