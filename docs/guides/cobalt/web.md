---
title: "cobalt/Host Web"
description: "How to setup your own cobalt web."
---
!!! danger "Warning"
    This guide uses an unofficial Docker image for hosting web. It pulls cobalt's official source. You can see the Docker image source [here](https://github.com/spotdemo4/cobalt-web-docker).

    This guide is not official. Use at your own risk.

This guide showcases how to setup your own cobalt web instance. cobalt web is the site itself where you input media.

!!! info "Information"
    This guide is not required to host your own cobalt API. cobalt lets you add your API to web directly. You should use [cobalt.tools](https://cobalt.tools) and add a custom processing instance. Only do this if you really want to.

## Requirements
* You need Docker. You can install it [here](https://docs.docker.com/engine/install/).
* Webserver, something like Caddy or NGINX.
* A domain or subdomain for cobalt web, pointed at your server.


## Setup Container
Add this container to your current `compose.yml`. If you don't have one, then simply make one.
```yaml
cobalt-web:
    image: ghcr.io/spotdemo4/cobalt-web:latest
    container_name: cobalt_web
    restart: unless-stopped
    environment:
      WEB_DEFAULT_API=https://api.cobalt.tools/
      WEB_HOST=cobalt.tools
      ENABLE_DEPRECATED_YOUTUBE_HLS=true
      WEB_PLAUSIBLE_HOST=plausible.io
      PORT=9002
      LOG_LEVEL=info
    ports:
      - 127.0.0.1:9002:9002
```

You'll need to edit some of the environment variables. Here are the ones to change:

* `WEB_DEFAULT_API` - set this to the default cobalt API your web will use.
* `WEB_HOST` - set this to your domain/subdomain cobalt web will use.
* `ENABLE_DEPRECATED_YOUTUBE_HLS` - set this to true/false if you want the deprecated YouTube HLS option.
* `WEB_PLAUSIBLE_HOST` - the host of your own Plausible instance for web analytics. If you don't have or want this, just remove it.
* `LOG_LEVEL` - `error`, `warn`, `info`, `debug`, `trace`. You can leave as `info`.

## Setup Reverse Proxy
!!! info "Information"
    If you have Cloudflare Turnstile setup, make sure you add your cobalt web domain to the domain list!


You'll need to setup a reverse proxy to proxy your domain to point to cobalt web. This can be done with different webservers, but you want to point it to `http://localhost:9002`.

These are examples, so seek out what webserver software you are using.

```caddy title="Caddy"
cobalt-web.example.com {
    reverse_proxy localhost:9002
}
```

```caddy title="NGINX"
# HTTP, redirected to HTTP
server {
    listen 80;
    server_name cobalt-web.example.com;

    return 301 https://$host$request_uri;
}

# HTTPS
server {
    listen 443 ssl;
    server_name cobalt-web.example.com;

    ssl_certificate /etc/letsencrypt/live/cobalt-web.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/cobalt-web.example.com/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:9002;
    }
}
```