#!/bin/bash

# Fetch the value of DB_PASSWORD environment variable
DB_PASSWORD="$DB_PASSWORD"

# Create a temporary SQL file with the password replaced
cat setup.sql | sed "s/\${env:DB_PASSWORD}/$DB_PASSWORD/g" > temp_setup.sql

# Execute the modified SQL script
mysql -hlocalhost -uroot -p < temp_setup.sql

# Clean up
rm temp_setup.sql

