import pandas as pd
from src.model import SemanticSimilarityModel
from tqdm import tqdm
import os

def process_dataset(input_csv, output_csv=None):
    """
    Process a CSV file containing text pairs and compute similarity scores.
    
    Args:
        input_csv (str): Path to input CSV file
        output_csv (str, optional): Path to save results. If None, will save to 
                                 'processed_' + input_filename
    """
    # Set output filename if not provided
    if output_csv is None:
        dirname, filename = os.path.split(input_csv)
        output_csv = os.path.join(dirname, f'processed_{filename}')
    
    # Load the model
    print("Loading the semantic similarity model...")
    model = SemanticSimilarityModel()
    
    # Read the input CSV
    print(f"Reading input file: {input_csv}")
    df = pd.read_csv(input_csv)
    
    # Validate required columns
    required_columns = ['text1', 'text2']
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"Input CSV must contain columns: {required_columns}")
    
    # Compute similarity scores
    print("Computing similarity scores...")
    tqdm.pandas(desc="Processing rows")
    df['similarity_score'] = df.progress_apply(
        lambda row: model.compute_similarity(str(row['text1']), str(row['text2'])), 
        axis=1
    )
    
    # Save results
    print(f"Saving results to: {output_csv}")
    df.to_csv(output_csv, index=False)
    print("Processing complete!")
    
    # Print some statistics
    print("\nSimilarity Score Statistics:")
    print(f"Average similarity score: {df['similarity_score'].mean():.4f}")
    print(f"Minimum similarity score: {df['similarity_score'].min():.4f}")
    print(f"Maximum similarity score: {df['similarity_score'].max():.4f}")
    
    return df

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Process semantic similarity on a CSV file.')
    parser.add_argument('input_file', help='Path to the input CSV file')
    parser.add_argument('--output', '-o', help='Path to save the output CSV file')
    
    args = parser.parse_args()
    
    process_dataset(args.input_file, args.output)
