#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from injector import Module, Binder

from internal.extension.database_extension import db
# from internal.extension.migrate_extension import migrate



class ExtensionModule(Module):
    """扩展模块的依赖注入"""

    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)
        # binder.bind(Migrate, to=migrate)
