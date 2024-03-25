#!/bin/sh
/usr/bin/resolvectl dnssec tun0 no
/usr/bin/resolvectl dnsovertls tun0 no
/usr/bin/resolvectl domain tun0 cluster.local some.other.domain
/usr/bin/resolvectl dns tun0 COMPANY_DNS_IP
