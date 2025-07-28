from fastapi.testclient import TestClient
from loanapp import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Loan Prediction API is live"}
