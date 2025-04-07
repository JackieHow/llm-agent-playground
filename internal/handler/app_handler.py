from dataclasses import dataclass
import uuid
from flask import request
from injector import inject
from openai import OpenAI
from internal.schema.app_schema import CompletionReq
from internal.exception import FailException
from internal.service import AppService
from pkg.response import success_json, success_message, validate_error_json


@inject
@dataclass
class AppHandler:
    """应用控制器"""

    app_service: AppService

    def create_app(self):
        app = self.app_service.create_app()
        return success_message(f"创建应用成功,id:{app.id}")

    def get_app(self, id: uuid.UUID):
        app = self.app_service.get_app(id)
        return success_message(f"获取应用成功,id:{app.id}")

    def update_app(self, id: uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"更新应用成功,id:{app.id}")

    def delete_app(self, id: uuid.UUID):
        app = self.app_service.delete_app(id)
        return success_message(f"删除应用成功,id:{app.id}")

    def completion(self):
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        client = OpenAI()
        completion = client.chat.completions.create(
            model="grok-2-vision-1212",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": req.query.data},
            ],
            stream=False,
        )
        content = completion.choices[0].message.content
        return success_json({"content": content})

    def ping(self):
        raise FailException("ping")
        # return {"ping": "pong"}
