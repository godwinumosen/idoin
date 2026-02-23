from django.urls import path
from . import views 
#from .views import HomeView


urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    #path('', HomeView.as_view(), name="home"),
    #path('home/', HomeView.as_view(), name='home'),
    #path('news_events/', NewsAndEventsView.as_view(), name='news_events'),
    #path('article/<int:pk>/', ArticleDetailView.as_view(), name="detail"),
    #path('upcoming_news_events/', UpcomingNewsAndEventsView.as_view(), name='upcoming_news_events'),
    #path('contact/', views.contact, name='contact'),

]