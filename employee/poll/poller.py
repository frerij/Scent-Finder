import django
import os
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "employee_project.settings")
django.setup()

from employee_rest.models import ProductVO
# from customer_rest.models import UserVO

def get_products():
    response = requests.get("http://inventory-api:8000/api/products/")
    content = json.loads(response.content)
    for product in content["products"]:
        ProductVO.objects.update_or_create(
            import_href=product["href"],
            defaults={
                "name": product["name"],
                "sku": product["sku"],
                "price": product["price"],
                "size": product["size"],
                "quantity": product["quantity"] ,
                "limited_item": product["limited_item"],
                "image": product["image"],
            },
        )

# def get_user():
#     response = requests.get("http://user-api:8100/api/users/")
#     content = json.loads(response.content)
#     for user in content["users"]:
#         UserVO.objects.update_or_create(
#             import_href=user["href"],
#             defaults={
#                 "email": user["name"],
#                 "first_name": user["name"],
#                 "last_name": user["name"]
#             },
#         )


def poll():
    while True:
        print('employee poller polling for data')
        try:
            get_products()
        except Exception as e:
            print(e, file=sys.stderr)
        time.sleep(60)


if __name__ == "__main__":
    poll()
