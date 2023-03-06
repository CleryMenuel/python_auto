import platform
import os

# Obtenir la version du système d'exploitation
if platform.system() == 'Linux':
    version = platform.release()

# Vérifier si la version est inférieure à 20.04
    if version < '20.04':
        os.system("python scripts/ipstatic_ubuntuinf20.04.py")
    elif version >= '20.04':
        print("PARFAITTTTT")
    else:
        print("La version du système d'exploitation est supérieure à 20.04. Le script ne sera pas exécuté.")
else:
    print("Le système d'exploitation n'est pas Linux. Le script ne sera pas exécuté.")