# -*- coding: utf-8 -*-
"""IBM Hackathon.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AgPQ1_qrOxQtiEzbp4_Pd-RTaT0fsUTm
"""

!git config --global credential.helper store

!huggingface-cli login

!pip install transformers torch huggingface_hub

!pip install huggingface_hub
!huggingface-cli login

from huggingface_hub import login

login(token="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")

from transformers import AutoModelForCausalLM, AutoTokenizer

# Load IBM Granite model and tokenizer
model_name = "ibm-granite/granite-3.3-2b-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(user_input):
    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example usage
user_query = "What are the symptoms of flu?"
response = generate_response(user_query)
print("AI Response:", response)

#Health Recomendation
from transformers import AutoModelForCausalLM, AutoTokenizer

# Loading IBM Granite 3.3-2B Base Model
model_name = "ibm-granite/granite-3.3-2b-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def get_health_recommendation(diagnosed_condition):
    """Generates AI-driven health recommendations using IBM Granite."""
    prompt = f"What are the recommended treatments for {diagnosed_condition}?"

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=100)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example Usage
diagnosed_condition = "Flu"
recommendation = get_health_recommendation(diagnosed_condition)

print("Health Recommendation:", recommendation)

#Emergency alert
def check_emergency_symptoms(symptoms):
    """Uses IBM Granite AI to assess life-threatening symptoms."""
    prompt = f"Is {symptoms} a medical emergency? Provide urgent response."

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=100)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example Usage
user_symptoms = "Chest pain and difficulty breathing"
emergency_message = check_emergency_symptoms(user_symptoms)

print("Emergency Alert:", emergency_message)

#Finding Nearby Hospitals
import requests

GOOGLE_MAPS_API_KEY = "AIzaSyAyi5NyPS-X2pMkTkzGu4ypDqUpMAS8d6M"
LOCATION = "Mancherial"  # Replace with user's actual location

def find_nearby_hospitals(location):
    """Fetch nearby hospitals using Google Maps API."""
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=17.6254,79.4373&radius=5000&type=hospital&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        hospitals = response.json()["results"][:5]  # Get top 5 hospitals
        return [hospital["name"] for hospital in hospitals]
    else:
        return "Error fetching hospital data."

# Example Usage
hospital_list = find_nearby_hospitals(LOCATION)
print("Nearby Hospitals:", hospital_list)

#Secure authentication for api access
import hashlib

def generate_secure_token(user_id):
    """Generate hashed authentication token for user privacy."""
    secret_key = "AIzaSyAyi5NyPS-X2pMkTkzGu4ypDqUpMAS8d6M"
    return hashlib.sha256(f"{user_id}{secret_key}".encode()).hexdigest()

# Example Usage
user_id = "User123"
secure_token = generate_secure_token(user_id)

print("Generated Secure Token:", secure_token)

#Ecrypting health data before storing
from cryptography.fernet import Fernet

# Generate encryption key
encryption_key = Fernet.generate_key()
cipher = Fernet(encryption_key)

def encrypt_user_data(data):
    """Encrypt health data before storing."""
    return cipher.encrypt(data.encode())

def decrypt_user_data(encrypted_data):
    """Decrypt stored health data."""
    return cipher.decrypt(encrypted_data).decode()

# Example Usage
user_health_data = "Diagnosed with flu. Prescribed medications: Paracetamol."
encrypted_data = encrypt_user_data(user_health_data)
decrypted_data = decrypt_user_data(encrypted_data)

print("Encrypted Health Data:", encrypted_data)
print("Decrypted Health Data:", decrypted_data)

!pip install gradio

import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer

# Loading IBM Granite model
model_name = "ibm-granite/granite-3.3-2b-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def analyze_symptoms(user_input):
    """Generates AI-driven health recommendations using IBM Granite."""
    prompt = f"What are the possible conditions for the symptoms: {user_input}?"

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=200)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Define Gradio Interface
ui = gr.Interface(
    fn=analyze_symptoms,  # Function for AI-powered symptom detection
    inputs=gr.Textbox(label="Enter Your Symptoms"),
    outputs=gr.Textbox(label="AI Diagnosis"),
    title="HealthAI: AI-Powered Disease Diagnosis",
    description="Enter your symptoms and receive AI-generated health insights powered by IBM Granite."
)

# Launch the Gradio App
ui.launch()

