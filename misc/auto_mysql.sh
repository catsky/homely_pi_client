#!/bin/bash
MYSQL_ROOT_PASSWORD=iamglad2passw0rd
MYSQL_DB_NAME=homelypi

echo "Installing mysql-server..."
sudo apt-get update

sudo debconf-set-selections <<< "mysql-server mysql-server/root_password password $MYSQL_ROOT_PASSWORD"
sudo debconf-set-selections <<< "mysql-server mysql-server/root_password_again password $MYSQL_ROOT_PASSWORD"
sudo apt-get -y install mysql-server

echo "run mysql_secure_installation..."
sudo apt-get -y install expect

SECURE_MYSQL=$(expect -c "
 
set timeout 10
spawn mysql_secure_installation
 
expect \"Enter current password for root (enter for none):\"
send \"$MYSQL_ROOT_PASSWORD\r\"
 
expect \"Change the root password?\"
send \"n\r\"
 
expect \"Remove anonymous users?\"
send \"y\r\"
 
expect \"Disallow root login remotely?\"
send \"y\r\"
 
expect \"Remove test database and access to it?\"
send \"y\r\"
 
expect \"Reload privilege tables now?\"
send \"y\r\"
 
expect eof
")
 
echo "$SECURE_MYSQL"

echo "create the database $MYSQL_DB_NAME..."
echo "CREATE DATABASE IF NOT EXISTS $MYSQL_DB_NAME;" | mysql -uroot -p$MYSQL_ROOT_PASSWORD


