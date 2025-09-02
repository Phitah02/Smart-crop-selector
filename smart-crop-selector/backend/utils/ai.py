
import os
from openai import OpenAI
import requests
from dotenv import load_dotenv

load_dotenv()

def get_crop_recommendations(soil, rainfall, region):
    prompt = f"Suggest 3 crops suitable for {soil} soil, {rainfall} rainfall, in {region}."
    # Try OpenAI first
    try:
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=100
        )
        crops = response.choices[0].text.strip().split('\n')
        return crops, None
    except Exception as e:
        # Fallback to Hugging Face
        try:
            hf_token = os.getenv('HF_API_TOKEN')
            headers = {"Authorization": f"Bearer {hf_token}"}
            payload = {
                "inputs": prompt,
                "parameters": {"max_new_tokens": 60}
            }
            response = requests.post(
                "https://api-inference.huggingface.co/models/bigscience/bloomz-560m",
                headers=headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            result = response.json()
            if isinstance(result, list) and len(result) > 0 and 'generated_text' in result[0]:
                crops = result[0]['generated_text'].strip().split('\n')
                return crops, None
            elif isinstance(result, dict) and 'error' in result:
                return [], f"Hugging Face error: {result['error']}"
            else:
                return [], "Hugging Face returned unexpected response."
        except Exception as hf_e:
            # Fallback to dummy data if both APIs fail
            dummy_crops = ["Maize", "Beans", "Tomatoes"]
            return dummy_crops, None
