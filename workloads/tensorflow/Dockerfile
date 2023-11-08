FROM python:3.9
WORKDIR /app

# Update the package lists and install Git
RUN apt-get update && apt-get install -y git
RUN git clone -b v1.13.0 https://github.com/tensorflow/models.git && cp ./models/tutorials/image/mnist/convolutional.py /app/script.py && rm -rf ./models
COPY main.py /app/main.py
RUN pip install minio==5.0.0 tensorflow==2.5.0