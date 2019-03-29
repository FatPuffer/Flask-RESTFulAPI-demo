# coding:utf-8
import redis


class Config(object):
    """配置参数"""

    SECRET_KEY = "%S-D*d\uk/j@51.65!_?"

    SQLALCHEMY_DATABASE_URL = "myslq://root:123456@127.0.0.1:3306/db_flask"

    # 设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # flask-session配置
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True  # 对cookie中的session_id进行隐藏处理
    PERMANENT_SESSION_LIFETIME = 86499  # session数据的有效期，单位：秒


class DevelopementConfig(Config):
    """开发模式的配置信息"""

    BEBUG = True


class ProductConfig(Config):
    """生产环境配置信息"""
    pass


config_map = {
    'develope': DevelopementConfig,
    'product': ProductConfig,
}











