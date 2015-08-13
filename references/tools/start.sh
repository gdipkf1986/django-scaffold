#!/bin/bash
WEB="gmc.garena.com"
python /var/www/${WEB}/htdocs/manage.py runfcgi host=127.0.0.1 method=prefork minchildren=8 maxchildren=64 port=8981 pidfile=/var/www/$WEB/bin/${WEB}.pid
