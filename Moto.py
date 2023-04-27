from Vehicule import Vehicule
class Moto(Vehicule):
    def __init__(self, marque, matricule, couleur, nombreRoues, besoinChauffeur, vitesse, typeMoto):
        super().__init__(marque, matricule, couleur, nombreRoues, besoinChauffeur, vitesse)
        self._typeMoto = typeMoto

    # Getter and setter for typeMoto
    def get_typeMoto(self):
        return self._typeMoto
    def set_typeMoto(self, typeMoto):
        self._typeMoto = typeMoto
