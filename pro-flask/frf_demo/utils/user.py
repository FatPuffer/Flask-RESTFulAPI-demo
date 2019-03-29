# coding: utf-8

from frf_demo.apps.user.models import User


def check_iterate(value):

    if value == 'mobile':
        mobile = User.query.filter_by(mobile=value)
        if mobile:
            raise ValueError("手机号已注册")
        else:
            return value
    elif value == 'uname':
        uname = User.query.filter_by(name=value)
        if uname:
            raise ValueError("用户名已注册")
        else:
            return value
