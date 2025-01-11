from django.http import HttpRequest, JsonResponse
from http import HTTPStatus
import django.middleware.csrf as csrf

def get_csrf_token(request: HttpRequest) -> JsonResponse:
    try:
        return JsonResponse({'csrfToken': str(csrf.get_token(request))}, status=HTTPStatus.OK)
    except Exception as e:
        return JsonResponse({'exception:': str(e)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

def get_spotify_token() -> JsonResponse:
    pass

"""
CLIENT: *Sign up is pressed* ->
        Navigate to Spotify auth URL ->
        Accept? -> *Callback endpoint is hit w/ code param* ->
                   Extract code param ->
                   Use code to start hourly loop to make server call for access token ->
                   SERVER: Return access token and save refresh token for user->
                   Navigate to home page
        Reject? -> *Callback endpoint is hit w/ error param* ->
                   Navigate to sign up w/ error displayed

CLIENT: *Log in is pressed* ->
        Validate credentials ->
        Start hourly loop to make server call for access token ->
        SERVER: Set user code ->
        Success? ->
            Navigate to home page
        Error? ->
            Navigate to Spotify auth URL ->
            Accept? -> *Callback endpoint is hit w/ query params* ->
                        Extract code param ->
                        Use code to start hourly loop to make server call for access token ->
                        SERVER: Return access token and save refresh token for user ->
                        Navigate to home page
            Reject? -> *Callback endpoint is hit w/ error param* ->
                        Navigate to log in w/ error displayed
"""