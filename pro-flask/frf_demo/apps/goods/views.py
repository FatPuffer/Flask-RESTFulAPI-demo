from flask_restful import Resource
import logging
from flask import current_app


class GoodsIndexView(Resource):
    """goods model"""
    def get(self):
        logging.info('info msg')  # method1
        current_app.logger.error('errmsg')  # method2
        current_app.logger.info('info message')
        return 'get page'

    def post(self):
        return 'post page'

