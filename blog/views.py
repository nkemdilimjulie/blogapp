from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from blog.models import Post
#from .models import Post

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class PostListView(ListView):
    context_object_name = "my_posts"
    model = Post
    template_name = "post_list.html"

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'  # Path to your detail template
    context_object_name = 'post'  # Optional: Changes the context variable name from 'object' to 'post'

def post_list(request):
    posts = (
        Post.objects.all()
    )  # retrieves all posts WITHOUT context_object_name. {posts: Post.objects.all()}. Post is model name or class name of  model db table(see models.py)
    return render(
        request, "post_list.html", {"posts": posts}
    )  
    # WITHOUT context_object_name: {posts: Post.objects.all()} - posts is defined in this current method
    # WITH context_object_name: {my_posts: Post.objects.all()} - my_posts is defined in PostListView class
