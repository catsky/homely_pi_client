from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic
from django.utils import timezone

from .models import Image


class IndexView(generic.ListView):
  template_name = 'cameras/index.html'
  context_object_name = 'latest_image_list'
  
  def get_queryset(self):
     """Return the last five published images."""
     return Image.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')[:5]
  

class DetailView(generic.DetailView):
  model = Image
  template_name = 'cameras/detail.html'