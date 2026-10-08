SHARED  or Virtual HOSTING:

Shared DNS: bts.army [ forward zone ]
# vim /etc/named.conf
Go to end of file and add
  zone "bts.army" IN {
      type master;
      file "for.bts.army";
  }
:wq
# cd /var/named
# vim for.bts.army

$TTL 1D
@ IN SOA master.itiss.com. email@gmail.com. (
                                      e 3 serial
                                      1D 3 refresh
                                      1H 3 retry
                                      1W 3 expire
                                      3H ) 3 minimum
            IN   NS   master.itiss.com.
bts.army.   IN   A    192.168.206.151
www         IN   A    192.168.206.151

:wq

# systemctl restart named
# host -t a bts.army
# host -t a www.bts.army


Step 3 — Managing the Apache Process
# vim /etc/httpd/conf.d/userdir. conf
  UserDir public_html
:wq

#useradd user
#chmod 711 /home/user
#mkdir /home/user/public_html
#chmod 755 /home/user/public_html
#cat > /home/user/public_html/index.html
  <h1>WEB SERVER</h1>
# chown user:user /home/user/public_html -R
# chmod 644 /home/user/public_html/index.html

# mkdir /etc/httpd/sites-available /etc/httpd/sites-enabled

# vim /etc/httpd/conf/httpd. conf
Go to end of file and add
      IncludeOptional sites-enabled/*.conf
:wq

# setenforce 0    # Disable SELinux
# vim /etc/httpd/sites-available/bts.conf
        <VirtualHost *:80>
            ServerName bts.army
            ServerAlias www.bts.army
            DocumentRoot /home/user/public_html
            <Directory /home/user/public_html>
                AllowOverride All
                Require all granted
            </Directory>
            ErrorLog /var/log/httpd/bts_error_log
            CustomLog /var/log/httpd/bts_access_log combined
    </VirtualHost>

:wq

# ln -s /etc/httpd/sites-available/bts.conf /etc/httpd/sites-enabled/bts. conf
      ln : Link
      -s : Symbolic/Soft Link

config test:
# httpd -t

To confirm that we loaded the VirtualHosts:
# httpd -S
# systemctl restart httpd

curl http://itiss.com
curl http://bts.army
