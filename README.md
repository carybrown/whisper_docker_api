Below are the instructions for wrapping OpenAI’s Whisper API in a Docker Instance for use on your Mac with Apple Silicon.  
My need here was to do transcription locally without going out to OpenAI to transcribe video and audio files.



Here, we have wrapped the Whisper model in a RESTful API. Here’s a step-by-step guide:

#1. Install Docker

Make sure you have Docker installed and running on your system.

#2. Pull the Whisper API Docker Image

Use the following command to pull the Whisper API image. If there’s an official image by OpenAI, you can specify it, but here’s an example for a commonly used Whisper API image on GitHub:

docker pull ghcr.io/openai/whisper-api

#3. Run the Whisper API Container

Run the container, exposing a port for the API (e.g., 9000; it could be whatever you need that doesn't conflict with existing containers), which you’ll call from n8n. If the container requires it, you can add environment variables.

docker run -d \
  --name whisper-api \
  -p 9000:9000 \
  ghcr.io/openai/whisper-api

This command:

	•	Names the container whisper-api
	•	Maps your host’s port 9000 to the container’s port 9000 (adjust as needed)
	•	Runs the container in detached mode (-d), so it runs in the background

#4. Verify the API is Running

To ensure the container is running, use:

docker ps

You should see the whisper-api container listed. Now, test the API by sending a request to http://localhost:9000.

#5. Set Up n8n to Use Whisper API

In n8n, create an HTTP request node to interact with the Whisper API. Configure the node to send audio or video files to the whisper-api endpoint. Here’s an example configuration:

	•	Method: POST
	•	URL: http://localhost:9000/transcribe
	•	Headers: Content-Type: multipart/form-data
	•	Body: Upload your audio file in the request body.

Whisper will then process the file, and you’ll receive a transcription as the response, which you can use in your n8n workflows.
