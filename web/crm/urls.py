from django.urls import path

from crm import views

app_name = 'crm'
urlpatterns = [
    path('', views.index, name='index'),
    path("<str:id>/", views.view, name='view')
]
