# 1. Start with an official Python image
FROM python:3.10-slim
# 2. Set the working directory inside the container
WORKDIR /app
# 3. Copy your requirements file
COPY requirements.txt .
# 4. Install your Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
# 5. Copy your application code into the container
COPY app.py .
# 6. This is the command that will run when the container starts
CMD [ "python", "app.py" ]