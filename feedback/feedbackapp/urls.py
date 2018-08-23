"""Urls for feedback app."""
from django.conf.urls import url

from .import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(
        r'^send-mail',
        views.send_feedback_mail, name='send_mail'),
]
