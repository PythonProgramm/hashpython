#! /bin/sh

sudo pip3 install passlib # for ntlm and lm support
sudo pip3 install numba # for gpu support

sudo mkdir /usr/share/hashpython/
sudo cp MD5.py /usr/share/hashpython/
sudo cp MD4.py /usr/share/hashpython/
sudo cp SHA224.py /usr/share/hashpython/
sudo cp SHA384.py /usr/share/hashpython/
sudo cp SHA512WHIRLPOOL.py /usr/share/hashpython/
sudo cp main.py /usr/share/hashpython/
sudo cp hashpython /bin/
sudo cp hashid.py /usr/share/hashpython/
sudo chmod +x /bin/hashpython
sudo cp shadow2hashpython /bin/
sudo chmod +x /bin/shadow2hashpython
sudo cp shadow2hashpython.py /usr/share/hashpython/
sudo cp unix.py /usr/share/hashpython/
sudo cp ntlm.py /usr/share/hashpython/