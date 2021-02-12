FROM alpine:edge
WORKDIR /app
RUN apk update
RUN apk add build-base python3 py3-pip python3-dev
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["python3", "/app/Code/GT.py"]
