# Setup
- Custom DNS entries (A record) for the FQDN of this Tailscale host/Nextcloud/etc. subdomain
    - `hostname.tailfdc91.ts.net` -> Tailscale IP (`100.XX.XX.XX`)
    - `nextcloud.hostname.ts` -> Tailscale IP (`100.XX.XX.XX`)
- Self-signed certificate for the FQDN of this Tailscale host:
    - Also add certificate(s) if you need to use Nextcloud subdomain
    - https://stackoverflow.com/questions/70820375/unable-to-obtain-acme-certificate-for-domains-trying-to-setup-https-in-virtual
    - `openssl req -x509 -newkey rsa:4096 -nodes -keyout key.pem -out cert.pem -sha256 -days 1000 -subj '/CN=nextcloud.hostname.ts'`
- A Caddyfile, see Caddyfile section
- See [docker-compose.yml](docker-compose.yml), `docker compose -f docker-compose.yml up -d`

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
