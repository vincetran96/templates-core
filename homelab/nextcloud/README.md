

# Prerequisites
- Tailscale as a native service
- Pi-hole as a native service, configured to listen on port 53 of this Tailscale host
- Custom DNS entries (A record) for the FQDM of this Tailscale host/Nextcloud subdomain
    - `hostname.tailfdc91.ts.net` -> Tailscale IP (`100.XX.XX.XX`)
    - `nextcloud.hostname.ts` -> Tailscale IP (`100.XX.XX.XX`)
- Self-signed certificate for the FQDM of this Tailscale host:
    - Also add certificate(s) if you need to use Nextcloud subdomain
    - https://stackoverflow.com/questions/70820375/unable-to-obtain-acme-certificate-for-domains-trying-to-setup-https-in-virtual
    - `openssl req -x509 -newkey rsa:4096 -nodes -keyout key.pem -out cert.pem -sha256 -days 1000 -subj '/CN=local.example.com'`

# Run
- Check out [Caddyfile](Caddyfile) and [docker-compose.yml](docker-compose.yml)
- `docker compose -f docker-compose.yml up`
- You may need to edit `/etc/hosts` on a client machine
    - Add `100.XX.XX.XX  nextcloud.hostname.ts`

# Reset
- https://github.com/nextcloud/all-in-one?tab=readme-ov-file#how-to-properly-reset-the-instance
- Steps:
    - `docker compose -f docker-compose.yml down --remove-orphans`
    - `docker container prune`
    - `docker network rm nextcloud-aio`
    - `docker system prune` (if really want to)
    - `docker volume rm $(docker volume ls -qf dangling=true)`
    - `sudo rm -rf /home/USERNAME/data/nextcloud`
    - `sudo rm -rf /home/USERNAME/nextcloud/certs/nextcloud/*`
