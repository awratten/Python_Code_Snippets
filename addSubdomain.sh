#!/bin/bash
echo "MUST HAVE FULLY QUALIFIED DOMAIN NAME SETUP:"
echo ""
echo "enter new subdomain - only string before domain.com"
read varsub
echo ""
mkdir /var/www/html/$varsub
echo "Made new Ditectory : /var/www/html/$varsub"
echo ""
echo "Get External IP Address"
IP=$(curl icanhazip.com)

#vardom = python -c 'import socket; print socket.gethostbyaddr("$IP")'
vardom=$(hostname)


sudo echo "$IP $varsub.$vardom" >> /etc/hosts
echo "Added new entry to Hosts file"
echo ""
sudo echo "" >> /etc/apache2/apache2.conf
sudo echo "# Automatically added by script" >> /etc/apache2/apache2.conf
sudo echo "<VirtualHost *:80>" >> /etc/apache2/apache2.conf
sudo echo "     DocumentRoot /var/www/html/$varsub/" >> /etc/apache2/apache2.conf
sudo echo "     ServerName $varsub.$vardom" >> /etc/apache2/apache2.conf
sudo echo "</VirtualHost>" >> /etc/apache2/apache2.conf

echo ""
echo "added new virtual host to apache2.conf"
echo ""

sudo service apache2 restart
echo ""
echo "All done making $varsub.$vardom"
echo ""

echo ""
echo "don't forget to manually add C-Name to your Domain Host panel ::"
echo ""
echo "HOST: $varsub"
echo "VALUE: $vardom"
