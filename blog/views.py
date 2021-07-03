from django.shortcuts import get_object_or_404, render

# Create your views here.

from .models import BlogAuthor, Blog, BlogComment

def index(request):
    """View function for home page of site."""

    return render(request, 'index.html',)

from django.views import generic

class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5

class BlogDetailView(generic.DetailView):
    model = Blog

class BlogAuthorListView(generic.ListView):
    model = BlogAuthor

class BlogAuthorDetailView(generic.DetailView):
    model = BlogAuthor

from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

class BlogCommentCreate(LoginRequiredMixin, CreateView):
    model = BlogComment
    fields = ['description',]

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        # Get the blog form id and add it to the context
        context['blog'] = get_object_or_404(Blog, pk = self.kwargs['pk'])
        return context

    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user
        #Associate comment with blog based on passed id
        form.instance.blog =  get_object_or_404(Blog, pk = self.kwargs['pk'])
        # Call super-class form validation behavior
        return super().form_valid(form)

    def get_success_url(self):
        """
        After posting comment return to associated blog.
        """
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'],})