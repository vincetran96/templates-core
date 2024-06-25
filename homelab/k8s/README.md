# Setup
## Prerequisites
Create a file named `/etc/ufw/applications.d/k3s` with the following content (see [this section](../_computer_hierarchy/etc/ufw/applications.d/))
```conf
[K3s]
title=K3s ports
description=Required by K3s: https://docs.k3s.io/installation/requirements#networking
ports=2379:2380/tcp|6443/tcp|8472/udp|10250/tcp|51820/udp|51821/udp|5001/tcp
```
## Server/Master
About token: https://docs.k3s.io/cli/token#server
### Install (with K3s)
```bash
export TAILSCALE_IP=XX.XX.XX.XX
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="server --write-kubeconfig $HOME/.kube/config --write-kubeconfig-mode 644 --flannel-iface tailscale0 --node-ip $TAILSCALE_IP --node-external-ip $TAILSCALE_IP" K3S_TOKEN=12345 sh -
```
### Get token
`cat /var/lib/rancher/k3s/server/node-token`
## Agent/Worker
### Install
```bash
export TAILSCALE_SERVER_IP=XX.XX.XX.XX
export TAILSCALE_IP=YY.YY.YY.YY
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="agent --server https://$TAILSCALE_SERVER_IP:6443 --token K10c3d7187aa06c30407582f2582c579ea69f47903833a575f3bb00f04077c2dce4::server:12345 --flannel-iface tailscale0 --node-ip $TAILSCALE_IP --node-external-ip $TAILSCALE_IP" sh -s -
```
## Packaged components
- https://docs.k3s.io/installation/packaged-components
- Location: `/var/lib/rancher/k3s/server/manifests`

# Configuration file
`/etc/rancher/k3s/config.yaml`

Example for server:
```yaml
write-kubeconfig-mode: "0644"
tls-san:
  - "foo.local"
node-label:
  - "foo=bar"
  - "something=amazing"
cluster-init: true
```

# Systemd configuration file
To change things when setting up K3s
## Server
`cat /etc/systemd/system/k3s.service`
## Agent
`cat /etc/systemd/system/k3s-agent.service`
## Apply changes to such configuration files
```bash
sudo systemctl daemon-reload
sudo systemctl restart <k3s on master node or k3s-agent on worker node>
```

# Use k3s with Tailscale
- https://weberc2.github.io/posts/k3s-tailscale.html
- https://stackoverflow.com/questions/66449289/is-there-any-way-to-bind-k3s-flannel-to-another-interface


# Traefik
## Install with Helm
```bash
helm install --namespace=traefik-system --values=$HOME/.kube/traefik/traefik-values.yaml traefik traefik/traefik
```
## Apply custom resources
At this point, I'm not sure which one runs first
```bash
kubectl -n default apply -f $HOME/.kube/traefik/traefik-crd-resource.yaml
kubectl -n traefik-system apply -f $HOME/.kube/traefik/traefik-crd-definition-v1.yaml
```
Source:
- https://github.com/traefik/traefik/blob/v3.0/docs/content/reference/dynamic-configuration/kubernetes-crd-definition-v1.yml
- https://github.com/traefik/traefik/blob/v3.0/docs/content/reference/dynamic-configuration/kubernetes-crd-resource.yml
## Update values file and restart
In case the values file is changed, etc.
```bash
helm upgrade --install --namespace=traefik-system --values=$HOME/.kube/traefik/traefik-values.yaml traefik traefik/traefik
```
## Values file
- https://github.com/traefik/traefik-helm-chart/blob/master/traefik/values.yaml
## Dashboard
### Visit dashboard
- Go to `TAILSCALE_IP:9000/dashboard/#/`
### Expose dashboard
- `kubectl -n traefik-system port-forward deployments/traefik 9000:9000`
- Or `kubectl apply -f $HOME/.kube/traefik/traefik-dashboard.yaml`
## Uninstall
```bash
helm uninstall -n traefik-system traefik traefik/traefik
```


# Cheatsheets
## kubectl
- https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands
- Forward port
  - `kubectl port-forward service/coin2-kafka-svc 9095:9095`
- Create a namespace
  - `kubectl create ns NAMESPACE`
- Update/replace an existing configMap
  - `kubectl replace -f some-configmap.yaml`
- Restart pods
  - `kubectl rollout restart deployment DEPLOYMENT -n NAMESPACE`
- Get volumes
  - `kubectl get pv`


# Tricks
- Expose traefik dashboard:
  - https://stackoverflow.com/questions/68565048/how-to-expose-traefik-v2-dashboard-in-k3d-k3s-via-configuration/70895373#70895373
- Docker Compose to Kubernetes
  - https://github.com/kubernetes/kompose?tab=readme-ov-file
- port vs targetPort
  - https://stackoverflow.com/questions/49981601/difference-between-targetport-and-port-in-kubernetes-service-definition
- Expose low-number ports to host
  - https://stackoverflow.com/questions/61787577/how-to-expose-low-numbered-ports-in-the-kubernetes-mini-cluster-that-comes-with/61795178#61795178
- Environment variables and configMap and Secret
  - https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#configure-all-key-value-pairs-in-a-configmap-as-container-environment-variables
  - https://gist.github.com/troyharvey/4506472732157221e04c6b15e3b3f094
- Convert local docker image to containerd image
  - https://stackoverflow.com/questions/69981852/how-to-use-local-docker-images-in-kubernetes-deployments-not-minikube
  - https://github.com/k3s-io/k3s/issues/213
- Connect from Pod to host
  - https://stackoverflow.com/questions/66290862/kubernetes-pod-talking-to-a-localhost-port
  - https://github.com/kubernetes-sigs/kind/issues/1200#issuecomment-1304855791
- Keep a container running
  - https://stackoverflow.com/questions/31870222/how-can-i-keep-a-container-running-on-kubernetes
## Traefik
- Dynamic configuration custom resource
  - https://doc.traefik.io/traefik/reference/dynamic-configuration/kubernetes-crd/#definitions
## Metallb
- IP address sharing
  - https://metallb.universe.tf/usage/#ip-address-sharing
