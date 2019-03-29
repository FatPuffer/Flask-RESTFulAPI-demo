from flask_restful import Api
from . import app_order
from .views import OrderInfoView

api = Api(app_order)

api.add_resource(OrderInfoView, '/orderinfo')
