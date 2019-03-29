# coding:utf-8

from flask_restful import Resource
from flask_restful import reqparse
from sqlalchemy.exc import IntegrityError
from frf_demo import db
from flask import current_app
from models import User
from frf_demo.utils.user import check_iterate


parser = reqparse.RequestParser()
parser.add_argument('uname', type=check_iterate, required=True, location='form', help='用户名重复')
parser.add_argument('password', required=True, type=str, location='form', help='密码不能为空')
parser.add_argument('mobile', type=check_iterate, required=True, location='form', help='密码重复')


class RegisterView(Resource):
    def get(self):
        return 'get retister page'

    def post(self):
        args = parser.parse_args()
        user = User(name=args['uname'], password=args['upwd'], mobile=args['mobile'])
        try:
            db.session.add(user)
            db.commit()

        except IntegrityError as e:
            # 数据库出错回滚
            db.session.rollback()
            # 手机号重复，记录错误日志
            current_app.logger.error(e)
            return {"errno": 0, "errmsg": "手机号已注册"}

        except Exception as e:
            # 数据库出错回滚
            db.session.rollback()
            current_app.logger.error(e)
            return {"errno": 0, "errmsg": "数据库查询异常"}

        return {"errno": 1, "errmsg": "注册成功"}