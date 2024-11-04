Below are the instructions for wrapping OpenAI’s Whisper API in a Docker Instance for use on your Mac with Apple Silicon.  
My need here was to do transcription locally without going out to OpenAI to transcribe video and audio files.



Here, we have wrapped the Whisper model in a RESTful API. Here’s a step-by-step guide:

#1. Install Docker

Make sure you have Docker installed and running on your system.

#2. Pull the Whisper API Docker Image

Use the following command to pull the Whisper API image. If there’s an official image by OpenAI, you can specify it, but here’s an example for a commonly used Whisper API image on GitHub:

	docker pull ghcr.io/openai/whisper-api

#3. Download the Dockerfile and api.py files from the repository and include in the /whisper-api folder created in the last step.

#4. Run the Whisper API Container

Run the container, exposing a port for the API (e.g., 9000; it could be whatever you need that doesn't conflict with existing containers), which you’ll call from n8n. If the container requires it, you can add environment variables.

	docker run -d \
	  --name whisper-api \
	  -p 9000:9000 \
	  ghcr.io/openai/whisper-api

This command:

• Names the container whisper-api
• Maps your host’s port 9000 to the container’s port 9000 (adjust as needed)
• Runs the container in detached mode (-d), so it runs in the background

#5. Verify the API is Running

To ensure the container is running, use:

	docker ps

You should see the whisper-api container listed. Now, test the API by sending a request to http://localhost:9000.

Test the API with curl.  You can test the API by sending a video or audio file to the /transcribe endpoint:

	curl -X POST -F "file=@/path/to/yourfile.mp4" http://localhost:9000/transcribe


## To access the Whisper transcription API from n8n using an n8n HTTP Request node, you can configure it as follows:

Step 1: Configure the HTTP Request Node in n8n

1. Add an HTTP Request Node to your n8n workflow.
2. Set the Method to POST.
3. Set the URL to your Whisper API endpoint:  http://localhost:9000/transcribe
4. Set the Body Content Type to Form-Data.
5. Add a Form-Data Field for the file you want to transcribe:
	• Parameter Name: file (this should match the field name expected by the API).
	• Type: File.
	• File Field Value: You can use the file path or a reference to a file that has been previously uploaded or exists in n8n.
6. Select the Input File:
	• If the file is stored locally or in n8n’s file storage, you can reference its path here.
	• Alternatively, if the file is part of the workflow, ensure the file has been uploaded or generated in a previous node (e.g., an S3 Download node if coming from a cloud bucket).

Example Configuration

Setting	Value
Method	POST
URL	http://localhost:9000/transcribe
Content Type	Form-Data
Form Data Field Name	file
Form Data Field Type	File
File Field Value	/path/to/yourfile.mp4

Step 2: Run the Workflow

Run the workflow to trigger the HTTP Request node. If everything is set up correctly, the Whisper API should receive the video file, extract the audio, process the transcription, and return the result as JSON.

Step 3: Access the Transcription Result

	•	The transcription result should appear as the response from the HTTP Request node.
	•	Use further nodes in your workflow to parse or store the transcription result as needed.


## Mermaid Diagram
	graph TD
	    A[Start] --> B[Install Docker]
	    B --> C[Pull Whisper API Docker Image]
	    C --> D[Run Whisper API Container]
	    D --> E[Verify the API is Running]
	    E --> F[Set Up n8n HTTP Request Node]
	    F --> G[Send Audio/Video Files to Transcribe]
	    G --> H[Receive Transcription Response]
	    H --> I[End]


<img width="213" alt="image" src="https://github.com/user-attachments/assets/b4c42717-1842-4c1c-92b8-4efc42db3da6">
