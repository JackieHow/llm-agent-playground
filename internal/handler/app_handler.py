from flask import request
from openai import OpenAI
from internal.schema.app_schema import CompletionReq
from internal.exception import FailException
from pkg.response import success_json, validate_error_json


class AppHandler:
    """应用控制器"""

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
