from Moto import Moto
from Voiture import Voiture
from Metro import Metro
from VehiculeService import VehiculeService

# Initialiser le service de véhicules
service = VehiculeService()

print("Bonjour et bienvenu à l'application de gestion des véhicules de la ville !")
while True:
    # Afficher le menu
    print("Que souhaitez-vous faire ?")
    print("1. Ajouter un véhicule")
    print("2. Mettre à jour un véhicule")
    print("3. Supprimer un véhicule")
    print("5. Quitter")

    choix = input("Entrez votre choix (1-5): ")

    if choix == "1":
        # Add a new véhicule
        marque = input("Entrez la marque du véhicule : ")
        matricule = input("Entrez la matricule  du véhicule : ")
        couleur = input("Entrez la couleur du véhicule : ")
        nombre_roues = input("Entrez le nombre de roues  du véhicule : ")
        besoin_chauffeur = input("Le véhicule a-t-il besoin d'un chauffeur (oui/non) ? ")
        vitesse = input("Entrez la vitesse  du véhicule : ")

        print("Quel type de véhicule souhaitez-vous ajouter ?")
        print("1. Moto")
        print("2. Voiture")
        print("3. Métro")

        type_vehicule = input("Entrez votre choix (1-3): ")

        if type_vehicule == "1":
            # Add moto
            type_moto = input("Entrez le type de moto : ")

            moto = Moto(marque, matricule, couleur, nombre_roues, besoin_chauffeur, vitesse, type_moto)
            service.add_moto(moto)
            print("La moto a été ajoutée avec succès.")

        elif type_vehicule == "2":
            # Add voiture
            nb_porte = input("Entrez le nombre de portes de la voiture : ")

            voiture = Voiture(marque, matricule, couleur, nombre_roues, besoin_chauffeur, vitesse, nb_porte)
            service.add_voiture(voiture)
            print("La voiture a été ajoutée avec succès.")

        elif type_vehicule == "3":
            # Add métro
            ligne = input("Enter the metro's ligne: ")
            metro = Metro(marque, matricule, couleur, nombreRoues, besoinChauffeur, vitesse, ligne)
            service.add_metro(metro)
        else:
            print("Le choix est invalide, réessayez")
    elif choix == 2:
        print("\nQuel véhicule voulez-vous mettre à jour?")
        print("1. Moto")
        print("2. Voiture")
        print("3. Métro")
        print("4. Retour")

        choice = input("Entrez votre choix : ")

        if choice == "1":
            if len(service.get_motos()) == 0:
                print("Aucune moto n'est actuellement enregistrée.")
            else:
                print("Voici la liste des motos enregistrées :")
                for moto in service.get_motos():
                    print(moto)

                moto_choice = input("Entrez le matricule de la moto que vous souhaitez mettre à jour : ")
                moto = service.find_moto(moto_choice)

                if moto is None:
                    print("La moto que vous avez choisie n'a pas été trouvée.")
                else:
                    print(f"Moto à mettre à jour : {moto}")
                    marque = input("Entrez la nouvelle marque de la moto : ")
                    couleur = input("Entrez la nouvelle couleur de la moto : ")
                    vitesse = input("Entrez la nouvelle vitesse de la moto : ")
                    type_moto = input("Entrez le nouveau type de moto : ")
                    new_moto = Moto(marque, moto_choice, couleur, 2, False, vitesse, type_moto)
                    service.update_moto(moto, new_moto)
                    print("La moto a été mise à jour avec succès.")

        elif choice == "2":
            if len(service.get_voitures()) == 0:
                print("Aucune voiture n'est actuellement enregistrée.")
            else:
                print("Voici la liste des voitures enregistrées :")
                for voiture in service.get_voitures():
                    print(voiture)

                voiture_choice = input("Entrez le matricule de la voiture que vous souhaitez mettre à jour : ")
                voiture = service.find_voiture(voiture_choice)

                if voiture is None:
                    print("La voiture que vous avez choisie n'a pas été trouvée.")
                else:
                    print(f"Voiture à mettre à jour : {voiture}")
                    marque = input("Entrez la nouvelle marque de la voiture : ")
                    couleur = input("Entrez la nouvelle couleur de la voiture : ")
                    vitesse = input("Entrez la nouvelle vitesse de la voiture : ")
                    nb_porte = input("Entrez le nouveau nombre de portes de la voiture : ")
                    new_voiture = Voiture(marque, voiture_choice, couleur, 4, True, vitesse, nb_porte)
                    service.update_voiture(voiture, new_voiture)
                    print("La voiture a été mise à jour avec succès.")

        elif choice == "3":
            if len(service.get_metros()) == 0:
                print("Aucun métro n'est actuellement enregistré.")
            else:
                print("Voici la liste des métros enregistrés :")
                for metro in service.get_metros():
                    print(metro)

                metro_choice = input("Entrez le matricule du métro que vous souhaitez mettre à jour : ")
                metro = service.find_metro(metro_choice)

                if metro is None:
                    print("Le métro que vous avez choisi n'a pas été trouvé.")
                else:
                    print(f"Métro à mettre à jour : {metro}")
                    marque = input("Entrez la nouvelle marque du metro : ")
                    couleur = input("Entrez la nouvelle couleur du metro : ")
                    vitesse = input("Entrez la nouvelle vitesse du metro : ")
                    ligne = input("Entrez la nouvelle ligne du métro : ")
                    new_metro = Metro(marque, voiture_choice, couleur, 12, True, vitesse, ligne)
                    service.update_metro(voiture, new_voiture)
                    print("La voiture a été mise à jour avec succès.")
        elif choice == "4":
            choix = input(
                "Veuillez choisir le type de véhicules que vous voulez supprimer (motos, voitures ou metros): ")
            if choix == "motos":
                motos = self.service.motos
                matricule = input("Veuillez saisir le matricule de la moto à supprimer: ")
                vehicule = service.find_moto(matricule)
            elif choix == "voitures":
                voitures = self.service.voitures
                matricule = input("Veuillez saisir le matricule de la voiture à supprimer: ")
                vehicule = service.find_voiture(matricule)
            elif choix == "metros":
                metros = self.service.metros
                matricule = input("Veuillez saisir le matricule du métro à supprimer: ")
                vehicule = service.find_metro(matricule)
            else:
                print("Choix invalide.")

            if not vehicule:
                print("Le véhicule avec le matricule {} n'existe pas dans la liste {}.")
            elif choix == "motos":
                service.delete_moto(vehicule)
            elif choix == "voitures":
                service.delete_voiture(vehicule)
            elif choix == "metros":
                service.delete_metro(vehicule)