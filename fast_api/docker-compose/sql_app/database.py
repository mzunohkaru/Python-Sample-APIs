from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# * データベースとの通信を行う

# DB指定
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# SQLAlchemyのエンジンを作成
engine = create_engine(
    # 第1引数：DB指定、第2引数：SQLite用に 多対1 で通信できるよう設定（デフォルトでは、1対1の通信。）
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# autocommit：自動で永続データをDBに反映させない
# autoflush：自動で一時データをDBに反映させない
# bind：このセッションで実行されるSQL操作をSQLAlchemyのエンジンに反映させる
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# DBに登録する項目を指定する基礎クラスを作成
Base = declarative_base()