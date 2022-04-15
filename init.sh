sudo ln -sf /home/box/web/etc/nginx.conf  
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/hello.py   
sudo /etc/init.d/gunicorn restart
