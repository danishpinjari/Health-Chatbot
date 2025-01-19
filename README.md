# Mindfulness Chatbot API

This project is a FastAPI-based chatbot that integrates with the Groq API to provide conversational responses. It includes emotion detection, mindfulness exercise recommendations, and resource suggestions based on the user's input.

## Features

- **Chatbot Functionality**: Uses the Groq API to generate conversational responses.
- **Emotion Detection**: Placeholder function to detect user emotion from their messages.
- **Mindfulness Recommendations**: Provides mindfulness exercises and resources based on detected emotions.
- **Static File Serving**: Serves CSS and JS files from the `static/` directory.
- **HTML Template Rendering**: Serves an HTML file from the `templates/` directory as the root page.

## Project Structure

```
.
├── app
│   └── main.py            # Main FastAPI application
├── static
│   ├── css                # CSS files
│   └── js                 # JavaScript files
├── templates
│   └── health.html        # HTML template file
├── requirements.txt       # Python dependencies
└── Dockerfile             # Dockerfile for containerization
```

## Requirements

- Python 3.9 or higher
- FastAPI
- Pydantic
- Uvicorn
- Requests

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/mindfulness-chatbot.git
   cd mindfulness-chatbot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI application**:
   ```bash
   uvicorn app.main:app --reload
   ```

   The application will be accessible at `http://127.0.0.1:8000`.

4. **Set up the Groq API key**:
   - Create an environment variable `GROQ_API_KEY` and set your Groq API key.
   ```bash
   export GROQ_API_KEY=your_groq_api_key
   ```

## API Endpoints

- **`POST /chat`**: Handles user messages and returns chatbot responses along with mindfulness exercises and resource recommendations.

  Example request:
  ```json
  {
    "message": "I'm feeling a bit anxious today."
  }
  ```

  Example response:
  ```json
  {
    "response": "Chatbot response...\n\nMindfulness Exercise: How about a 5-minute guided meditation?\nResource Recommendation: Watch this calming video: [link]"
  }
  ```

- **`GET /`**: Serves the root HTML page (`health.html`).

## Running with Docker

1. **Build the Docker image**:
   ```bash
   docker build -t mindfulness-chatbot .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -p 80:80 -e GROQ_API_KEY=your_groq_api_key mindfulness-chatbot
   ```

   The application will be accessible at `http://127.0.0.1`.

## Deployment

To deploy the application to Google Cloud Platform (GCP), you can use Google Cloud Run or Google Kubernetes Engine (GKE). Ensure that the `GROQ_API_KEY` environment variable is set in the cloud environment.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Groq API](https://www.groq.com/)
```

### Instructions
- Update the placeholder values such as `yourusername` in the repository URL and `your_groq_api_key` with actual values.
- Replace `[link]` with actual resource links in the mindfulness recommendations.
- Add a `LICENSE` file if you choose to include a specific license for the project.