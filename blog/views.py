from django.views.generic import TemplateView , ListView , DetailView
from .models import Post
class HomePage(TemplateView):
    template_name = "home.html"
    
class BlogPage(ListView):
    template_name = 'blog.html'
    model = Post
    
class PostDetail(DetailView):
    model = Post
    template_name = 'single-post.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'