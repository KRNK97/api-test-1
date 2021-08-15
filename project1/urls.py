from app.views import *
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/',CreateUser.as_view(),name="create"),
    path('users/',ListUser.as_view(),name="list"),
    path('users/delete/<int:pk>',DeleteUser.as_view(),name="delete"),
    path('users/edit/<int:pk>',UpdateUser.as_view(),name="update")
]
