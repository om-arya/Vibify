from django.contrib import admin
from django.urls import path
import backend.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/create_user', views.create_user, name='create_user'),
    path('user/get_user_by_username', views.get_user_by_username, name='get_user_by_username'),
    path('user/get_user_by_email', views.get_user_by_email, name='get_user_by_email'),
    path('user/set_user_first_name', views.set_user_first_name, name='set_user_first_name'),
    path('user/set_user_last_name', views.set_user_last_name, name='set_user_last_name'),
    path('user/set_user_email', views.set_user_email, name='set_user_email'),
    path('user/set_user_password', views.set_user_password, name='set_user_password'),
    path('user/delete_user', views.delete_user, name='delete_user'),
    path('vibe/create_vibe', views.create_vibe, name='create_vibe'),
    path('vibe/get_vibe', views.get_vibe, name='get_vibe'),
    path('vibe/get_user_vibes', views.get_user_vibes, name='get_user_vibes'),
    path('vibe/set_vibe_color', views.set_vibe_color, name='set_vibe_color'),
    path('vibe/delete_vibe', views.delete_vibe, name='delete_vibe'),
]
