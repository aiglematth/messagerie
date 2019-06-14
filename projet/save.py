"""
Fichier contenant la classe Save elle meme contenant les outils de sauvegarde.
"""
import pickle

class Save():
    """
    Classe Save contenant les outils de sauvegarde.
    """
    def __init__(self):
        pass

    def SaveData(self, chemin, data):
        with open(chemin, 'wb') as fichier:
            mon_pickle = pickle.Pickler(fichier)
            mon_pickle.dump(data)

    def LoadData(self, chemin):
        with open(chemin, 'rb') as fichier:
            mon_pickle = pickle.Unpickler(fichier)
            data = mon_pickle.load()
            return data

    def ChangeData(self, chemin, newdata):
        data = self.LoadData(chemin)
        ndata = {}
        for key, value in data.items():
            for nkey, nvalue in newdata.items():
                if nkey in data.keys():
                    if key == nkey:
                        data[key] = nvalue
                    else:
                        pass
                else:
                    ndata[nkey] = nvalue
        for key, value in ndata.items():
            data[key] = value
        self.SaveData(chemin, data)
        d = self.LoadData(chemin)
        print(d)


if __name__ == '__main__':
    data = {'login':'xx-arcamyst-xx', 'sound':1}
    s = Save()
    t = s.LoadData('constantes.txt')
    print(t)
