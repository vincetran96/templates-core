# Setup
## Server
Token: https://docs.k3s.io/cli/token#server

# Configuration file
`/etc/rancher/k3s/config.yaml`

Example for server:
```
write-kubeconfig-mode: "0644"
tls-san:
  - "foo.local"
node-label:
  - "foo=bar"
  - "something=amazing"
cluster-init: true
```
