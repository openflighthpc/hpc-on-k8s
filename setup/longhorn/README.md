# Installing Longhorn Inside Kubernetes Cluster

To install Longhorn inside your Kubernetes cluster, follow these steps:

1. Create a directory for Longhorn installation, copy the content from longhorn.yaml file and apply the files.

```bash
mkdir ~/rke/build
cd ~/rke/build
vi longhorn.yaml
kubectl apply -f longhorn.yaml
```