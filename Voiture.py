from Vehicule import Vehicule
class Voiture(Vehicule):
    def __init__(self, marque, matricule, couleur, nombreRoues, besoinChauffeur, vitesse, nbPorte):
        super().__init__(marque, matricule, couleur, nombreRoues, besoinChauffeur, vitesse)
        self._nbPorte = nbPorte

    # Getter and setter for nbPorte
    def get_nbPorte(self):
        return self._nbPorte
    def set_nbPorte(self, nbPorte):
        self._nbPorte = nbPorte
