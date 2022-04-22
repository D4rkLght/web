sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE USER 'djangouser'@'localhost'"
mysql -uroot -e "SET PASSWORD FOR 'djangouser'@'localhost' = PASSWORD('password')"
mysql -uroot -e "CREATE DATABASE my_database"
mysql -uroot -e "GRANT ALL ON my_database.* TO 'djangouser'@'localhost'"
sudo /home/box/web/ask/manage.py migrate