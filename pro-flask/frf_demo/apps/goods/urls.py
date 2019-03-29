from flask_restful import Api
from . import app_goods
from .views import GoodsIndexView

api = Api(app_goods)

api.add_resource(GoodsIndexView, '')
