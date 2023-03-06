#Voici un exemple de script Python qui peut être utilisé pour configurer une adresse IP statique persistante sur un système Linux :

import os

# Définir l'adresse IP statique, le masque de sous-réseau et la passerelle par défaut
ip_address = input("Entrez une adresse IP (Ex : 192.168.1.60) : ")
subnet_mask = input("Entrez un masque de sous réseau (Ex : 255.255.255.0) : ")
default_gateway = input("Entrez la passerelle par default (Ex : 192.168.1.254) : ")

# Modifier le fichier de configuration réseau pour ajouter les paramètres d'adresse IP statique
with open('/etc/network/interfaces', 'a') as config_file:
    config_file.write(f"\nauto eth0\niface eth0 inet static\naddress {ip_address}\nnetmask {subnet_mask}\ngateway {default_gateway}\n")

# Redémarrer le réseau pour appliquer les modifications
os.system("sudo systemctl restart networking.service")

"""
Dans ce script, nous utilisons le module os pour exécuter des commandes système, comme le redémarrage du service réseau. 
Nous définissons ensuite l'adresse IP statique, le masque de sous-réseau et la passerelle par défaut en tant que variables. 
Nous ouvrons ensuite le fichier de configuration réseau /etc/network/interfaces en mode d'ajout et ajoutons les paramètres d'adresse IP statique à la fin du fichier.

Notez que ce script doit être exécuté avec des privilèges de superutilisateur pour pouvoir modifier le fichier de configuration réseau et redémarrer le service réseau.

En utilisant ce script, les modifications de configuration réseau seront persistantes après un redémarrage du système. 
Cependant, vous devez vous assurer que le fichier de configuration réseau est correctement modifié pour votre distribution Linux.

Ce code Python configure une adresse IP statique persistante sur un système Linux en modifiant le fichier de configuration réseau et en redémarrant le service réseau.

Voici une explication plus détaillée de ce code :

1 La première ligne importe le module os, qui fournit une interface pour interagir avec le système d'exploitation sous-jacent.

2 Les trois lignes suivantes définissent l'adresse IP statique (ip_address), le masque de sous-réseau (subnet_mask) et la passerelle par défaut (default_gateway).

3 La ligne suivante utilise la fonction open pour ouvrir le fichier de configuration réseau /etc/network/interfaces en mode d'ajout (a). 
    Cela signifie que nous pouvons ajouter des données à la fin du fichier sans écraser les données existantes.

4 La ligne suivante utilise la méthode write pour ajouter les paramètres d'adresse IP statique à la fin du fichier de configuration réseau. 
    Les caractères \n sont utilisés pour insérer des retours à la ligne et rendre les paramètres plus lisibles.

5 La dernière ligne utilise la fonction system du module os pour exécuter la commande sudo systemctl restart networking.service. 
    Cette commande redémarre le service réseau pour appliquer les modifications de configuration.

Notez que pour exécuter ce script avec succès, il doit être exécuté avec des privilèges de superutilisateur (sudo). 
Si vous ne disposez pas de privilèges de superutilisateur, vous pouvez également exécuter le script en tant que superutilisateur en utilisant sudo python nom_du_script.py.
"""
