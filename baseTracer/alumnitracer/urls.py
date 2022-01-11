from django.urls import path
from django.urls.resolvers import URLPattern
from .views import test


urlpatterns = [
    path('', test)
]