from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Image

def index(request):
  latest_image_list = Image.objects.order_by('-created_at')[:5]
  context = {
     'latest_image_list': latest_image_list,
  }
  return render(request, 'cameras/index.html', context)

def detail(request, image_id):
  image = get_object_or_404(Image, pk=image_id)
  return render(request, 'cameras/detail.html', {'image': image})
