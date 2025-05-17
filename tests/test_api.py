import pytest
import pandas as pd
from io import StringIO
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Semantic Similarity API is running. Visit /docs for API documentation."}

def test_predict_similarity():
    test_data = {
        "text1": "This is a test sentence.",
        "text2": "This is another test sentence."
    }
    response = client.post("/predict", json=test_data)
    assert response.status_code == 200
    data = response.json()
    assert "similarity score" in data
    assert isinstance(data["similarity score"], float)
    assert 0 <= data["similarity score"] <= 1

def test_predict_similarity_same_text():
    test_data = {
        "text1": "Identical text",
        "text2": "Identical text"
    }
    response = client.post("/predict", json=test_data)
    assert response.status_code == 200
    data = response.json()
    assert data["similarity score"] == 1.0

def test_batch_prediction():
    test_data = {
        "data": [
            {"text1": "The cat sat on the mat", "text2": "A cat was sitting on the mat"},
            {"text1": "The sky is blue", "text2": "The ocean is deep blue"},
            {"text1": "I love programming", "text2": "Coding is my passion"}
        ]
    }
    response = client.post("/predict/batch", json=test_data)
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert len(data["results"]) == 3
    for result in data["results"]:
        assert "similarity score" in result
        assert 0 <= result["similarity score"] <= 1

def test_csv_prediction():
    # Create a test CSV file in memory
    csv_data = "text1,text2\n" \
              "\"The cat sat on the mat\",\"A cat was sitting on the mat\"\n" \
              "\"The sky is blue\",\"The ocean is deep blue\"\n" \
              "\"I love programming\",\"Coding is my passion\""
    
    # Create a temporary file for testing
    with open("test_data.csv", "w") as f:
        f.write(csv_data)
    
    # Test with file upload
    with open("test_data.csv", "rb") as f:
        files = {"file": ("test_data.csv", f, "text/csv")}
        response = client.post("/predict/csv", files=files)
    
    # Clean up
    import os
    if os.path.exists("test_data.csv"):
        os.remove("test_data.csv")
    
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert len(data["results"]) == 3
    for result in data["results"]:
        assert "similarity score" in result
        assert 0 <= result["similarity score"] <= 1

def test_invalid_csv():
    # Create a temporary invalid CSV file
    with open("invalid_data.csv", "w") as f:
        f.write("invalid,columns\nvalue1,value2")
    
    # Test with invalid CSV format
    with open("invalid_data.csv", "rb") as f:
        files = {"file": ("invalid_data.csv", f, "text/csv")}
        response = client.post("/predict/csv", files=files)
    
    # Clean up
    import os
    if os.path.exists("invalid_data.csv"):
        os.remove("invalid_data.csv")
    
    assert response.status_code == 400
