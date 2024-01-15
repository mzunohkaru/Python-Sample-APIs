from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None


@app.get("/mix")
async def index():
    return {
        "str": "hello",
        "int": 230,
        "bool": True,
        "list": [1, 2, 3, "あいう", "a i u"],
        "dict": {"key": "val", "K": 1000},
    }


inventory = {
    1: {
        "name": "Mike",
        "price": 3.99,
        "brand": "Regular",
    },
    2: {
        "name": "mmm",
        "price": 4.99,
        "brand": "Premium",
    },
}


# http://127.0.0.1:8000/get-item/1
@app.get("/get-item/{item_id}")
async def get_item(
    item_id: int = Path(
        None, description="The ID of the item you'd like to view.", gt=0
    )
):
    return inventory[item_id]


# http://127.0.0.1:8000/get-by-name/1?test=2&name=Mike
# {"name":"Mike","price":3.99,"brand":"Regular"}
@app.get("/get-by-name/{item_id}")
async def get_item(*, item_id: int, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    # return {"Data": "Not found"}
    raise HTTPException(status_code=404, detail="Item name not found.")


# http://127.0.0.1:8000/get-by-name-query/?name=Mike
# {"name":"Mike","price":3.99,"brand":"Regular"}
@app.get("/get-by-name-query")
async def get_item_query(
    name: str = Query(
        # title: このパラメータは、ドキュメンテーションで表示されるクエリパラメータの名前を設定します。
        # description: このパラメータは、ドキュメンテーションで表示されるクエリパラメータの詳細な説明を提供します。
        # これらより、Swagger UIを見た時、クエリパラメータ( name )がアイテムの名前を指定するために使用されることを理解できます。
        None,
        title="Name",
        description="Name of item",
        min_length=3,
        max_length=10,
    )
):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not found"}


@app.post("/create-item/{item_id}")
async def create_item(item_id: int, item: Item):
    if item_id in inventory:
        # return {"Error": "Item ID already exists."}
        raise HTTPException(status_code=400, detail="Item ID already exists.")

    inventory[item_id] = item
    return inventory[item_id]


@app.put("/update-item/{item_id}")
async def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        # return {"Error": "Item ID dose not already exists."}
        raise HTTPException(status_code=404, detail="Item ID dose not already exist.")

    if item.name != None:
        inventory[item_id].name = item.name

    if item.price != None:
        inventory[item_id].price = item.price

    if item.brand != None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]


@app.delete("/delete-item")
async def delete_item(
    item_id: int = Query(..., description="The ID of the item to delete", gt=0)
):
    if item_id not in inventory:
        # return {"Error": "ID does not exist."}
        raise HTTPException(status_code=404, detail="ID does not exist.")

    del inventory[item_id]
    return {"Success": "Item deleted"}
