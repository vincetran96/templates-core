Build:
`make setup_docker tag=my-airflow:test df=Dockerfile`

Compose up:
`make docker_up cf=docker-compose.yml`

Build and up:
`make docker_buildup tag=my-airflow:test df=Dockerfile cf=docker-compose.yml`
