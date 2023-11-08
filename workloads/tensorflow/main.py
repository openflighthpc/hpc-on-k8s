from minio import Minio
from datetime import datetime
import os

import subprocess

def run_fastqc(fastq_file):

    command = ["bash", fastq_file]
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    return_code = process.wait()
    output = process.stdout.read().decode("utf-8")
    return return_code, output

def main():
    fastq_file = "/app/script.py"

    return_code, output = run_fastqc(fastq_file)
    file1 = open('/app/output', 'w')
    file1.write(output)
    file1.close()

    minio_client = Minio(
    f"{os.environ.get('MINIO_IP')}:{os.environ.get('MINIO_PORT')}",
    access_key=f"{os.environ.get('MINIO_AKEY')}",
    secret_key=f"{os.environ.get('MINIO_SKEY')}",
    secure=False  # Set to True if using HTTPS
    )

    bucket_name = f"{os.environ.get('BUCKET_NAME')}"
    file_name  = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    file_path = '/app/output'

    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)

    minio_client.fput_object(
        bucket_name,
        file_name,
        file_path
    )
    print(f'File {file_name} uploaded successfully to {bucket_name}')

if __name__ == "__main__":
    main()