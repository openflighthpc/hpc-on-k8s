FROM apache/hadoop:3
WORKDIR /opt
ADD hdfiles.zip /opt/hdfiles.zip
ADD script.sh /opt/script.sh
ADD main.py /opt/main.py
RUN sudo yum update -y && sudo yum install -y java-1.8.0-openjdk.x86_64 java-1.8.0-openjdk-devel.x86_64 unzip python36 python36-devel python36-setuptools 
RUN sudo pip3 install minio==5.0.0
