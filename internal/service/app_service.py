from dataclasses import dataclass
import uuid
 
from flask_sqlalchemy import SQLAlchemy
from injector import inject

from internal.model.app import App
 

@inject
@dataclass
class AppService:
    db: SQLAlchemy

    def create_app(self) -> App:
        app = App()
        app.name = "测试机器人"
        app.account_id = uuid.uuid4()
        app.icon = ""
        app.description = "测试机器人"

        self.db.session.add(app)
        self.db.session.commit()
        return app

    def get_app(self, id: uuid.UUID) -> App:
        app =  self.db.session.query(App).get(id)
        return app
    
    def update_app(self, id: uuid.UUID) -> App:
        app = self.get_app(id)
        app.name = "更新后的机器人"
        self.db.session.commit()
        return app

    def delete_app(self, id: uuid.UUID) -> App:
        app = self.get_app(id)
        self.db.session.delete(app)
        self.db.session.commit()
        return app
