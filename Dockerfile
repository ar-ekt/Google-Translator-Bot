FROM python:3.8.0-alpine
WORKDIR /app
RUN apk update
RUN apk add build-base python3 py3-pip \
    python3-dev gcc libressl-dev musl-dev \
    libffi-dev
COPY . .
RUN mv /app/Code/* /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "GT.py"]
