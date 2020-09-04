#!/bin/bash


# Installing Ansible with pip
#Ansible can be installed with pip, the Python package manager. 
#If pip isn’t already available on your system of Python
#run the following commands to install it:





	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	python get-pip.py --user
	pip install --user git+https://github.com/ansible/ansible.git@devel
	

	#If you are installing on macOS Mavericks (10.9), you may encounter some noise from your compiler. A workaround is to do the following :

	CFLAGS=-Qunused-arguments CPPFLAGS=-Qunused-arguments pip install --user ansible
	pip install --user paramiko
	sudo python get-pip.py
	sudo pip install ansible
	
