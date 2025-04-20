from fastapi.testclient import TestClient
from app.main import app  # FastAPI 애플리케이션 인스턴스 가져오기

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# 필요에 따라 다른 API 엔드포인트 및 기능을 테스트하는 함수를 추가합니다.
# 예를 들어, app/routers/items.py 에 정의된 엔드포인트를 테스트할 수 있습니다.

# 예시: items 라우터에 정의된 POST 엔드포인트 테스트 (가정)
def test_create_item():
    item_data = {"name": "Test Item", "description": "This is a test item."}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 201
    assert response.json()["name"] == "Test Item"
    assert response.json()["description"] == "This is a test item."
    assert "id" in response.json()

# 예시: items 라우터에 정의된 GET 특정 아이템 엔드포인트 테스트 (가정)
def test_read_item():
    # 먼저 아이템을 생성해야 테스트 가능
    item_data = {"name": "Get Item", "description": "Item to get."}
    create_response = client.post("/items/", json=item_data)
    item_id = create_response.json()["id"]

    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Get Item"
    assert response.json()["id"] == item_id

# ... 더 많은 테스트 함수를 추가하여 앱의 다양한 기능을 검증할 수 있습니다.
