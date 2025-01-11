from django.contrib import admin
from django.urls import path
import backend.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/get_csrf_token/', views.get_csrf_token, name='auth/get_csrf_token/'),
    path('users/create_user/', views.create_user, name='users/create_user/'),
    path('users/authenticate_user_by_username/', views.authenticate_user_by_username, name='users/authenticate_user_by_username/'),
    path('users/authenticate_user_by_email/', views.authenticate_user_by_email, name='users/authenticate_user_by_email/'),
    path('users/set_user_email/', views.set_user_email, name='users/set_user_email/'),
    path('users/set_user_password/', views.set_user_password, name='users/set_user_password/'),
    path('users/set_user_first_name/', views.set_user_first_name, name='users/set_user_first_name/'),
    path('users/set_user_last_name/', views.set_user_last_name, name='users/set_user_last_name/'),
    path('users/delete_user/', views.delete_user, name='users/delete_user/'),
    path('vibes/create_vibe/', views.create_vibe, name='vibes/create_vibe/'),
    path('vibes/get_vibe/', views.get_vibe, name='vibes/get_vibe/'),
    path('vibes/get_user_vibes/', views.get_user_vibes, name='vibes/get_user_vibes/'),
    path('vibes/set_vibe_color/', views.set_vibe_color, name='vibes/set_vibe_color/'),
    path('vibes/delete_vibe/', views.delete_vibe, name='vibes/delete_vibe/'),
]
