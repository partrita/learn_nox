# app/routers/items.py (예시)
from fastapi import APIRouter, HTTPException
from ..schemas import Item  # Item 스키마 임포트

router = APIRouter(prefix="/items", tags=["items"])

items = []
item_id_counter = 0


@router.post("/", response_model=Item, status_code=201)
async def create_item(item: Item):
    global item_id_counter
    item_id_counter += 1
    new_item = item.dict()
    new_item["id"] = item_id_counter
    items.append(new_item)
    return new_item


# ... 다른 아이템 관련 라우터 ...
@router.get("/{item_id}", response_model=Item)
async def read_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
