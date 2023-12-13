from sqlalchemy.orm import Session

from . import models, schemas

# * DBとデータの送受信を行う

# ユーザー情報を取得
def get_user(db: Session, user_id: int):
    # db.query( 探すテーブル ).filter( 探す条件 )
    # first()：取得したデータの1番目を返す
    return db.query(models.User).filter(models.User.id == user_id).first()

# ユーザーのメールアドレスを取得
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# 複数のユーザーを取得する
def get_users(db: Session, skip: int = 0, limit: int = 100):
    # offset：テーブルの先頭から何番目のデータを取得するか指定
    # limit：取得するデータの最大数を指定
    # all()：取得したデータをすべて返す
    return db.query(models.User).offset(skip).limit(limit).all()

# ユーザー作成
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    # DBに追加
    db.add(db_user)
    # DBに反映
    db.commit()
    # db_userをDBに登録されているデータで更新（id がDBに登録したタイミングで値をセットするため）
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    # **item.dict()：Itemクラスの項目を辞書型にする
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item