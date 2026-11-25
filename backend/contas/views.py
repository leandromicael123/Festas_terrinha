import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods


@never_cache
@csrf_protect
@require_http_methods(["GET", "POST", "DELETE"])
def sessao(request):
    if request.method == "POST":
        try:
            dados = json.loads(request.body)
        except (ValueError, UnicodeDecodeError):
            dados = None
        if not isinstance(dados, dict) or not all(isinstance(dados.get(k), str) for k in ("username", "password")):
            return JsonResponse({"detail": "Indica username e password."}, status=400)
        user = authenticate(request, username=dados["username"], password=dados["password"])
        if user is None:
            return JsonResponse({"detail": "Credenciais inválidas."}, status=401)
        login(request, user)
    elif request.method == "DELETE":
        logout(request)
    user = request.user
    return JsonResponse({
        "user": {"id": user.pk, "username": user.get_username()} if user.is_authenticated else None,
        "csrfToken": get_token(request),
    })
