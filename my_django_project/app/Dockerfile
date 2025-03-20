# 1. Specify the base image
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file to the container
COPY requirements.txt .

# 4. Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy all project files to the container
COPY . .

# 6. Expose the port for the Django application
EXPOSE 8000

# 7. Specify the command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
