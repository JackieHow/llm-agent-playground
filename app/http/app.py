#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dotenv
from flask_migrate import Migrate
from pkg.sqlalchemy import SQLAlchemy
from injector import Injector

from config import Config
from internal.router import Router
from internal.server import Http

from .module import ExtensionModule

# 将env加载到环境变量中
dotenv.load_dotenv()

conf = Config()

injector = Injector([ExtensionModule])

app = Http(
    __name__,
    conf=conf,
    db=injector.get(SQLAlchemy),
    migrate=injector.get(Migrate),
    router=injector.get(Router),
)

if __name__ == "__main__":
    app.run(debug=True)
