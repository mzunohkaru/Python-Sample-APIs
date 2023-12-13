from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base  # .( 同フォルダ )database.pyのBaseをインポート


class User(Base):
    # テーブル名
    __tablename__ = "users"

    # カラム作成
    # primary_key：主キー
    # index：索引する
    # unique：単一データである
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # Itemクラスと紐付けする
    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    # Userテーブルのidと紐づく
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Userクラスと紐付けする
    owner = relationship("User", back_populates="items")
