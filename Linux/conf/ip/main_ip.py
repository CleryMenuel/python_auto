import platform
import os

# Obtenir la version du système d'exploitation
if platform.system() == 'Linux':
    version = platform.release()

# Vérifier si la version est inférieure à 20.04
    if version < '17.10':
        os.system("python scripts/ipstatic_ubuntuinf17.10.py")
    elif version >= '17.10':
        os.system("python scripts/ipstatic_ubuntusupegal17.10.py")
# Gros message d'erreur si cela intervient contacter le dev du programme
    else:
        print("ERROR")
# Message d'erreur car le systeme d'exploitation n'est pas un linux
else:
    print("Le système d'exploitation n'est pas Linux. Le script ne sera pas exécuté.")