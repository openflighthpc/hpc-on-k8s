FROM bitnami/pytorch:2.1.0
USER root
RUN pip install tensorboardX==1.6.0 protobuf==3.17.0 minio
RUN mkdir -p /opt/mnist
WORKDIR /opt/mnist/src
RUN chmod -R g+rwX /opt/mnist
ADD mnist.py /opt/mnist/src/mnist.py
ADD main.py /opt/mnist/src/main.py
