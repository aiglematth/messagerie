"""
Classe rassemblant les outils ayant rapport aux relations réseau.
"""
import socket
class Serveur():
    """
    Classe rassemblant les outils ayant rapport aux serveurs.
    """
    def __init__(self, ip, port):
        """
        Constructeur de la classe Serveur.
        """
        self.ip = ip
        self.port = port

    def serveur(self):
        """
        Création de l'objet socket.
        """
        serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return serveur

    def open_serveur(self, connexion):
        """
        Initialisation de l'écoute.
        """
        connexion.bind((self.ip, self.port))
        connexion.listen(1)
        client, info = connexion.accept()
        return (client, info)

    def close_serveur(self, connexion):
        connexion.close()

class Client():
    """
    Classe rassemblant les outils ayant rapport aux clients.
    """
    def __init__(self, ip, port):
        """
        Constructeur de la classe Client.
        """
        self.ip = ip
        self.port = port

    def client(self):
        """
        Création de l'objet socket.
        """
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return client

    def connect_client(self, connexion):
        """
        Initialisation de la connexion.
        """
        try:
            connexion.connect((self.ip, self.port))
        except:
            print('Le destinataire est actuellement injoignable, veuillez contacter votre administateur si le problème persiste.')

    def close_client(self, connexion):
        connexion.close()

if __name__ == '__main__':
    serveur = Serveur('localhost', 5555)
    con = serveur.serveur()
    serveur.open_serveur(con)
