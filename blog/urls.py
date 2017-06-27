from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='Events'),
    url(r'^articles/', views.articles, name='Articles'),
]