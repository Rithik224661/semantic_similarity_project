# Semantic Textual Similarity API

## Overview
This project provides a RESTful API for quantifying the semantic similarity between pairs of text paragraphs using state-of-the-art NLP techniques. It leverages the `sentence-transformers/all-MiniLM-L6-v2` model to compute similarity scores between 0 (completely dissimilar) and 1 (identical meaning).

## Features

- FastAPI-based REST API with automatic documentation (Swagger UI)
- Pre-trained transformer model for accurate semantic similarity scoring
- Multiple endpoints for different use cases:
  - Single prediction
  - Batch predictions
  - CSV file processing
- Comprehensive test suite
- Easy deployment to Heroku

## Local Development Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git
- (Optional) Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rithik224661/semantic_similarity_project.git
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
   - Use the Swagger UI to test all available endpoints

2. **Running tests**
   ```bash
   python -m pytest tests/
   ```

## API Endpoints

### 1. Single Prediction
**Endpoint:** `POST /predict`

Compute the semantic similarity between two text inputs.

**Request:**
```json
{
    "text1": "First text to compare",
    "text2": "Second text to compare"
}
```

**Response:**
```json
{
    "similarity score": 0.85
}
```

### 2. Batch Prediction
**Endpoint:** `POST /predict/batch`

Compute similarity scores for multiple text pairs in a single request.

**Request:**
```json
{
    "data": [
        {"text1": "First text 1", "text2": "Second text 1"},
        {"text1": "First text 2", "text2": "Second text 2"}
    ]
}
```

### 3. CSV Processing
**Endpoint:** `POST /predict/csv`

Process a CSV file containing text pairs and return similarity scores.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: file (CSV file with 'text1' and 'text2' columns)

## Dataset Processing

To process the dataset and compute similarity scores:

```bash
python process_dataset.py docs/DataNeuron_Text_Similarity.csv --output docs/processed_output.csv
```

## Project Structure

```
semantic_similarity_project/
├── docs/                    # Documentation and datasets
│   ├── DataNeuron_Text_Similarity.csv         # Sample dataset
│   └── processed_DataNeuron_Text_Similarity.csv  # Processed output
├── src/                    # Source code
│   ├── __init__.py         # Package initialization
│   ├── main.py             # FastAPI application
│   └── model.py            # Semantic similarity model
├── tests/                  # Test files
│   └── test_api.py         # API tests
├── .gitignore              # Git ignore file
├── Procfile                # Heroku process file
├── README.md               # This file
├── process_dataset.py      # Script to process dataset
├── requirements.txt        # Python dependencies
├── run_api.py             # Script to run the API
└── start_api.bat          # Windows batch file to start the API
```

## Deployment to Heroku

1. **Install the Heroku CLI**
   Follow the instructions at: https://devcenter.heroku.com/articles/heroku-cli

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
   https://your-app-name.herokuapp.com/
   ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
