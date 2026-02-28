from django.urls import include, path
from . import views 
from .views import HomeView,blog


urlpatterns = [
    path('index/', views.index, name='index'),
    path('', HomeView.as_view(), name="home"),
    path('home/', HomeView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/category/<str:category>/', views.blog_by_category, name='blog_by_category'),
    path('contact/', views.contact, name='contact'),
    #path('directory/', views.directory, name='directory'),

    path('', include('accounts.urls')),

]