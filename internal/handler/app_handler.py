from flask import request
from openai import OpenAI


class AppHandler:
    """应用控制器"""

    def completion(self):
        query = request.json.get("query")
        client = OpenAI()
        completion = client.chat.completions.create(
            model="grok-2-latest",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": query},
            ],
            stream=False,
        )
        content = completion.choices[0].message.content
        return content

    def ping(self):
        return {"ping": "pong"}
