## Hadoop Workload

### Steps to build Docker Image
```bash
docker build -t <image_name>:<image_tag> .
```
### Steps to install Hadoop cluster
```bash
helm helm repo add pfisterer-hadoop https://pfisterer.github.io/apache-hadoop-helm/

helm install hadoop --set persistence.nameNode.storageClass=longhorn --set persistence.dataNode.storageClass=longhorn --set persistence.dataNode.size=10Gi --set persistence.nameNode.size=10Gi   pfisterer-hadoop/hadoop
```


### Steps to Execute Job
```bash
kubectl create -f job.yaml
```

When the job status is Completed then check the S3/minio console to verify results.
