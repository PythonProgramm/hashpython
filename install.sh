#! /bin/sh

sudo mkdir /usr/share/hashpython/
sudo cp MD5.py /usr/share/hashpython/
sudo cp MD4.py /usr/share/hashpython/
sudo cp SHA224.py /usr/share/hashpython/
sudo cp SHA384.py /usr/share/hashpython/
sudo cp main.py /usr/share/hashpython/
sudo cp hashpython /bin/
sudo chmod +x /bin/hashpython