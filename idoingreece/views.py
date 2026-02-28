from django.shortcuts import render, redirect, get_object_or_404 
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
from .models import ContactMessage, IdoingreecePost,AboutIdoingreecePost
import os 


def index (request):
    return render (request, 'idoingreece/index.html')

class HomeView(ListView):
    model = IdoingreecePost
    template_name = 'idoingreece/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_about'] = AboutIdoingreecePost.objects.all()
        return context


#The first ArticleDetailView page for news and events
'''class ArticleDetailView(DetailView):
    #model = NewsAndEventsPsnRivers
    template_name = 'psnrivers/news_article_detail.html'
    context_object_name = 'article'''




def about (request):
    return render (request, 'idoingreece/about.html')


def contact (request):
    return render (request, 'idoingreece/contact.html')


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



def blog (request):
    return render (request, 'idoingreece/blog.html')