from django.http import HttpRequest, JsonResponse
from http import HTTPStatus
from django.middleware.csrf import get_token

def get_csrf_token(request: HttpRequest) -> JsonResponse:
    try:
        return JsonResponse({'csrfToken': str(get_token(request))}, status=HTTPStatus.OK)
    except Exception as e:
        return JsonResponse({'exception:': str(e)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)