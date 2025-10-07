from django.urls import path
from . import views

app_name = "academy"

urlpatterns = [
    path('', views.home, name="home"),
    path('formations/', views.formation_list, name="formation_list"),
    path('formations/<int:pk>/', views.formation_detail, name="formation_detail"),
    path('videos/', views.video_list, name="video_list"),
    path('videos/<int:pk>/', views.video_detail, name="video_detail"),
    path('gallery/', views.gallery, name="gallery"),
    path('formations/<int:pk>/comment/', views.add_comment, name="add_comment"),
]
