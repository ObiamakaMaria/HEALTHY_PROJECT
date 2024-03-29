# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define Nginx configuration file for your Flask app
file { '/etc/nginx/sites-available/my_flask_app.conf':
  ensure  => present,
  content => @(EOF)
server {
    listen 80;  # Nginx default port
    server_name 54.89.116.235;  # Your public IP address

    location / {
        proxy_pass http://127.0.0.1:5000;  # Proxy to port 5000
        include /etc/nginx/proxy_params;
        proxy_redirect off;
    }
}
EOF
}

# Create a symbolic link to enable the configuration
file { '/etc/nginx/sites-enabled/my_flask_app.conf':
  ensure => link,
  target => '/etc/nginx/sites-available/my_flask_app.conf',
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => running,
  enable => true,
  require => File['/etc/nginx/sites-enabled/my_flask_app.conf'],
}

