FROM python:3.11-slim

# Install tkinter dependencies
RUN apt-get update && \
    apt-get install -y python3-tk tk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy your project files into the container
COPY . .

# Run the Snake Game
CMD ["python", "main.py"]
