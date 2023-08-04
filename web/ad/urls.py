from django.urls import path
from django.views.generic import RedirectView
from . import views
urlpatterns = []
urlpatterns += [
    path('', views.index, name='ad'),
]