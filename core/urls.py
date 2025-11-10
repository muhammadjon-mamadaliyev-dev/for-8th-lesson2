from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(),name='home'),
    path('posts/<int:pk>', views.PostDetailView.as_view(),name='post-deatil '),
    path('post_f/', views.PostFormView.as_view(),name='post-form'),
    path('post_c/', views.PostCreateView.as_view(),name='post-create'),
    path('post_d/<int:pk>', views.PostDeleteView.as_view(),name='post-delete')
    
]