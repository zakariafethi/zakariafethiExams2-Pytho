class Vehicule:
    def __init__(self, marque, matricule, couleur, nombreRoues, besoinChauffeur, vitesse):
        self._marque = marque
        self._matricule = matricule
        self._couleur = couleur
        self._nombreRoues = nombreRoues
        self._besoinChauffeur = besoinChauffeur
        self._vitesse = vitesse

    # marque
    def get_marque(self):
        return self.marque
    def set_marque(self, marque):
        self._marque = marque

    # matricule
    def get_matricule(self):
        return self._matricule
    def set_matricule(self, matricule):
        self._matricule = matricule

    # couleur
    def get_couleur(self):
        return self._couleur
    def set_couleur(self, couleur):
        self._couleur = couleur

    # nombreRoues
    def get_nombreRoues(self):
        return self._nombreRoues
    def set_nombreRoues(self, nombreRoues):
        self._nombreRoues = nombreRoues

    # besoinChauffeur
    def get_besoinChauffeur(self):
        return self._besoinChauffeur
    def set_besoinChauffeur(self, besoinChauffeur):
        self._besoinChauffeur = besoinChauffeur

    # vitesse
    def get_vitesse(self):
        return self._vitesse
    def set_vitesse(self, vitesse):
        self._vitesse = vitesse
