from django.urls import path
from . import views as pages_views
urlpatterns = [
    path('', pages_views.index,name="home"),
    path('about/', pages_views.about,name="about"),
    path('contact/', pages_views.contact,name="contact"),
]