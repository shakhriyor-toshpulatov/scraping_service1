from django.urls import path

from scraping.views import home_view

urlpatterns = [
    path('', home_view, name='home')
]
