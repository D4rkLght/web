sudo ln -sf /home/box/web/etc/nginx.conf  
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/hello.py   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
