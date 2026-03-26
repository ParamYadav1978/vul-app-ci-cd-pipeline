FROM python:3.12-slim

WORKDIR /app

# 🔐 OS security updates
RUN apt-get update && apt-get upgrade -y && apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000
CMD ["python", "app.py"]


