from django.conf.urls import url

from userprofile import views

urlpatterns = [
    url(r'^login/', views.login),
]