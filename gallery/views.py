from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from gallery.models import Image

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