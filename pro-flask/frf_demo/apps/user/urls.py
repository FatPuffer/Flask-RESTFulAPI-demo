from flask_restful import Api
from . import app_user
from .views import RegisterView

api = Api(app_user)

api.add_resource(RegisterView, '/register')