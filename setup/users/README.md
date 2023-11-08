## Steps to create bio-user in bio namespace

1. Apply the YAML file for `bio-user`:

   ```bash
   kubectl apply -f bio-user.yaml


### Add configuration to `~/.kube/config`

```bash
kubectl config set-credentials bio-user --token=$(kubectl get secret -n bio $(kubectl get sa bio-user -n bio -o jsonpath='{.secrets[0].name}') -o jsonpath='{.data.token}' | base64 --decode)
kubectl config set-context bio-context --cluster=$(kubectl config view -o jsonpath='{.clusters[0].name}') --namespace=bio --user=bio-user


### Switch to bio-context

```bash
kubectl config use-context bio-context


## Steps to create physics-user in bio namespace

1. Apply the YAML file for `physics-user`:

   ```bash
   kubectl apply -f physics-user.yaml

### Add configuration to `~/.kube/config`

```bash
kubectl config set-credentials physics-user --token=$(kubectl get secret -n physics $(kubectl get sa physics-user -n physics -o jsonpath='{.secrets[0].name}') -o jsonpath='{.data.token}' | base64 --decode)
kubectl config set-context physics-context --cluster=$(kubectl config view -o jsonpath='{.clusters[0].name}') --namespace=physics --user=physics-user

### Switch to physics-context

```bash
kubectl config use-context physics-context

### Switch back to admin context

```bash
kubectl config use-context local
