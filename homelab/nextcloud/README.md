

# Prerequisites
- Tailscale as a native service
- Pi-hole as a native service, configured to listen on port 53 of this Tailscale host
- Custom DNS entries (A record) for the FQDM of this Tailscale host/Nextcloud subdomain
    - `hostname.tailfdc91.ts.net` -> Tailscale IP (`100.XX.XX.XX`)
    - `nextcloud.hostname.tailfdc91.ts.net` -> Tailscale IP (`100.XX.XX.XX`)
- Self-signed certificate for the FQDM of this Tailscale host:
    - Also add certificate(s) if you need to use Nextcloud subdomain
    - https://stackoverflow.com/questions/70820375/unable-to-obtain-acme-certificate-for-domains-trying-to-setup-https-in-virtual

# Run
- Check out [Caddyfile](Caddyfile) and [docker-compose.yml](docker-compose.yml)
- `docker compose -f docker-compose.yml up`
- You may need to edit `/etc/hosts` on a client machine
    - Add `100.XX.XX.XX  nextcloud.hostname.tailfdc91.ts.net`
