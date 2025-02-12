from django.urls import path
from . import views
from .views import NewsDetailView, NewsUpdateView, NewsDeleteView

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('Add/', views.add, name='Add'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', NewsDeleteView.as_view(), name='news-delete'),

]
