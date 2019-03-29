from flask_restful import Resource
from flask import request


class CartInfoView(Resource):
    """cart model"""
    def get(self):
        return 'cart page'

    def post(self):
        id = request.form.get('id')
        num = request.form.get('num')
        print id, num
        return {"goods_id": id, "goods_num": num}
