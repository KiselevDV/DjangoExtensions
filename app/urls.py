from django.urls import path

from .views import hello_world

app_name = 'app'
urlpatterns = [
    path('', hello_world, name='hello_world'),
]
