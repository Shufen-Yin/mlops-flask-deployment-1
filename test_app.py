import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """测试首页是否正常运行"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Application is running successfully!" in response.data

def test_predict_route(client):
    """测试预测接口逻辑"""
    test_data = {"data": [1, 2, 3, 4, 5]}
    response = client.post('/predict', json=test_data)
    assert response.status_code == 200
    # 验证模拟模型的求和逻辑 (1+2+3+4+5=15)
    assert response.get_json()["prediction"] == 15



