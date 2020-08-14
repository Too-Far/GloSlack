from django.urls import include, path
from . import views

urlpatterns = [
    path('hook', views.event_hook),
    path('web-hook', views.incoming_web_hook)
]
