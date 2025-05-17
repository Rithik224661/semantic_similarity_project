import requests
import json

def test_api():
    # Test data
    test_data = {
        "text1": "The quick brown fox jumps over the lazy dog.",
        "text2": "A fast brown fox leaps over a sleeping dog."
    }
    
    # Local URL
    url = "http://localhost:8000/predict"
    
    try:
        # Make the POST request
        response = requests.post(url, json=test_data)
        
        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            print("API Response:")
            print(json.dumps(result, indent=2))
            
            # Print a simple interpretation
            score = result.get('similarity_score', 0)
            print(f"\nSimilarity Score: {score:.2f}")
            if score > 0.7:
                print("The texts are very similar.")
            elif score > 0.4:
                print("The texts are somewhat similar.")
            else:
                print("The texts are not very similar.")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    test_api()
