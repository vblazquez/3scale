FROM ubuntu

# Install Nginx, php5-fpm
RUN \
  apt-get update && \
  apt-get install -y nginx && \
  mkdir -p /var/www && \
  mkdir -p /etc/nginx && \
  mkdir -p /var/lib/nginx/cache/datacenters && \
  mkdir -p /var/lib/nginx/cache/servers && \
  chown www-data /var/lib/nginx/cache/datacenters && \
  chown www-data /var/lib/nginx/cache/servers && \
  chmod 700 /var/lib/nginx/cache/datacenters /var/lib/nginx/cache/servers && \
  echo "daemon off;" >> /etc/nginx/nginx.conf

ADD nginx/default /etc/nginx/sites-available/default
ADD nginx/htpasswd /etc/nginx/htpasswd

# Expose ports.
EXPOSE 80

# Define default command.
CMD ["nginx"]

