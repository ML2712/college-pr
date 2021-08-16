from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="edge-home"),
    path('blog/', views.blog, name="edge-blog"),
    # path('blogs/<int:pk>/', views.post, name="edge-blog-post"),
    path('about/', views.about, name='edge-about'),
    path('contact/', views.contact, name='edge-contact'),
    path('newsletter/', views.subscribe, name='edge-newsletter'),
]
