from django.urls import path

from core import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path("tools/date-convert", views.date_convert, name='date_convert')
]
