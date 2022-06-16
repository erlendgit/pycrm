from django.urls import path

from crm import views

app_name = 'crm'
urlpatterns = [
    path("create/", views.create, name='create'),
    path("<str:id>/update/", views.update, name='update'),
    path("<str:id>/relate/", views.relate, name='relate'),
    path("<str:id>/delete/", views.delete, name='delete'),
    path("<str:id>/", views.view, name='view'),
    path('', views.index, name='index'),
]
