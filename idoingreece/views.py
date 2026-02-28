from django.shortcuts import render, redirect, get_object_or_404 
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import ( TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView,)
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse, reverse_lazy
from django.template.loader import get_template, render_to_string
from django.contrib import messages
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.db.models import Q 
from django.contrib.auth import get_user_model 
from .models import ContactMessage, IdoingreecePost,AboutIdoingreecePost,FirstIdoingreecePost,BlogPost
import os 


def index (request):
    return render (request, 'idoingreece/index.html')

class HomeView(ListView):
    model = IdoingreecePost
    template_name = 'idoingreece/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_about'] = AboutIdoingreecePost.objects.all()
        context['home_first_category'] = FirstIdoingreecePost.objects.all()
        return context


#The first ArticleDetailView page for news and events
'''class ArticleDetailView(DetailView):
    #model = NewsAndEventsPsnRivers
    template_name = 'psnrivers/news_article_detail.html'
    context_object_name = 'article'''




def about (request):
    return render (request, 'idoingreece/about.html')


def contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )
        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")
    return render(request, "idoingreece/contact.html")


# Blog list (all posts)
def blog(request):
    all_posts = BlogPost.objects.order_by('-publish_date')
    paginator = Paginator(all_posts, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = BlogPost.objects.values_list('category', flat=True).distinct()
    recent_posts = BlogPost.objects.order_by('-publish_date')[:5]

    return render(request, 'idoingreece/blog.html', {
        'posts': page_obj,
        'categories': categories,
        'recent_posts': recent_posts,
        'page_obj': page_obj,
        'selected_category': None
    })


# Blog detail
def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'idoingreece/blog_detail.html', {'post': post})

# Filter by category
def blog_by_category(request, category):
    posts = BlogPost.objects.filter(category=category).order_by('-publish_date')
    categories = BlogPost.objects.values_list('category', flat=True).distinct()
    recent_posts = BlogPost.objects.order_by('-publish_date')[:5]

    return render(request, 'idoingreece/blog.html', {
        'posts': posts,
        'categories': categories,
        'recent_posts': recent_posts,
        'selected_category': category,
    })