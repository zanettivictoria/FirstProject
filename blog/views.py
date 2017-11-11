from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    Post.objects.filter(publicar_data__lte=timezone.now()).order_by("publicar_data")
    return render(request,'blog/post_list.html',{'posts':posts})

