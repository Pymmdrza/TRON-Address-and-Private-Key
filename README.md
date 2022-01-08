# TRON-Address-and-Private-Key
File Python TRX Tron Privatekey and address fast generator with Python
make and create wallet address and private key in tron network (trx) with help python for batch maker code sample . In this tool, many other models and methods can be used and it can be used for other ways, which I will try in the future for you, dear friends, more and more professional tools in this field. But as far as I could, I sent this tutorial simple so that even beginners can understand it from the beginning tron (TRX). I promise you the future development of this tool.
```
# Programmer MMDRZA | https://MMDRZA.COM
# Python / TRON , TRONPY
from tronpy.keys import PrivateKey
import time

a=1
while True:
    Private = PrivateKey.random()
    Address  = Private.public_key.to_base58check_address()
    print((a),'\nP:',Private,'\nA:',Address)
# You can change it in seconds. The less it is
# the faster you want the result. The more CPU it uses.
    time.sleep(1)
# You can delete this value if you do not need to number
# and sort the output results
    a=a+1
```
    
###How To Create Address and Private Key  Tron TRX

Install :

 `

    Python3
    
    pip3
    
    Anaconda
    
    Vitrualenv
    
    Spyder
    
    Tron
    
    tronpy
    
    
 `

i for tools use Anaconda Package and Vitrualenv Python3 , Spyder IDE for Edit and test cod run . include package for this tools tron , tronpy .
how to install #Anaconda In Windows ( install Anaconda in Windows Common CMD )

Anaconda is a package manager, an environment manager, and Python distribution that contains a collection of many open source packages. This is advantageous as when you are working on a data science project, you will find that you need many different packages (numpy, scikit-learn, scipy, pandas to name a few), which an installation of Anaconda comes preinstalled with. If you need additional packages after installing Anaconda, you can use Anaconda’s package manager, conda, or pip to install those packages. This is highly advantageous as you don’t have to manage dependencies between multiple packages yourself. Conda even makes it easy to switch between Python 2 and 3 (you can learn more here).

In fact, an installation of Anaconda is also the recommended way to install Jupyter Notebooks 

More About Install Anaconda Visit Datacamp Site This [Link]
How To Create Tron (TRX) Wallet Address and Private Key With Python
How To Install #Python3

    Step 1: Select Version of Python to Install. …
    Step 2: Download Python Executable Installer. …
    Step 3: Run Executable Installer. …
    Step 4: Verify Python Was Installed On Windows. …
    Step 5: Verify Pip Was Installed. …
    Step 6: Add Python Path to Environment Variables (Optional)

Install Python3 visit this Post 
Install pip3 On Windows and Linux 

after install python if have not pip3 package on your system , can use this common with CMD on Windows and Terminal There Linux (Debian OS)

pip3 Windows:

```

npm install pip3

```

###pip3 Linux:

    Step 1 – Update system. It is always a good idea to update before trying to install a new package. …
    Step 2 – Install pip3. If Python 3 has already been installed on the system, execute the command below to install pip3:
```
sudo apt-get -y install python3-pip
```

  
###How To Install Spyder IDE Python

You can install Spyder with the pip package manager, which comes by default with most Python installations. Before installing Spyder itself by this method, you need to acquire the Python programming language. Then, to install Spyder and its other dependencies, run pip install spyder  (Read More)

 

###How to install virtualenv:

    Install pip first. sudo apt-get install python3-pip.
    Then install virtualenv using pip3. …
    Now create a virtual environment. …
    You can also use a Python interpreter of your choice. …
    Active your virtual environment: …
    Using fish shell: …
    To deactivate: …
    Create virtualenv using Python3.

#Install pip first

```
sudo apt-get install python3-pip
```

#Then install virtualenv using pip3
```
sudo pip3 install virtualenv
```

#Now create a virtual environment

```
virtualenv venv
```

#you can use any name insted of venv


#You can also use a Python interpreter of your choice

```
virtualenv -p /usr/bin/python2.7 venv
```

#Active your virtual environment:

```
source venv/bin/activate
```

#Using fish shell:

```

source venv/bin/activate.fish
```

#To deactivate:
deactivate

#Create virtualenv using Python3

```
virtualenv -p python3 myenv
``` 

#Instead of using virtualenv you can use this command in Python3
```
python3 -m venv myenv

```

Install Package TRON in Python (Code)

 
```
$ pip install tron

```

or

```

$ pip3 install tron

$ pip install tronapi

$ pip3 install tronapi

```

Install tronpy package python

 
```
pip3 install tronpy
```    


Visit Orginal Post + Video Link ==> https://mmdrza.com/create-private-key-and-address-tron-python/
