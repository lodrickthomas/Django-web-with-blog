from django.urls import path, re_path
from . import views as articles_views



urlpatterns = [
    path('', articles_views.articleslist, name="articleslist"),
    path(r'^(?P<slug>[\w-]+)/$', articles_views.articlesdetails, name="articlesdetails"),
    # path('', articles_views.articleslist, name="articleslist"),
]