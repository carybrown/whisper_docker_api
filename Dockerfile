# Use a Python base image
FROM python:3.9-slim-bullseye

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Set working directory
WORKDIR /app

# Copy the Whisper code
COPY . /app

# Install Whisper and dependencies
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install -r requirements.txt
RUN pip install flask

# Expose the port
EXPOSE 9000

# Copy and add an API server script (below)
COPY api.py /app/api.py

# Run the API server
CMD ["python", "api.py"]
