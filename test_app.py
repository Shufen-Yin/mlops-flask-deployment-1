from app import app, model_predict

def test_home():
    """Test if the home route is accessible"""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Application is running successfully!" in response.data

def test_predict():
    """Test the prediction route with JSON data"""
    client = app.test_client()
    # Sending mock data
    response = client.post("/predict", json={"data": [1, 2, 3]})
    assert response.status_code == 200
    # 1+2+3 should equal 6
    assert response.get_json() == {"prediction": 6}

def test_model_logic():
    """Test the model function logic directly"""
    assert model_predict([10, 20]) == 30
