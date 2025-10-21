# 1. Start from an official Python 3.11 "slim" image
FROM python:3.11-slim

# 2. Set the "working directory" inside the container
WORKDIR /app

# 3. Copy your requirements file into the container
COPY requirements.txt .

# 4. Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your project code into the container
COPY . .

# 6. Set the default command to run when the container starts
CMD ["python3", "monitor.py", "--file", "sites.txt"]
