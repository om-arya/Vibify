from django.http import HttpRequest, HttpResponse, JsonResponse
import backend.service.csrf_service as csrf_service
import backend.service.user_service as user_service
import backend.service.vibe_service as vibe_service

def get_csrf_token(request: HttpRequest) -> JsonResponse:
    if request.method == 'GET':
        return csrf_service.get_csrf_token(request)

def create_user(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username: str = request.POST.get('username')
        email: str = request.POST.get('email')
        password: str = request.POST.get('password')
        first_name: str = request.POST.get('first_name')
        last_name: str = request.POST.get('last_name')

        return user_service.create_user(username, email, password, first_name, last_name)

def get_user_by_username(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        username: str = request.GET.get('username')

        return user_service.get_user_by_username(username)

def get_user_by_email(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        email: str = request.GET.get('email')

        return user_service.get_user_by_email(email)

def set_user_first_name(request: HttpRequest) -> HttpResponse:
     if request.method == 'POST':
        username: str = request.POST.get('username')
        new_first_name: str = request.POST.get('new_first_name')

        return user_service.set_user_first_name(username, new_first_name)
     
def set_user_last_name(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username: str = request.POST.get('username')
        new_last_name: str = request.POST.get('new_last_name')

        return user_service.set_user_last_name(username, new_last_name)

def set_user_email(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username: str = request.POST.get('username')
        new_email: str = request.POST.get('new_email')

        return user_service.set_user_email(username, new_email)

def set_user_password(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username: str = request.POST.get('username')
        new_password: str = request.POST.get('new_password')

        return user_service.set_user_password(username, new_password)

def delete_user(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username: str = request.POST.get('username')

        return user_service.delete_user(username)

def create_vibe(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        name: str = request.POST.get('name')
        username: str = request.POST.get('username')
        color: str = request.POST.get('color')

        return vibe_service.create_vibe(name, color, username)
    
def get_vibe(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        username: str = request.GET.get('username')
        name: str = request.GET.get('name')

        return vibe_service.get_vibe(username, name)

def get_user_vibes(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        username: str = request.GET.get('username')

        return vibe_service.get_user_vibes(username)

def set_vibe_color(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username: str = request.POST.get('username')
        name: str = request.POST.get('name')
        new_color: str = request.POST.get('new_color')

        return vibe_service.set_vibe_color(username, name, new_color)
    
def delete_vibe(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username: str = request.POST.get('username')
        name: str = request.POST.get('name')

        return vibe_service.delete_vibe(username, name)