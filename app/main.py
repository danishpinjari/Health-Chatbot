from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import requests
import json
import os

# Set up the Groq API key and endpoint
groq_api_key = os.getenv("GROQ_API_KEY", "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")  # Use environment variable for security
endpoint = "https://api.groq.com/openai/v1/chat/completions"  # Groq API endpoint

# FastAPI instance
app = FastAPI()

# Mount static files for serving CSS, JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Conversation history for the session
conversation_history = []

# Pydantic model for user input
class UserMessage(BaseModel):
    message: str

# Function to generate a response from the Groq API
def generate_response(user_input: str):
    global conversation_history
    conversation_history.append({"role": "user", "content": user_input})

    # Prepare the data with the conversation history for the model
    data = {
        "model": "llama-3.3-70b-versatile",  # Replace with the model you are using
        "messages": conversation_history
    }
    
    try:
        # Make a request to the Groq API with the conversation history
        response = requests.post(endpoint, headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {groq_api_key}"
        }, json=data)
        response.raise_for_status()  # Raise an exception for bad responses
        response_json = response.json()

        # Extract the chatbot's response and add it to the conversation history
        if 'choices' in response_json:
            chatbot_response = response_json['choices'][0]['message']['content']
            conversation_history.append({"role": "assistant", "content": chatbot_response})
            return chatbot_response
        else:
            return "Sorry, I didn't understand that."
    except requests.exceptions.RequestException as err:
        return f"Error: {err}"

# Function for emotion detection (placeholder, replace with actual implementation)
def detect_emotion(user_input: str):
    # Replace this with actual emotion detection logic, e.g., using an external API or a model
    # For now, returning a mock emotion
    return "calm"

# Function to recommend mindfulness exercises based on emotion
def recommend_mindfulness_exercise(emotion: str):
    # Example recommendations based on emotion
    exercises = {
        "calm": "Try a deep breathing exercise.",
        "anxious": "How about a 5-minute guided meditation?",
        "sad": "Consider journaling your thoughts."
    }
    return exercises.get(emotion, "Take a moment to relax.")

# Function to suggest resources
def recommend_resources(emotion: str):
    # Example resources based on emotion
    resources = {
        "calm": "Here's an article on maintaining mindfulness: [link]",
        "anxious": "Watch this calming video: [link]",
        "sad": "Read this guide on coping with sadness: [link]"
    }
    return resources.get(emotion, "Here are some general well-being tips: [link]")

# API endpoint to handle chat messages
@app.post("/chat")
async def chat(user_message: UserMessage):
    user_input = user_message.message
    emotion = detect_emotion(user_input)  # Detect the user's emotion
    chatbot_response = generate_response(user_input)  # Generate chatbot's response

    # Add mindfulness exercise and resource recommendation
    mindfulness_exercise = recommend_mindfulness_exercise(emotion)
    resource_recommendation = recommend_resources(emotion)

    # Combine the chatbot response with additional features
    combined_response = (
        f"{chatbot_response}\n\n"
        f"Mindfulness Exercise: {mindfulness_exercise}\n"
        f"Resource Recommendation: {resource_recommendation}"
    )

    return {"response": combined_response}

# Root endpoint to serve the HTML file
@app.get("/", response_class=HTMLResponse)
async def root():
    with open("templates/health.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

