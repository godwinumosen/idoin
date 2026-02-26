from django.urls import include, path
from . import views 
from .views import HomeView


urlpatterns = [
    path('index/', views.index, name='index'),
    path('', HomeView.as_view(), name="home"),
    path('home/', HomeView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    #path('directory/', views.directory, name='directory'),

    path('', include('accounts.urls')),

]