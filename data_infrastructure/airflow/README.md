# Commands
## Build:
`make docker-build tag=my-airflow:test df=Dockerfile`

## Compose up:
`make docker-up cf=docker-compose.yml env=.env`

## Build and up:
`make docker_buildup tag=my-airflow:test df=Dockerfile cf=docker-compose.yml env=.env`

## Compose down:
`make docker-down cf=docker-compose.yml`

Notes:
- This Docker's configurations create a network called `my-network`, with the `NETWORK_NAME` defined the in the `.env` file
- The Postgres host name is the `PG_HOST` defined in the `.env` file

Extra notes:
- Services (compose other than the Airflow one) can be connected with the Airflow compose by having these lines in the compose file (this is Mac's version):
    ```
    extra_hosts:
        - "docker.for.mac.host.internal:host-gateway"
    ```
