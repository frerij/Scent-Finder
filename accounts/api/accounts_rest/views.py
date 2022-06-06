from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
import json

from .encoders import AccountModelEncoder
from .models import User

# Create your views here.
def create_user(json_content):
    try:
        content = json.loads(json_content)
    except json.JSONDecodeError:
        return 400, {"message": "Bad JSON"}, None

    required_properties = [
        "username",
        "email",
        "password",
        "first_name",
        "last_name",
    ]
    missing_properties = []
    for required_property in required_properties:
        if required_property not in content or len(content[required_property]) == 0:
            missing_properties.append(required_property)
    if missing_properties:
        response_content = {
            "message": "missing properties",
            "properties": missing_properties,
        }
        return 400, response_content, None

    try:
        account = User.objects.create_user(
            username=content["username"],
            email=content["email"],
            password=content["password"],
            first_name=content["first_name"],
            last_name=content["last_name"],
        )
        return 200, account, account
    except IntegrityError as e:
        return 409, {"message": str(e)}, None
    except ValueError as e:
        return 400, {"message": str(e)}, None


@require_http_methods(["GET", "POST"])
def api_list_accounts(request):
    if request.method == "GET":
        users = User.objects.exclude(email="").filter(is_active=True)
        return JsonResponse(
            {"accounts": users},
            encoder=AccountModelEncoder,
        )
    else:
        status_code, response_content, _ = create_user(request.body)
        response = JsonResponse(
            response_content,
            encoder=AccountModelEncoder,
            safe=False,
        )
        response.status_code = status_code
        return response


@require_http_methods(["GET", "PUT", "DELETE"])
def api_account_detail(request, email):
    try:
        account = User.objects.filter(is_active=True).get(email=email)
    except User.DoesNotExist:
        print("User.DoesNotExist", email)
        if request.method == "GET":
            response = JsonResponse({"message": email})
            response.status_code = 404
            return response
        else:
            account = None

    if request.method == "GET":
        return JsonResponse(
            account,
            encoder=AccountModelEncoder,
            safe=False,
        )
    elif request.method == "PUT":
        try:
            content = json.loads(request.body)
        except json.JSONDecodeError:
            response = JsonResponse({"message": "Bad JSON"})
            response.status_code = 400
            return response

        if "email" in content:
            del content["email"]
        if "username" in content:
            del content["username"]
        if account is not None:
            for property in content:
                if property != "password" and hasattr(account, property):
                    setattr(account, property, content[property])
                elif property == "password":
                    account.set_password(content["password"])
            status = 200
            response_content = account
        else:
            status, response_content, account = create_user(request.body)
        if account:
            account.save()
        response = JsonResponse(
            response_content,
            encoder=AccountModelEncoder,
            safe=False,
        )
        response.status_code = status
        return response
    else:
        account.is_active = False
        account.save()
        response = HttpResponse()
        response.status_code = 204
        return response
