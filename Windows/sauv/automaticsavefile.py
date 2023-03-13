"""
Pour automatiser la sauvegarde tous les jours à 23h, vous pouvez utiliser le module schedule qui permet de planifier des tâches récurrentes en Python. Voici un exemple de script qui sauvegarde le dossier tous les jours à 23h :
"""

import shutil
import schedule
import time

def sauvegarde():
    # Chemin du dossier à sauvegarder
    dossier_source = r'C:\chemin\vers\dossier\source'

    # Chemin du dossier de destination sur le NAS
    dossier_destination = r'\\adresseIPdunNAS\chemin\vers\dossier\destination'

    # Copie récursive du dossier source vers le dossier destination
    shutil.copytree(dossier_source, dossier_destination)
    print("Sauvegarde effectuée avec succès !")

# Planifier la sauvegarde tous les jours à 23h
schedule.every().day.at("23:00").do(sauvegarde)

while True:
    # Exécuter les tâches planifiées
    schedule.run_pending()
    # Attendre une seconde avant de vérifier à nouveau
    time.sleep(1)

"""
Ce script définit une fonction sauvegarde qui contient le code pour copier le dossier source vers le dossier de destination, puis planifie l'exécution de cette fonction tous les jours à 23h à l'aide de la méthode schedule.every().day.at("23:00").do(sauvegarde). Ensuite, il exécute continuellement les tâches planifiées à l'aide d'une boucle while True et utilise time.sleep(1) pour éviter de consommer trop de ressources système.
La boucle while True dans ce script est utilisée pour exécuter en continu les tâches planifiées à l'aide de la bibliothèque schedule.

La fonction schedule.run_pending() est appelée dans cette boucle pour exécuter toutes les tâches planifiées qui sont prêtes à l'heure actuelle. Si aucune tâche n'est prête, cette fonction ne fait rien. La fonction time.sleep(1) est également appelée dans la boucle pour éviter de surcharger le processeur, en attendant une seconde avant de vérifier à nouveau si une tâche est prête à être exécutée.

En résumé, la boucle while True est utilisée pour maintenir le script en cours d'exécution et vérifier périodiquement si une tâche planifiée doit être exécutée. Cela permet de garantir que la sauvegarde est exécutée tous les jours à l'heure prévue, sans avoir à exécuter le script manuellement chaque fois.
"""