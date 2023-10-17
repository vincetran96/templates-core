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
{PATH_TO_KAFKA_BINARY}/kafka-topics.sh \
    --bootstrap-server localhost:9094 \
    --topic topic0 \
    --create \
    --partitions 3 \
    --replication-factor 2
```

```
{PATH_TO_KAFKA_BINARY}/kafka-topics.sh \
    --bootstrap-server localhost:9094 \
    --list
```

```
{PATH_TO_KAFKA_BINARY}/kafka-topics.sh \
    --bootstrap-server localhost:9094 \
    --topic topic0 \
    --describe
```

## Messages
```
{PATH_TO_KAFKA_BINARY}/kafka-console-producer.sh \
    --bootstrap-server localhost:9094 \
    --topic topic0 \
    --property "parse.key=true" \
    --property "key.separator=:"
```

```
{PATH_TO_KAFKA_BINARY}/kafka-console-consumer.sh \
    --bootstrap-server localhost:9094 \
    --topic topic0 \
    --from-beginning \
    --property "parse.key=true" \
    --property "key.separator=:"
```

## Consumer group
```
{PATH_TO_KAFKA_BINARY}/kafka-console-consumer.sh \
    --bootstrap-server localhost:9094 \
    --topic topic0 \
    --group group0 \
    --from-beginning \
    --property "parse.key=true" \
    --property "key.separator=:"
```

```
{PATH_TO_KAFKA_BINARY}/kafka-console-consumer.sh \
    --bootstrap-server localhost:9094 \
    --topic topic0 \
    --group group0 \
    --reset-offset --to-earliest \
    --execute
```
