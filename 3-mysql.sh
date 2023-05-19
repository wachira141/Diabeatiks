#!/bin/bash

#install mysql and configure

if [ -f /etc/init.d/mysql* ]; then
    echo "installed"
else
    echo "installing mysql on this server ------>"
    yum localinstall -y https://dev.mysql.com/get/mysql8.0-community-release-el7-3.noarch.rpm
    yum install -y mysql-community-server-*

    #start mysql server
    echo "starting mysql server"
    sudo systemctl start mysql.service 2>/dev/null
    systemctl enable mysql.service 2>/dev/null

    #change mysql default root password
    DB_PASSWORD=kenya
    TEMPROOTPASS="`sudo grep 'temporary.* root@localhost' /var/log/mysqld.log | tail -n 1 | sed 's/.*root@localhost://'`"
    mysql -u "root" --password="TEMPROOTPASS" --connect-expired-password -e "ALTER USER 'root'@'localhost' IDENTIFIED BY '${DB_PASSWORD}';"
    FLUSH PRIVELEGES

    #simple hardening
    mysql -u root -p="$DB_PASSWORD" -e "DELETE FROM mysql.user WHERE USER='';
    DROP DATABASE IF EXISTS test; DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%;'
    FLUSH PRIVELEGES;"


    mysql -u root -p="$DB_PASSWORD" -e "CREATE DATABASE IF EXISTS 'diabetics_dev_db';
    USE 'diabetics_dev_db';
    CREATE USER IF NOT EXISTS 'diabetics_dev'@'localhost' IDENTIFIED BY 'diabetics_dev_pwd';
    GRANT ALL PRIVILEGES ON `diabetics_dev_db`. * TO 'diabetics_dev'@'localhost';
    GRANT SELECT ON `performance_schema`. * TO 'diabetics_dev'@'localhost';
    FLUSH PRIVILEGES;"

fi