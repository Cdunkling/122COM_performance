#!bin/bash
apt-get update
apt-get -y install build-essentials
apt-get -y install python3 python3-setuptools
apt-get -y install graphviz
apt-get -y install evince
easy_install3 snakeviz gprof2dot
