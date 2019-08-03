#!/bin/bash
######################################################
#                librerias.sh
######################################################
echo "---------herramientas de Desarrollador----------"
sudo apt -y install build-essential cmake unzip pkg-config

echo "---------Librerias manejo de imagen y video----------"
sudo ap -y install libjpeg-dev libpng-dev libtiff-dev
sudo apt -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt -y install libxvidcore-dev libx264-dev

echo "---------Instalar GTK----------"
sudo apt -y install libgtk-3-dev

echo "---------Eliminar warnings de gtk----------"
sudo apt -y install libcanberra-gtk*

echo "---------Optimizaciones para calculos numericos----------"
sudo apt -y install libatlas-base-dev gfortran

echo "---------Librerias de Desarrollo Python----------"
sudo apt -y install python3-dev
