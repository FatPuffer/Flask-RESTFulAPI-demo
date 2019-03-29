from flask_restful import Api
from .views import CartInfoView
from . import app_cart

api = Api(app_cart)
api.add_resource(CartInfoView, '/cartinfo')
