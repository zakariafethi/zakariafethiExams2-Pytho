from Vehicule import Vehicule
class Metro(Vehicule):
    def __init__(self, marque, matricule, couleur, nombreRoues, besoinChauffeur, vitesse, ligne):
        super().__init__(marque, matricule, couleur, nombreRoues, besoinChauffeur, vitesse)
        self._ligne = ligne

    # Getter and setter for ligne
    def get_ligne(self):
        return self._ligne
    def set_ligne(self, ligne):
        self._ligne = ligne
