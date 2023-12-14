## PyTorch Workload

### Steps to build Docker Image
```bash
docker build -t <image_name>:<image_tag> .
```

Before running the worklaod we need to make sure kubeflow operators and CRDs are in place, if they are present then use the below command.
```bash
kubectl apply -k "github.com/kubeflow/training-operator/manifests/overlays/standalone?ref=v1.5.0"
```

### Steps to Execute Job
```bash
kubectl create -f job.yaml
```

When the job status is Completed then check the S3/minio console to verify results.