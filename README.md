I am new to GIThub and Raspberry Pi. This is my repo for learning how to navigate the Raspberry Pi 3 B+ that I was gifted from a thoughtful mentor. It was intially a PWNIGOTCHI that I have repurposed for a network information discovery tool. Here are some additional commands that may be of use to you. Please forgive me if I have not followed GIThub best practices, I am still learning to use this service. 


pi@testpi:~ $ sudo apt update
pi@testpi:~ $ sudo apt upgrade


pi@testpi:~ $ sudo apt-get install python3-rpi.gpio python3-spidev python3-pil python3-pip
pi@testpi:~ $ git clone https://github.com/waveshare/e-Paper.git
cd e-Paper/RaspberryPi_JetsonNano/python
sudo python3 setup.py install

These libraries are used to access network information

pi@testpi:~/e-Paper/RaspberryPi_JetsonNano/python $ sudo apt install python3-setuptools
pi@testpi:~/e-Paper/RaspberryPi_JetsonNano/python $ sudo apt install python3-netifaces
