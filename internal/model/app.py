
import datetime
import uuid
from internal.extension.database_extension import db

from sqlalchemy import Column, String, DateTime, UUID, Text, PrimaryKeyConstraint, Index


class App(db.Model):
    # AI应用基础类
    __tablename__ = "app"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="pk_app_id"),
        Index("idx_app_account_id", "account_id"),
    )

    id = Column(UUID, default=uuid.uuid4, nullable=False, comment="主键")
    account_id = Column(UUID, default="", nullable=False, comment="账号ID")
    name = Column(String(255), default="", nullable=False, comment="名称")
    icon = Column(String(255), default="", nullable=True, comment="图标")
    description = Column(Text, default="", nullable=True, comment="描述")
    update_at = Column(
        DateTime,
        default=datetime.datetime.now(),
        nullable=False,
        onupdate=datetime.datetime.now(),
        comment="更新时间",
    )
    create_at = Column(
        DateTime, default=datetime.datetime.now(), nullable=False, comment="创建时间"
    )
