# Setup
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


# Cheatsheets
## kubectl
- https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands
- Forward port
  - `kubectl port-forward service/coin2-kafka-svc 9095:9095`
- Create a namespace
  - `kubectl create ns NAMESPACE`
- Update/replace an existing configMap
  - `kubectl replace -f some-configmap.yaml`


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
