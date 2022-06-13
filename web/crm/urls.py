from django.urls import path

from crm import views

app_name = 'crm'
urlpatterns = [
    path("<str:id>/update", views.update, name='update'),
    path("<str:id>/", views.view, name='view'),
    path('', views.index, name='index'),
]
