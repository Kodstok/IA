from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.default, name='default'),
    url(r'^page2$', views.page2, name='page2'),
    url(r'^page3$', views.page3, name='page3'),
]