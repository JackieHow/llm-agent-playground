from flask import Flask, Blueprint
from internal.handler import AppHandler

from injector import inject
from dataclasses import dataclass


@inject
@dataclass
class Router:
    """路由器"""

    app_handler: AppHandler

    def register_router(self, app: Flask):
        """注册路由"""
        # 1.创建一个蓝图
        bp = Blueprint("llmops", __name__, url_prefix="")

        #  2.将url与对应的控制器方法进行绑定
        bp.add_url_rule("/ping", view_func=self.app_handler.ping)
        bp.add_url_rule("app/completion", methods=["POST"],view_func=self.app_handler.completion)
        # 3.将蓝图注册到app
        app.register_blueprint(bp)
