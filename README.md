# Network-Scanner

**Network-Scanner** is a python tool designed to find the connected devices into a network (tested on Kali)


## Install

**Prerequisites**

- Python 3.7.6

**Installing**

    $ git clone https://github.com/amananand369/Network-Scanner.git

    $ cd Network-Scanner

    $ python3 NetScanner.py -ip 192.168.1.1 or python3 NetScanner.py --ip 192.168.1.1/24
  
 NetScanner arguments
-----

    $ python3 NetScanner.py --help 
  
  Options:
  
    -h,     --help      show this help message and exit
    -i IP,  --ip = IP   IP Address or Range

  
  Example
-------

**Scan Network**

     $ python3 NetScanner.py -i 192.168.1.1 or python3 NetScanner.py --ip 192.168.1.1

     $ python3 NetScanner.py -i 192.168.1.1/24 or python3 NetScanner.py --ip 192.168.1.1/24
  
  
  
