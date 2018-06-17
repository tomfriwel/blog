---
title: ubuntu apache python mysql setup
tags:
---

#### Version
```
$ cat /etc/issue
> Ubuntu 14.04.2 LTS \n \l
```

#### Setup

[How To Set Up an Apache, MySQL, and Python (LAMP) Server Without Frameworks on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-apache-mysql-and-python-lamp-server-without-frameworks-on-ubuntu-14-04)

```
$ sudo rm /usr/bin/python
$ sudo ln -s /usr/bin/python3 /usr/bin/python
$ sudo a2dismod mpm_event
```
```
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
	LANGUAGE = "en_US:",
	LC_ALL = (unset),
	LC_CTYPE = "UTF-8",
	LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
Module mpm_event already disabled
```

Get rid of this warning:

[How to set locale?](https://askubuntu.com/a/17002)
[Cannot set LC_CTYPE to default locale: No such file or directory](https://askubuntu.com/a/749780)

```
$ sudo apt-get install language-pack-en-base
$ sudo dpkg-reconfigure locales
$ export LC_ALL="en_US.UTF-8"
```

Setup Apache conf:

```
<VirtualHost *:80>
    <Directory /var/www/test>
        Options +ExecCGI
        DirectoryIndex index.py
    </Directory>
    AddHandler cgi-script .py

    ...
```

index.py:
```python
#!/usr/bin/python

print('Content-type:text/html\r\n')
print('hello')

```

```
$ sudo chmod 755 /var/www/test/index.py
$ sudo service apache2 restart
```

---

## Content of [How To Set Up an Apache, MySQL, and Python (LAMP) Server Without Frameworks on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-apache-mysql-and-python-lamp-server-without-frameworks-on-ubuntu-14-04)

#### Introduction

This article will walk you through setting up a server with Python 3, MySQL, and Apache2, sans the help of a framework. By the end of this tutorial, you will be fully capable of launching a barebones system into production.

Django is often the one-shop-stop for all things Python; it's compatible with nearly all versions of Python, comes prepackaged with a custom server, and even features a one-click-install database. Setting up a vanilla system without this powerful tool can be tricky, but earns you invaluable insight into server structure from the ground up.

This tutorial uses only package installers, namely apt-get and Pip. Package installers are simply small programs that make code installations much more convenient and manageable. Without them, maintaining libraries, modules, and other code bits can become an extremely messy business.

Prerequisites
To follow this tutorial, you will need:

One Ubuntu 14.04 Droplet.
A sudo non-root user, which you can set up by following this tutorial.
Step 1 — Making Python 3 the Default
In this step, we will set Python 3 as the default for our python command.

First, check your current Python version.

`$ python --version`

On a fresh Ubuntu 14.04 server, this will output:

` Python 2.7.6`

We would like to have python run Python 3. So first, let's remove the old 2.7 binary.

`$ sudo rm /usr/bin/python`
Next, create a symbolic link to the Python 3 binary in its place.

`$ sudo ln -s /usr/bin/python3 /usr/bin/python`

If you run `python --version` again, you will now see `Python 3.4.0`.

Step 2 — Installing Pip
In this section, we will install Pip, the recommended package installer for Python.

First, update the system's package index. This will ensure that old or outdated packages do not interfere with the installation.

sudo apt-get update
Pip allows us to easily manage any Python 3 package we would like to have. To install it, simply run the following:

sudo apt-get install python3-pip
For an overview of Pip, you can read this tutorial.

Step 3 — Installing MySQL
In this section, we will install and configure MySQL.

Installing SQL is simple:

sudo apt-get install mysql-server
Enter a strong password for the MySQL root user when prompted, and remember it, because we will need it later.

The MySQL server will start once installation completes. After installation, run:

mysql_secure_installation
This setup will take you through a series of self-explanatory steps. First, you'll need to enter the root password you picked a moment ago. The first question will ask if you want to change the root password, but because you just set it, enter n. For all other questions, press ENTER to accept the default response.

Python 3 requires a way to connect with MySQL, however. There are a number of options, like MySQLclient, but for the module's simplicity, this tutorial will use pymysql. Install it using Pip:

sudo pip3 install pymysql
Step 4 — Installing Apache 2
In this section, we will install Apache 2, and ensure that it recognizes Python files as executables.

Install Apache using apt-get:

sudo apt-get install apache2
Like MySQL, the Apache server will start once the installation completes.

Note: After installation, several ports are open to the internet. Make sure to see the conclusion of this tutorial for resources on security.

We want to place our website's root directory in a safe location. The server is by default at /var/www/html. To keep convention, we will create a new directory for testing purposes, called test, in the same location.

sudo mkdir /var/www/test
Finally, we must register Python with Apache. To start, we disable multithreading processes.

sudo a2dismod mpm_event
Then, we give Apache explicit permission to run scripts.

sudo a2enmod mpm_prefork cgi
Next, we modify the actual Apache configuration, to explicitly declare Python files as runnable file and allow such executables. Open the configuration file using nano or your favorite text editor.

sudo nano /etc/apache2/sites-enabled/000-default.conf
Add the following right after the first line, which reads <VirtualHost *:80\>.

<Directory /var/www/test>
    Options +ExecCGI
    DirectoryIndex index.py
</Directory>
AddHandler cgi-script .py
Make sure that your <Directory> block is nested inside the <VirtualHost> block, like so. Make sure to indent correctly with tabs, too.

/etc/apache2/sites-enabled/000-default.conf

<VirtualHost *:80>
    <Directory /var/www/test>
        Options +ExecCGI
        DirectoryIndex index.py
    </Directory>
    AddHandler cgi-script .py

    ...
This Directory block allows us to specify how Apache treats that directory. It tells Apache that the /var/www/test directory contains executables, considers index.py to be the default file, then defines the executables.

We also want to allow executables in our website directory, so we need to change the path for DocumentRoot, too. Look for the line that reads DocumentRoot /var/www/html, a few lines below the long comment at the top of the file, and modify it to read /var/www/test instead.

DocumentRoot /var/www/test
Your file should now resemble the following.

/etc/apache2/sites-enabled/000-default.conf

<VirtualHost *:80>
        <Directory /var/www/test>
                Options +ExecCGI
                DirectoryIndex index.py
        </Directory>
        AddHandler cgi-script .py

        ...

        DocumentRoot /var/www/test

        ...
Save and exit the file. To put these changes into effect, restart Apache.

sudo service apache2 restart
Note: Apache 2 may throw a warning which says about the server's fully qualified domain name; this can be ignored as the ServerName directive has little application as of this moment. They are ultimately used to determine subdomain hosting, after the necessary records are created.

If the last line of the output reads [ OK ], Apache has restarted successfully.

Step 5 — Testing the Final Product
In this section, we will confirm that individual components (Python, MySQL, and Apache) can interact with one another by creating an example webpage and database.

First, let's create a database. Log in to MySQL. You'll need to enter the MySQL root password you set earlier.

mysql -u root -p
Add an example database called example.

CREATE DATABASE example;
Switch to the new database.

USE example;
Add a table for some example data that we'll have the Python app add.

CREATE TABLE numbers (num INT, word VARCHAR(20));
Press CTRL+D to exit. For more background on SQL, you can read this MySQL tutorial.

Now, create a new file for our simple Python app.

sudo nano /var/www/test/index.py
Copy and paste the following code in. The in-line comments describe what each piece of the code does. Make sure to replace the passwd value with the root MySQL password you chose earlier.

#!/usr/bin/python

# Turn on debug mode.
import cgitb
cgitb.enable()

# Print necessary headers.
print("Content-Type: text/html")
print()

# Connect to the database.
import pymysql
conn = pymysql.connect(
    db='example',
    user='root',
    passwd='your_root_mysql_password',
    host='localhost')
c = conn.cursor()

# Insert some example data.
c.execute("INSERT INTO numbers VALUES (1, 'One!')")
c.execute("INSERT INTO numbers VALUES (2, 'Two!')")
c.execute("INSERT INTO numbers VALUES (3, 'Three!')")
conn.commit()

# Print the contents of the database.
c.execute("SELECT * FROM numbers")
print([(r[0], r[1]) for r in c.fetchall()])

Save and exit.

Next, fix permissions on the newly-created file. For more information on the three-digit permissions code, see the tutorial on Linux permissions.

sudo chmod 755 /var/www/test/index.py
Now, access your server's by going to http://your_server_ip using your favorite browser. You should see the following:

your_server_ip'>http://your_server_ip
[(1, 'One!'), (2, 'Two!'), (3, 'Three!')]
Congratulations! Your server is now online.

Conclusion
You now have a working server that can run Python 3 with a robust, SQL database. The server is now also configured for easy maintenance, via well-documented and established package installers.

However, in its current state, the server is vulnerable to outsiders. Whereas elements like SSL encryption are not essential to your server's function, they are indispensable resources for a reliable, safe server. Learn more by reading about how to configure Apache, how to create an Apache SSL certificate and how to secure your Linux server.
