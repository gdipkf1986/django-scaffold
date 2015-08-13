#!/usr/bin/env bash
WEB="gmc.garena.com"
#pidfile="/var/www/$WEB/bin/$WEB.pid"
#kill `cat -- $pidfile`
#rm -f $pidfile
sudo kill -9 `ps -ef | grep $WEB | grep -v grep | awk '{print $2}'`
#sudo kill -9 `ps -ef | grep gmc.garena.com | grep -v grep | awk '{print $2}'`