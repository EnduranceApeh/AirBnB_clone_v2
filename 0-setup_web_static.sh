#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Helberton school" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -hR ubuntu:ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 http://apehendurance.tech/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart