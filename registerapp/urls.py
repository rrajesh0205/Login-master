from django.urls import path 
from .views import ArticleListView, ArticleDetailView, CreatePostView, ArticleUpdate, ArticleDelete, ArticleAboutView

from .import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('test', views.test, name='test'),
    path('testnew', views.testnew, name='testnew'),
    path('logout', views.logout, name='logout'),
    path('created', views.created, name='created'),

    path('create/', CreatePostView.as_view(), name='create'),
    path('create/<int:pk>/', ArticleUpdate.as_view(), name='article_edit'),
    path('delete/<int:pk>/', ArticleDelete.as_view(), name='delete'), 
    ]
