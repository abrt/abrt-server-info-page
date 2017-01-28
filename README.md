# ABRT server info page

**A webpage for servers containing ABRT's services**

### About
The main purpose of this webpage is to provide some user-friendly welcome
page on servers on which ABRT's services are running e.g 
([FAF](https://github.com/abrt/faf) or 
[Retrace server](https://github.com/abrt/retrace-server)).

This page should present information about ABRT and our services, tools and 
libraries.

### Running and deploying
**Test-running this webpage locally:**

    $ git clone https://github.com/abrt/abrt-server-info-page.git

    $ cd abrt-server-info-page

    $ export FLASK_APP=abrt_server_info_page.py

    $ flask run
Now click the link the flask provided you and you should see the page in your
browser.

**Deploying this webpage:**
* Easiest way is to build a rpm package and install it:

    `$ tito build --rpm -i`

* Without building you need to distribute files manually:

    `$ cp config/abrt-server-info-page.conf /etc/httpd/conf.d/`

    `$ cp -r ../abrt-server-info-page/ /usr/lib/python2.7/site-packages/`

You will probably need to restart Apache.



