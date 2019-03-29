from flask_restful import Resource


class OrderInfoView(Resource):
    """order model"""
    def get(self):
        return 'order page'

    def post(self):
        return 'post order page'
