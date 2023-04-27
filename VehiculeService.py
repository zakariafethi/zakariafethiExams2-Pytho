class VehiculeService:
    def __init__(self):
        self._motos = []
        self._voitures = []
        self._metros = []

    # Add methods
    def add_moto(self, moto):
        self._motos.append(moto)

    def add_voiture(self, voiture):
        self._voitures.append(voiture)

    def add_metro(self, metro):
        self._metros.append(metro)

    # update
    def update_moto(self, old_moto, new_moto):
        index = self._motos.index(old_moto)
        self._motos[index] = new_moto

    def update_voiture(self, old_voiture, new_voiture):
        index = self._voitures.index(old_voiture)
        self._voitures[index] = new_voiture

    def update_metro(self, old_metro, new_metro):
        index = self._metros.index(old_metro)
        self._metros[index] = new_metro

    # delete
    def delete_moto(self, moto):
        self._motos.remove(moto)

    def delete_voiture(self, voiture):
        self._voitures.remove(voiture)

    def delete_metro(self, metro):
        self._metros.remove(metro)

    # find
        def get_motos(self):
            return self.motos

        def find_moto(self, matricule):
            for moto in self.motos:
                if moto.get_matricule() == matricule:
                    return moto
            return None

        def get_voitures(self):
            return self.voitures

        def find_voiture(self, matricule):
            for voiture in self.voitures:
                if voiture.get_matricule() == matricule:
                    return voiture
            return None

        def get_metros(self):
            return self.metros

        def find_metro(self, matricule):
            for metro in self.metros:
                if metro.get_matricule() == matricule:
                    return metro
            return None