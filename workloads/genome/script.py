import os
from minio import Minio
from minio.error import S3Error
from datetime import datetime
import subprocess

def run_fastqc(fastq_file):
    command = ["fastqc", fastq_file]
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    return_code = process.wait()
    output = process.stdout.read().decode("utf-8")
    return return_code, output

def main():
    
    fastq_file = "/app/sample_data.fastq"

    return_code, output = run_fastqc(fastq_file)

    if return_code != 0:
        raise Exception("FastQC failed with return code {}".format(return_code))

    with open("fastqc_output.html", "w") as f:
        f.write(output)

    minio_client = Minio(
    f"{os.environ.get('MINIO_IP')}:{os.environ.get('MINIO_PORT')}",
    access_key=f"{os.environ.get('MINIO_AKEY')}",
    secret_key=f"{os.environ.get('MINIO_SKEY')}",
    secure=False  # Set to True if using HTTPS
    )

    # Define the bucket and object name
    bucket_name = f"{os.environ.get('BUCKET_NAME')}"
    file_name  = datetime.now().strftime("%Y-%m-%d-%H-%M-%S.html")
    # Path to the file you want to upload
    file_path = '/app/sample_data_fastqc.html'

    # Upload the file
    try:
        # Ensure the bucket exists, if not, create it
        if not minio_client.bucket_exists(bucket_name):
            minio_client.make_bucket(bucket_name)

        # Upload the file
        minio_client.fput_object(
            bucket_name,
            file_name,
            file_path
        )
        print(f'File {file_name} uploaded successfully to {bucket_name}')
    except S3Error as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main()