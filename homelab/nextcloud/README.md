

# Prerequisites
- Tailscale as a native service
- Pi-hole as a native service, configured to listen on port 53 of this Tailscale host
- Caddy as a native/Docker service, see [caddy](../caddy/README.md) for details
- Custom DNS entries (A record) for the FQDN of this Tailscale host/Nextcloud subdomain
    - `hostname.tailfdc91.ts.net` -> Tailscale IP (`100.XX.XX.XX`)
    - `nextcloud.hostname.ts` -> Tailscale IP (`100.XX.XX.XX`)
- Self-signed certificate for the FQDN of this Tailscale host:
    - Also add certificate(s) if you need to use Nextcloud subdomain
    - https://stackoverflow.com/questions/70820375/unable-to-obtain-acme-certificate-for-domains-trying-to-setup-https-in-virtual
    - `openssl req -x509 -newkey rsa:4096 -nodes -keyout key.pem -out cert.pem -sha256 -days 1000 -subj '/CN=nextcloud.hostname.ts'`

# Run
- Check out [Caddyfile](../caddy/Caddyfile) and [docker-compose.yml](docker-compose.yml)
- `docker compose -f docker-compose.yml up`
- You *may* need to edit `/etc/hosts` on a client machine
    - Add `100.XX.XX.XX  nextcloud.hostname.ts`

# Reset
- https://github.com/nextcloud/all-in-one?tab=readme-ov-file#how-to-properly-reset-the-instance
- Steps:
    - `docker compose -f docker-compose.yml down --remove-orphans`
    - `docker container prune`
    - `docker network rm nextcloud-aio`
    - `docker system prune` (if really want to)
    - `docker volume rm $(docker volume ls -qf dangling=true)` (to delete AIO & other services' configs)
    - `sudo rm -rf /home/USERNAME/data/nextcloud` (to delete all data)

# Resources
- https://www.reddit.com/r/Tailscale/comments/104y6nq/docker_tailscale_and_caddy_with_https_a_love_story/
