from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('view/<int:pk>/', views.view, name="view"),
    path('update/<int:pk>/', views.update, name="update"),
    path('create/', views.create, name="create"),
]
