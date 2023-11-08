FROM ubuntu:22.04
COPY script.py /app/script.py
COPY sample_data.fastq /app/sample_data.fastq
RUN apt update && apt install -y fastqc python3  python3-pip && pip install minio
