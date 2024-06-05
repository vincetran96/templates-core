# Setup
- See [docker-compose.yml](docker-compose.yml)
- `docker compose -f docker-compose.yml up -d`

# Caddyfile
## Example
A Caddyfile that handles Nextcloud and Pi-hole admin servers may look like this (see [Caddyfile](Caddyfile)):
```
nextcloud.hostname.ts {
	tls /certs/cert.nextcloud.pem /certs/nextcloud/key.nextcloud.pem
	reverse_proxy 127.0.0.1:11000
}

pihole.hostname.ts {
	tls /certs/cert.pihole.pem /certs/key.pihole.pem
	rewrite * /admin{uri}
	reverse_proxy 127.0.0.1:60080
}
```
## Reload Caddyfile
`docker compose exec -w /etc/caddy caddy caddy reload`


# Resources
- https://caddy.community/t/reverse-proxy-into-docker-container-sub-path/9232/2
