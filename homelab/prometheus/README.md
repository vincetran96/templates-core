# Guides
- https://www.confluent.io/blog/monitor-kafka-clusters-with-prometheus-grafana-and-confluent/
- https://medium.com/@oredata-engineering/setting-up-prometheus-grafana-for-kafka-on-docker-8a692a45966c


# Make services export data
## Allow Prometheus on Docker to access exported data (assuming usage of UFW)
Create custom UFW configs in `/etc/ufw/applications.d` (see [this](../_computer_hierarchy/etc/ufw/applications.d))
## Service examples
### Kafka
**Kafka brokers**
- https://github.com/prometheus/jmx_exporter/blob/release-1.0.1/example_configs/kafka-2_0_0.yml
- https://gist.githubusercontent.com/baturalpk/fb2e394e2d133d107477bb198ab0a92c/raw/a7917c6f633666ee84e1588d663fde48d6dec640/kafka-broker.yml
- https://github.com/confluentinc/jmx-monitoring-stacks/blob/6.1.0-post/shared-assets/jmx-exporter/kafka_broker.yml


# Prepare Prometheus and Grafana config files
- [prometheus.yml](prometheus/prometheus.yml)
- [prometheus-ds.yml](grafana/provisioning/datasources/prometheus-ds.yml)


# Docker Compose file
- [docker-compose.yaml](docker-compose.yaml)


# JMX jar execution file
- https://repo.maven.apache.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.20.0/jmx_prometheus_javaagent-0.20.0.jar
- Put it in an appropriate folder (e.g., Kafka)


# After things are up
Check datasources status: http://TAILSCALE_IP:9090/targets
