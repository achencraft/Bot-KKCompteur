#######################################################################################
#                                                                                     #
#                                Fonction lignes                                      #
#                                                                                     #
#######################################################################################
import interactions


class Admin(interactions.Extension):
    def __init__(self, client):
        return



#commande   reload pour executer update.py
#commande   definir_preference pour la compagnie par défaut du serveur



def setup(client):
    Admin(client)
