#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/3/29 15:10
@Author  : thezehui@gmail.com
@File    : http.py
"""
import os

from flask import Flask
from flask_migrate import Migrate


from config import Config
from internal.exception import CustomException
from internal.router import Router
from pkg.response import json, Response, HttpCode
from pkg.sqlalchemy import SQLAlchemy


class Http(Flask):
    """Http服务引擎"""

    def __init__(
        self,
        *args,
        conf: Config,
        db: SQLAlchemy,
        migrate: Migrate,
        router: Router,
        **kwargs,
    ):
        # 1.调用父类构造函数初始化
        super().__init__(*args, **kwargs)

        # 2.初始化应用配置
        self.config.from_object(conf)

        # 3.注册绑定异常错误处理
        self.register_error_handler(Exception, self._register_error_handler)

        # 4.初始化数据库
        db.init_app(self)
        migrate.init_app(self, db, directory="internal/migration")

        # 5.注册应用路由
        router.register_router(self)

    def _register_error_handler(self, error: Exception):
        # 1.异常信息是不是我们的自定义异常，如果是可以提取message和code等信息
        if isinstance(error, CustomException):
            return json(
                Response(
                    code=error.code,
                    message=error.message,
                    data=error.data if error.data is not None else {},
                )
            )
        # 2.如果不是我们的自定义异常，则有可能是程序、数据库抛出的异常，也可以提取信息，设置为FAIL状态码
        if self.debug or os.getenv("FLASK_ENV") == "development":
            raise error
        else:
            return json(
                Response(
                    code=HttpCode.FAIL,
                    message=str(error),
                    data={},
                )
            )
