# What is k8s
https://kubernetes.io/docs/concepts/overview/


# Objects in k8s
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
## Labels and selectors
- Label vs name
  - https://stackoverflow.com/questions/60027090/what-is-the-difference-between-label-and-selector-in-kubernetes
  - https://stackoverflow.com/questions/54436623/why-labels-are-mentioned-three-times-in-a-single-deployment
  - https://serverfault.com/questions/1134929/what-is-the-difference-between-metadata-labels-and-spec-template-metadata-lab


# >> Cluster architecture
![alt text](image.png)
https://kubernetes.io/docs/concepts/architecture/
## Controller
https://kubernetes.io/docs/concepts/architecture/controller/


# >> Containers
## Images
Image pull policy: https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy
- IfNotPresent
- Always
- Never
## Container environment
https://kubernetes.io/docs/concepts/containers/container-environment/
- **Services have dedicated IP addresses** and are available to the Container **via DNS**, if DNS addon is enabled.


# >> Workloads
- Workload is an app - it runs inside a pod
- Workload resources:
  - Deployment and ReplicaSet
  - StatefulSet
  - ...
## Pods
https://kubernetes.io/docs/concepts/workloads/pods
- Pods are the smallest deployable units of computing.
- Grouping multiple co-located and co-managed containers in a single Pod is a relatively advanced use case.
- You don't need to run multiple containers to provide replication (for resilience or capacity); if you need multiple replicas, see Workload management.
- Pods natively provide two kinds of **shared resources** for their constituent containers: **networking** and **storage**.
- On Nodes, the kubelet does **not** directly observe or manage any of the details around pod templates and updates; those details are abstracted away.
### Pod templates
https://kubernetes.io/docs/concepts/workloads/pods/#pod-templates
### Resource sharing
#### Pods storage
#### Pods networking
https://kubernetes.io/docs/concepts/workloads/pods/#resource-sharing-and-communication
- Each Pod is assigned a unique IP address for each address family.
- Every container in a Pod shares the network namespace, including the IP address and network ports.
- Inside a Pod, the containers that belong to the Pod can communicate with one another using `localhost`.
- When containers in a Pod communicate with entities *outside* the Pod, they must coordinate how they use the shared network resources (such as ports).
- Containers that want to interact with a container running in a *different* Pod can use **IP networking** to communicate.
### Pods with multiple containers
https://kubernetes.io/docs/concepts/workloads/pods/#how-pods-manage-multiple-containers
### Pod lifecycle
#### Container restart policy
https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy
- The spec of a Pod has a `restartPolicy` field with possible values
  - Always
  - OnFailure
  - Never
### Downward API
https://kubernetes.io/docs/concepts/workloads/pods/downward-api/
- Information available to a container about itself.
## Workload management
https://kubernetes.io/docs/concepts/workloads/controllers/
### Deployment
https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
- You must specify an appropriate selector and Pod template labels in a Deployment (in this case, app: nginx).
- Do not overlap labels or selectors with other controllers (including other Deployments and StatefulSets).
### DaemonSet
https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
- HostPort vs NodePort
  - https://www.reddit.com/r/kubernetes/comments/w757ju/hostport_vs_nodeport/
## Autoscaling workloads
https://kubernetes.io/docs/concepts/workloads/autoscaling/
## Managing workloads
https://kubernetes.io/docs/concepts/workloads/management/


# Services, load balancing and networking
## The K8s network model
https://kubernetes.io/docs/concepts/services-networking/#the-kubernetes-network-model
- Every Pod in a cluster gets its own **unique cluster-wide** IP address.
- This means you do not need to explicitly create links between Pods and you almost never need to deal with mapping container ports to host ports.
- This creates a clean model where **Pods can be treated much like VMs or physical hosts** from the perspectives of port allocation, naming, service discovery, load balancing, application configuration.
- Without any intentional network segmentation/modification
  - Pods can communicate with all other pods on any other node without NAT
  - Agents on a node (e.g. system daemons, kubelet) can communicate with all pods on that node
- Kubernetes IP addresses exist at the Pod scope - containers within a Pod share their network namespaces - including their IP address and MAC address.
  - This means that containers within a Pod can all reach each other's ports on `localhost`.
  - This is called the "IP-per-pod" model.
- The Pod itself is **blind to the existence or non-existence** of host ports.
## K8s and Traefik
- Ports, pods connectivity
  - https://github.com/k3s-io/k3s/issues/1414#issuecomment-1681112614


# Storage


# Configuration
## Configuration best practices
https://kubernetes.io/docs/concepts/configuration/overview/


# Configure pods
## Assign memory resources and limits
https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/


# >> Services
https://kubernetes.io/docs/concepts/services-networking/service/
## Service types
https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types
