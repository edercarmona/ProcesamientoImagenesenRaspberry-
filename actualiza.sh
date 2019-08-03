#!/bin/bash
##################################
#        actualiza.sh
##################################
echo "---------Actuliazndo Repositorios----------"
sudo apt -y update
echo "---------Instalando poaquetes----------"
sudo apt -y upgrade
echo "----------Actuliazndo Distribucion---------"
sudo apt -y dist-upgrade
echo "----------Actuliazndo firmware-----------"
sudo rpi-update
