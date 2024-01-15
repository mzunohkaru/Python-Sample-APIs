from fastapi import FastAPI, Query, Header, Response
from typing import Annotated, Union


app = FastAPI()

lists = [1,2,3,4,5,6,7,8,9,10,11]

@app.get("/list")
# skip : 何個のデータをスキップするか指定
# limit : 何個のデータを取得するか指定
# http://127.0.0.1:8000/item?skip=1&limit=4
def read_list(skip: int = 0,
              # Query( ( パラメータが提供されなかった場合のデフォルト値 ), (1以上) ,(3以下) ) = ( パラメータが提供されなかった場合のデフォルト値 )
              limit: Annotated[int, Query(default=1, ge=1, le=5)] = 1):
    return {"items": items[skip : skip + limit]}


# @app.get("/lists/{item_id}")
# def read_list(
#     item_id: str,  <- パスパラメーター
#     skip: int = 0, <- クエリパラメーター
#     limit: int = 10):  <- クエリパラメーター
#     return {}


@app.get("/sample/")
def read_sample(
    # レスポンスにHeader情報を付与する
    response: Response,
    # Headerに設定されたAuthデータ
    # Headerの項目名と引数のなめがマッチしている場合にデータを取得する
    authorization: Union[str, None] = Header(default =None)):
    print(authorization)
    response.header["custom-header"] = "123456"
    return {"message": "ヘッダーを取得しました"}