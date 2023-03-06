#!/usr/bin/env python3

import os

# Définir l'adresse IP statique, le masque de sous-réseau et la passerelle par défaut
ip_address = "192.168.1.100"
subnet_mask = "255.255.255.0"
default_gateway = "192.168.1.1"

# Définir le chemin du fichier de configuration d'interface réseau
interface_file = "/etc/netplan/01-netcfg.yaml"

# Ouvrir le fichier de configuration en mode écriture
with open(interface_file, "w") as file:
    # Écrire la configuration de l'interface réseau
    file.write("# This file is generated by Python\n")
    file.write("network:\n")
    file.write("  version: 2\n")
    file.write("  renderer: networkd\n")
    file.write("  ethernets:\n")
    file.write("    enp0s3:\n")  # Modifier le nom de l'interface en fonction de votre configuration
    file.write("      dhcp4: no\n")
    file.write(f"      addresses: [{ip_address}/{subnet_mask}]\n")
    file.write(f"      gateway4: {default_gateway}\n")

# Appliquer la nouvelle configuration de l'interface réseau
os.system("sudo netplan apply")

"""
Ce script définit une adresse IP statique de 192.168.1.100 avec un masque de sous-réseau de 255.255.255.0 et 
une passerelle par défaut de 192.168.1.1. Le nom de l'interface réseau est défini sur enp0s3, mais 
vous devrez le modifier en fonction de votre configuration.

Le script écrit ensuite la configuration de l'interface réseau dans le fichier /etc/netplan/01-netcfg.yaml et 
applique la nouvelle configuration en exécutant la commande sudo netplan apply. 
Notez que vous devrez exécuter ce script avec les privilèges sudo pour qu'il puisse écrire dans le fichier de configuration et 
appliquer les modifications.
"""