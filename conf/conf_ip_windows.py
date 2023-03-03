"""
Voici un exemple de script Python qui définit une adresse IP statique sur un système Windows :
"""
import subprocess

# Définir l'adresse IP statique, le masque de sous-réseau et la passerelle par défaut
ip_address = "192.168.1.60"
subnet_mask = "255.255.255.0"
default_gateway = "192.168.1.254"

# Configurer l'adresse IP statique avec netsh
command = f"netsh interface ipv4 set address name=\"Ethernet\" static {ip_address} {subnet_mask} {default_gateway}"
subprocess.call(command, shell=True)

# Configurer le DNS avec netsh
dns_server = "8.8.8.8"
command = f"netsh interface ipv4 add dnsserver name=\"Ethernet\" address={dns_server} index=1"
subprocess.call(command, shell=True)

# Redémarrer le service DHCP pour éviter les conflits d'adresse IP
subprocess.call("net stop dhcp & net start dhcp", shell=True)

"""
Ce script utilise la bibliothèque subprocess pour exécuter des commandes système et configurer l'adresse IP statique avec la commande netsh. 
Il définit également un serveur DNS et redémarre le service DHCP pour éviter les conflits d'adresse IP. 
Vous pouvez personnaliser les valeurs de ip_address, subnet_mask, default_gateway et dns_server selon vos besoins. 
N'oubliez pas d'exécuter le script en tant qu'administrateur pour pouvoir effectuer les changements de configuration réseau.
"""