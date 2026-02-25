from django.urls import include, path
from . import views 
from .views import HomeView


urlpatterns = [
    path('index/', views.index, name='index'),
    path('', HomeView.as_view(), name="home"),
    path('home/', HomeView.as_view(), name='home'),
    #path('news_events/', NewsAndEventsView.as_view(), name='news_events'),
    #path('article/<int:pk>/', ArticleDetailView.as_view(), name="detail"),
    #path('upcoming_news_events/', UpcomingNewsAndEventsView.as_view(), name='upcoming_news_events'),
    path('about/', views.about, name='about'),
    path('directory/', views.directory, name='directory'),

    path('', include('accounts.urls')),

]