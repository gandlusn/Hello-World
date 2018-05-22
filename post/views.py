from django.shortcuts import render

from .models import Post

# Create your views here.
def post_home(request):

    posts = Post.objects.order_by('pub_date')
    return render(request,'post/post_home.html',{'posts':posts})

def post(request,post_id):
    post = Post.objects.get(pk=post_id)
    return render(request,'post/post.html',{'post':post})


