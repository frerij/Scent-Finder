from common.json import ModelEncoder
from .models import (
    BodyQuiz,
    Cart,
    HomeQuiz,
    ProductVO,
    WishList,
)


class ProductVOEncoder(ModelEncoder):
    model = ProductVO
    properties = [
        "id",
        "import_href",
        "name",
        "sku",
        "price",
        "image",
        "cartQuantity",
    ]


class BodyQuizEncoder(ModelEncoder):
    model = BodyQuiz
    properties = [
        "id",
        "answer_1",
        "answer_2",
        "answer_3",
        "answer_4",
        "answer_5",
        "created",
        "user",
    ]


class HomeQuizEncoder(ModelEncoder):
    model = HomeQuiz
    properties = [
        "id",
        "answer_1",
        "answer_2",
        "answer_3",
        "answer_4",
        "answer_5",
        "created",
        "user",
    ]


class CartEncoder(ModelEncoder):
    model = Cart
    properties = ["product", "user", "quantity", "totals"]
    encoders = {
        "product": ProductVOEncoder(),
    }


class WishListEncoder(ModelEncoder):
    model = WishList
    properties = ["user", "product"]
    encoders = {
        "product": ProductVOEncoder(),
    }
