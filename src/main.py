from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import List, Dict, Any
import pandas as pd
import numpy as np
from src.model import SemanticSimilarityModel

app = FastAPI(
    title="Semantic Similarity API",
    description="API for computing semantic similarity between two texts",
    version="1.0.0"
)

# Initialize the model
model = SemanticSimilarityModel()

class TextPair(BaseModel):
    text1: str
    text2: str

class BatchRequest(BaseModel):
    data: List[Dict[str, str]]

@app.get("/")
async def read_root():
    return {"message": "Semantic Similarity API is running. Visit /docs for API documentation."}

@app.post("/predict")
async def predict_similarity(pair: TextPair):
    """
    Predict similarity score between two texts.
    
    Args:
        pair: A JSON object containing 'text1' and 'text2' strings
        
    Returns:
        A JSON object with the similarity score
    """
    try:
        similarity_score = model.compute_similarity(pair.text1, pair.text2)
        return {"similarity score": float(similarity_score)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict/batch")
async def predict_batch_similarity(request: BatchRequest):
    """
    Predict similarity scores for multiple text pairs in batch.
    
    Args:
        request: A JSON object containing a list of text pairs
        
    Returns:
        A JSON object with similarity scores for each pair
    """
    try:
        results = []
        for item in request.data:
            score = model.compute_similarity(item['text1'], item['text2'])
            results.append({
                'text1': item['text1'],
                'text2': item['text2'],
                'similarity score': float(score)
            })
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict/csv")
async def predict_from_csv(file: UploadFile = File(...)):
    """
    Process a CSV file containing text pairs and return similarity scores.
    
    Expected CSV format:
        text1,text2
        "first text","second text"
        ...
    """
    try:
        # Read the CSV file
        try:
            df = pd.read_csv(file.file)
        except pd.errors.EmptyDataError:
            raise HTTPException(
                status_code=400,
                detail="The CSV file is empty"
            )
        except pd.errors.ParserError:
            raise HTTPException(
                status_code=400,
                detail="Invalid CSV format"
            )
        
        # Validate required columns
        if not all(col in df.columns for col in ['text1', 'text2']):
            raise HTTPException(
                status_code=400,
                detail="CSV must contain 'text1' and 'text2' columns"
            )
        
        # Validate data types
        if not all(isinstance(x, str) for x in df['text1']) or not all(isinstance(x, str) for x in df['text2']):
            raise HTTPException(
                status_code=400,
                detail="Text columns must contain string values"
            )
        
        # Process each row
        results = []
        for _, row in df.iterrows():
            try:
                score = model.compute_similarity(str(row['text1']), str(row['text2']))
                results.append({
                    'text1': row['text1'],
                    'text2': row['text2'],
                    'similarity score': float(score)
                })
            except Exception as e:
                raise HTTPException(
                    status_code=400,
                    detail=f"Error processing row {_ + 1}: {str(e)}"
                )
        
        return {"results": results}
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
