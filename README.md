# ShopBat lets you compare the price of the product from various websites in a real time.

Steps to be done-->(On linux OS)
1. Load the extension in chrome, <a href = "https://www.cnet.com/how-to/how-to-install-chrome-extensions-manually/" > click here </a>
2. First Setup a server.(Xampp Server)
3. In file /opt/lampp/etc/httpd.conf,Change DocumentRoot and Directory path in /opt/lampp/etchttpd.conf  from  DocumentRoot "/opt/lampp/htdocs" and Directory "/opt/lampp/htdocs"
                        to 
    DocumentRoot "/home/user/Downloads/ShopBat" and Directory "/home/user/Downloads/ShopBat"
   (or where it has been downloaded).

Just in case step 3 still does not, <a href = "https://askubuntu.com/questions/64095/change-xampps-htdocs-web-root-folder-to-another-one" > click here </a>

4. Start the server, by following commands
    $ sudo /opt/lampp/lampp start
5. Enter localhost in browser, then click on Final Server, then on search.php.
6. Run the python script named price.py in background.
7. Search any item in searchbox. Wait for 8-10 seconds depending on internet speed and get your   		results   in extension.



