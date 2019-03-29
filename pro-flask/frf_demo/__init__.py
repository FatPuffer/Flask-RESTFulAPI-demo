# coding:utf-8

from flask import Flask
import redis
import logging
from logging.handlers import RotatingFileHandler
from flask_session import Session
from flask_wtf import CSRFProtect
from config import config_map
from flask_sqlalchemy import SQLAlchemy


# 数据库
db = SQLAlchemy()

# 创建redis连接
redis_store = None

# 为flask补充csrf防护
csrf = CSRFProtect()

# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG)
# 创建日志记录器，指明日志保存的路径，每个日志文件的最大大小，保存日志文件个数上限
file_log_handler = RotatingFileHandler('logs/log', maxBytes=1024*1024*1000, backupCount=10)
# 创建日志记录格式                   日志等级  输出日志信息的文件名   行数       日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日志记录器
logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    """工厂模式"""

    app = Flask(__name__,
                template_folder='template',
                static_folder='static')

    # 根据配置模式的名字获取配置参数类
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    # 使用app初始化db
    db.init_app(app)

    # 初始化redis工具
    global redis_store
    redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)

    # 利用flask-session，将session数据保存到redis中
    Session(app)

    # 初始化
    csrf.init_app(app)

    from apps.cart import app_cart
    from apps.order import app_order
    from apps.goods import app_goods
    from apps.user import app_user

    app.register_blueprint(app_cart, url_prefix='/cart')
    app.register_blueprint(app_goods, url_prefix='/')
    app.register_blueprint(app_order, url_prefix='/order')
    app.register_blueprint(app_user, url_prefix='/user')

    return app
