# Semantic Textual Similarity API

## Overview
This project provides a RESTful API for quantifying the semantic similarity between pairs of text paragraphs using state-of-the-art NLP techniques. It leverages the `sentence-transformers/all-MiniLM-L6-v2` model to compute similarity scores between 0 (completely dissimilar) and 1 (identical meaning).

## Features

- FastAPI-based REST API with automatic documentation (Swagger UI)
- Pre-trained transformer model for accurate semantic similarity scoring
- Simple and intuitive API endpoints
- Containerized deployment with Heroku support
- Comprehensive test suite

## Local Development Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git
- (Optional) Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd semantic_similarity_project
   ```

2. **Create and activate a virtual environment**
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the API Locally

#### Option 1: Using the provided script (Windows)
```bash
.\start_api.bat
```

#### Option 2: Directly with uvicorn
```bash
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`

### Testing the API

1. **Using the interactive documentation**
   - Visit `http://localhost:8000/docs` in your browser
   - Use the Swagger UI to test the `/predict` endpoint

2. **Using the test script**
   ```bash
   python test_api.py
   ```

3. **Using curl**
   ```bash
   curl -X 'POST' \
     'http://localhost:8000/predict' \
     -H 'Content-Type: application/json' \
     -d '{"text1": "The quick brown fox jumps over the lazy dog.", "text2": "A fast brown fox leaps over a sleeping dog."}'
   ```

## API Reference

### POST /predict
Compute the semantic similarity between two text inputs.

**Request Body:**
```json
{
    "text1": "First text to compare",
    "text2": "Second text to compare"
}
```

**Response:**
```json
{
    "text1": "First text to compare",
    "text2": "Second text to compare",
    "similarity_score": 0.85
}
```

## Running Tests

Run the test suite with pytest:
```bash
pytest tests/
```

## Deployment to Heroku

1. **Install the Heroku CLI**
   Follow the instructions at: https://devcenter.heroku.com/articles/heroku-cli


## Project Structure

```
semantic_similarity_project/
├── src/                    # Source code
│   ├── __init__.py         # Package initialization
│   ├── main.py             # FastAPI application
│   └── model.py            # Semantic similarity model
├── tests/                  # Test files
│   └── test_api.py         # API tests
├── .gitignore              # Git ignore file
├── Procfile                # Heroku process file
├── README.md               # This file
├── requirements.txt        # Python dependencies
├── runtime.txt             # Python version for Heroku
└── setup.sh               # Setup script
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create a new Heroku app**
   ```bash
   heroku create your-app-name
   ```

4. **Deploy your code**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push heroku main
   ```

5. **Your API will be live at**
   ```
   https://your-app-name.herokuapp.com/predict
   ```

## Project Structure
- `src/` - Source code for model and API
  - `model.py` - Semantic similarity model implementation
  - `api.py` - FastAPI application
  - `test_model_on_data.py` - Script to test the model on sample data
- `requirements.txt` - Python dependencies
- `Procfile` - Heroku deployment configuration

## Requirements
- Python 3.8+
- See `requirements.txt` for dependencies
