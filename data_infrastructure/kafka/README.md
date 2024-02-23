# Download necessary binaries
- Download Java JRE
- Download Kafka binary from: https://kafka.apache.org/downloads
- After extracting, you can add the binary path into `$PATH` in your `~/.bashrc`:
    ```
    export PATH="/home/user_name/kafka_2.13-3.6.0/bin:$PATH"
    ```

# Commands
## Topics
```
kafka-topics.sh \
    --bootstrap-server localhost:9094 \
    --topic topic0 \
    --create \
    --partitions 3 \
    --replication-factor 2
```

```
kafka-topics.sh \
    --bootstrap-server localhost:9094 \
    --list
```

```
kafka-topics.sh \
    --bootstrap-server localhost:9094 \
    --topic topic0 \
    --describe
```

## Messages
```
kafka-console-producer.sh \
    --bootstrap-server localhost:9094 \
    --topic topic0 \
    --property "parse.key=true" \
    --property "key.separator=:"
```

```
kafka-console-consumer.sh \
    --bootstrap-server localhost:9094 \
    --topic topic0 \
    --from-beginning \
    --property "parse.key=true" \
    --property "key.separator=:"
```

```
kafka-console-consumer.sh \
    --bootstrap-server localhost:9094 \
    --consumer.config config/config.example.properties \
    --topic shopping-ads-log \
    --from-beginning
```

## Consumer group
**Create consumer group**
```
kafka-console-consumer.sh \
    --bootstrap-server localhost:9094 \
    --topic topic0 \
    --group group0 \
    --from-beginning \
    --property "parse.key=true" \
    --property "key.separator=:"
```

**Reset offsets**
```
kafka-consumer-groups.sh \
    --bootstrap-server localhost:9094 \
    --topic topic0 \
    --group group0 \
    --reset-offsets --to-earliest \
    --execute
```

**Describe offsets, etc. of consumer groups**
```
kafka-consumer-groups.sh \
    --bootstrap-server localhost:9094 \
    --describe \
    --all-groups
```
