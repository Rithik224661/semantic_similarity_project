from sentence_transformers import SentenceTransformer, util
import torch

MODEL_NAME = 'sentence-transformers/all-MiniLM-L6-v2'

class SemanticSimilarityModel:
    def __init__(self, model_name=MODEL_NAME):
        """
        Initialize the semantic similarity model.
        
        Args:
            model_name (str): Name of the pre-trained model to use.
        """
        self.model = SentenceTransformer(model_name)
    
    def compute_similarity(self, text1: str, text2: str) -> float:
        """
        Compute the semantic similarity between two texts.
        
        Args:
            text1 (str): First text
            text2 (str): Second text
            
        Returns:
            float: Similarity score between 0 and 1
        """
        # Encode the texts to get their embeddings
        emb1 = self.model.encode(text1, convert_to_tensor=True)
        emb2 = self.model.encode(text2, convert_to_tensor=True)
        
        # Compute cosine similarity and normalize to [0, 1] range
        score = util.cos_sim(emb1, emb2).item()
        normalized_score = max(0.0, min(1.0, (score + 1) / 2))
        
        return round(normalized_score, 4)
