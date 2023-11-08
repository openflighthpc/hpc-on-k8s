## PyTorch Workload

### Steps to build Docker Image
```bash
docker build -t <image_name>:<image_tag> .
```

### Steps to Execute Job
```bash
kubectl create -f job.yaml
```

When the job status is Completed then check the S3/minio console to verify results.