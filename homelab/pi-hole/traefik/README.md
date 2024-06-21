Use Pi-hole with Traefik
```bash
kubectl apply \
    -f pi-hole/k8s/traefik/pi-hole.yaml \
    -f pi-hole/k8s/traefik/pi-hole-ingress.yaml \
    -f pi-hole/k8s/pi-hole-pvc.yaml
```
