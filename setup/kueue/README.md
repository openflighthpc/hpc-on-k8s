### Installing Kueue

To install a released version of Kueue in your cluster, run the following command:

```bash
VERSION=v0.4.2
kubectl apply --server-side -f https://github.com/kubernetes-sigs/kueue/releases/download/$VERSION/manifests.yaml
```


Once Kueue is installed, you can proceed to configure it. Create resource flavors, a cluster queue, and a local queue for the following namespaces: default, bio, and physics.

Apply the provided YAML file kueue-resources.yaml:

```bash
kubectl apply -f kueue-resources.yaml
```