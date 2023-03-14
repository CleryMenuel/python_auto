"""
Pour automatiser la sauvegarde tous les jours à 23h, vous pouvez utiliser le module schedule qui permet 
de planifier des tâches récurrentes en Python. Voici un exemple de script qui sauvegarde le dossier tous les jours à 23h :
"""
import os
import shutil
import schedule
import time
import datetime

def sauvegarde():
    dossier_source = "C:/Users/inazu/Bureau/test"
    date = str(datetime.datetime.now().date())
    dossier_destination = "C:/Users/inazu/OneDrive/Documents/sauvegarde/" + date + "/test"

    if not os.path.exists(dossier_destination):
        shutil.copytree(dossier_source, dossier_destination)
        print("La sauvegarde a été effectuée avec succès.")
    else:
        print("Le dossier de destination existe déjà.")

# Planifier la sauvegarde tous les jours à 23h
schedule.every().day.at("14:50").do(sauvegarde)

while True:
    # Exécuter les tâches planifiées
    schedule.run_pending()
    # Attendre une seconde avant de vérifier à nouveau
    time.sleep(1)


"""
Ce script définit une fonction sauvegarde qui contient le code pour copier le dossier source vers le dossier de destination, 
puis planifie l'exécution de cette fonction tous les jours à 23h à l'aide de la méthode schedule.every().day.at("23:00").do(sauvegarde).
Ensuite, il exécute continuellement les tâches planifiées à l'aide d'une boucle while True et utilise time.sleep(1) pour 
éviter de consommer trop de ressources système.
La boucle while True dans ce script est utilisée pour exécuter en continu les tâches planifiées à l'aide de la bibliothèque schedule.

La fonction schedule.run_pending() est appelée dans cette boucle pour exécuter toutes les tâches planifiées qui sont prêtes à 
l'heure actuelle. Si aucune tâche n'est prête, cette fonction ne fait rien. La fonction time.sleep(1) est également appelée dans 
la boucle pour éviter de surcharger le processeur, en attendant une seconde avant de vérifier à nouveau 
si une tâche est prête à être exécutée.

En résumé, la boucle while True est utilisée pour maintenir le script en cours d'exécution et vérifier périodiquement si 
une tâche planifiée doit être exécutée. Cela permet de garantir que la sauvegarde est exécutée tous les jours à l'heure prévue, 
sans avoir à exécuter le script manuellement chaque fois.
"""

"""
si la machine redémarre, le programme ne sera plus en cours d'exécution et la sauvegarde quotidienne à 23h ne sera plus effectuée. 
Cela est dû au fait que le script doit être lancé manuellement à chaque fois que la machine redémarre.

Si vous voulez que le programme soit lancé automatiquement au démarrage de la machine, 
vous pouvez ajouter le script dans les tâches planifiées de Windows en utilisant l'utilitaire "Planificateur de tâches". 
Cela permettra au script d'être exécuté automatiquement chaque fois que la machine sera démarrée.

Pour cela, vous devez créer une nouvelle tâche planifiée, spécifier le chemin d'accès au script Python, 
définir les options de sécurité appropriées, et planifier la tâche pour qu'elle soit exécutée au démarrage de la machine.

Une fois que vous avez créé la tâche planifiée, le script sera lancé automatiquement à chaque démarrage de la machine, 
et la sauvegarde quotidienne à 23h sera effectuée comme prévu.
"""

"""
N'OUBLIEZ PAS D'INSTALLER SCHEDULE:
"pip install schedule" 
dans l'invité de commande
POSSIBILITE QUE SHUTIL NE SOIT PAS INSTALLE SI C'EST LE CAS REINSTALLE PYTHON CAR DE BASE LA BIBLIOTHEQUE EST FOURNIE AVEC PYTHON SINON : 
"pip install shutil"
dans l'invité de commande
"""