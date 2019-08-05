#!/bin/bash
##########################################
#               instala.sh
##########################################
echo "---------Instalando OpenCV----------"
cd ~/opencv/build
sudo make install
sudo ldconfig
cd /usr/lib/python3/dist-packages/
ln -s /usr/local/python/cv2/python-3.7/cv2.cpython-37m-arm-linux-gnueabihf.so cv2.so
cd ~

