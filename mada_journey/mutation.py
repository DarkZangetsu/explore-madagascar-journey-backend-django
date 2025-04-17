import graphene

from graphql_relay import from_global_id

from .djangoObjectType import BlogType, CircuitType, DestinationType, FaqType, PointInteretType, ReservationType, SaisonType, UtilisateurType, VehiculeType

from .models import (
    Faq, Utilisateur, Destination, Saison, Circuit, PointInteret,
     Vehicule, Reservation, Blog,
)

# Destination
class CreateDestinationMutation(graphene.Mutation):
    class Arguments:
        nom = graphene.String(required=True)
        description = graphene.String(required=True)
        region = graphene.String(required=True)
        pays = graphene.String(default_value="Madagascar")
        image_url = graphene.String()

    destination = graphene.Field(DestinationType)

    def mutate(self, info, nom, description, region, pays="Madagascar", image_url=None):
        destination = Destination.objects.create(
            nom=nom,
            description=description,
            region=region,
            pays=pays,
            image_url=image_url
        )
        return CreateDestinationMutation(destination=destination)

class UpdateDestinationMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        nom = graphene.String()
        description = graphene.String()
        region = graphene.String()
        pays = graphene.String()
        image_url = graphene.String()

    destination = graphene.Field(DestinationType)

    def mutate(self, info, id, **kwargs):
        _, destination_id = from_global_id(id)
        Destination.objects.filter(id=destination_id).update(**kwargs)
        destination = Destination.objects.get(id=destination_id)
        return UpdateDestinationMutation(destination=destination)

class DeleteDestinationMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        _, destination_id = from_global_id(id)
        try:
            Destination.objects.get(id=destination_id).delete()
            success = True
        except Destination.DoesNotExist:
            success = False
        return DeleteDestinationMutation(success=success)

# Saison
class CreateSaisonMutation(graphene.Mutation):
    class Arguments:
        nom = graphene.String(required=True)
        date_debut = graphene.Date(required=True)
        date_fin = graphene.Date(required=True)

    saison = graphene.Field(SaisonType)

    def mutate(self, info, nom, date_debut, date_fin):
        saison = Saison.objects.create(
            nom=nom,
            date_debut=date_debut,
            date_fin=date_fin
        )
        return CreateSaisonMutation(saison=saison)

class UpdateSaisonMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        nom = graphene.String()
        date_debut = graphene.Date()
        date_fin = graphene.Date()

    saison = graphene.Field(SaisonType)

    def mutate(self, info, id, **kwargs):
        _, saison_id = from_global_id(id)
        Saison.objects.filter(id=saison_id).update(**kwargs)
        saison = Saison.objects.get(id=saison_id)
        return UpdateSaisonMutation(saison=saison)

class DeleteSaisonMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        _, saison_id = from_global_id(id)
        try:
            Saison.objects.get(id=saison_id).delete()
            success = True
        except Saison.DoesNotExist:
            success = False
        return DeleteSaisonMutation(success=success)

# Circuit
class CreateCircuitMutation(graphene.Mutation):
    class Arguments:
        titre = graphene.String(required=True)
        description = graphene.String(required=True)
        duree = graphene.Int(required=True)
        prix = graphene.Float(required=True)
        image_url = graphene.String()
        difficulte = graphene.String()
        destination_id = graphene.ID(required=True)
        saison_id = graphene.ID(required=True)

    circuit = graphene.Field(CircuitType)

    def mutate(self, info, titre, description, duree, prix, destination_id, saison_id, image_url=None, difficulte="FACILE"):
        _, destination_db_id = from_global_id(destination_id)
        _, saison_db_id = from_global_id(saison_id)
        
        circuit = Circuit.objects.create(
            titre=titre,
            description=description,
            duree=duree,
            prix=prix,
            image_url=image_url,
            difficulte=difficulte,
            destination_id=destination_db_id,
            saison_id=saison_db_id
        )
        return CreateCircuitMutation(circuit=circuit)

class UpdateCircuitMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        titre = graphene.String()
        description = graphene.String()
        duree = graphene.Int()
        prix = graphene.Float()
        image_url = graphene.String()
        difficulte = graphene.String()
        destination_id = graphene.ID()
        saison_id = graphene.ID()

    circuit = graphene.Field(CircuitType)

    def mutate(self, info, id, **kwargs):
        _, circuit_id = from_global_id(id)
        
        # Transformation des ID GraphQL en ID de base de données
        if 'destination_id' in kwargs:
            _, kwargs['destination_id'] = from_global_id(kwargs['destination_id'])
        if 'saison_id' in kwargs:
            _, kwargs['saison_id'] = from_global_id(kwargs['saison_id'])
            
        Circuit.objects.filter(id=circuit_id).update(**kwargs)
        circuit = Circuit.objects.get(id=circuit_id)
        return UpdateCircuitMutation(circuit=circuit)

class DeleteCircuitMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        _, circuit_id = from_global_id(id)
        try:
            Circuit.objects.get(id=circuit_id).delete()
            success = True
        except Circuit.DoesNotExist:
            success = False
        return DeleteCircuitMutation(success=success)

# Point d'intérêt
class CreatePointInteretMutation(graphene.Mutation):
    class Arguments:
        nom = graphene.String(required=True)
        description = graphene.String(required=True)
        image_url = graphene.String()
        circuit_id = graphene.ID(required=True)

    point_interet = graphene.Field(PointInteretType)

    def mutate(self, info, nom, description, circuit_id, image_url=None):
        _, circuit_db_id = from_global_id(circuit_id)
        
        point_interet = PointInteret.objects.create(
            nom=nom,
            description=description,
            image_url=image_url,
            circuit_id=circuit_db_id
        )
        return CreatePointInteretMutation(point_interet=point_interet)

class UpdatePointInteretMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        nom = graphene.String()
        description = graphene.String()
        image_url = graphene.String()
        circuit_id = graphene.ID()

    point_interet = graphene.Field(PointInteretType)

    def mutate(self, info, id, **kwargs):
        _, point_id = from_global_id(id)
        
        if 'circuit_id' in kwargs:
            _, kwargs['circuit_id'] = from_global_id(kwargs['circuit_id'])
            
        PointInteret.objects.filter(id=point_id).update(**kwargs)
        point_interet = PointInteret.objects.get(id=point_id)
        return UpdatePointInteretMutation(point_interet=point_interet)

class DeletePointInteretMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        _, point_id = from_global_id(id)
        try:
            PointInteret.objects.get(id=point_id).delete()
            success = True
        except PointInteret.DoesNotExist:
            success = False
        return DeletePointInteretMutation(success=success)

# Réservation
class CreateReservationMutation(graphene.Mutation):
    class Arguments:
        utilisateur_id = graphene.ID(required=True)
        circuit_id = graphene.ID(required=True)
        vehicule_id = graphene.ID(required=True)
        date_depart = graphene.DateTime(required=True)
        duree = graphene.Int(required=True)
        nombre_personnes = graphene.Int(required=True)
        hebergement = graphene.String()
        activite = graphene.String()
        budget = graphene.String()
        nom = graphene.String(required=True)
        prenom = graphene.String(required=True)
        email = graphene.String(required=True)
        telephone = graphene.String(required=True)
        commentaire = graphene.String()

    reservation = graphene.Field(ReservationType)

    def mutate(self, info, utilisateur_id, circuit_id, vehicule_id, date_depart, duree, 
               nombre_personnes, nom, prenom, email, telephone, hebergement="STANDARD", 
               activite="RANDONNEE", budget=None, commentaire=None):
        
        _, user_db_id = from_global_id(utilisateur_id)
        _, circuit_db_id = from_global_id(circuit_id)
        _, vehicule_db_id = from_global_id(vehicule_id)
        
        reservation = Reservation.objects.create(
            utilisateur_id=user_db_id,
            circuit_id=circuit_db_id,
            vehicule_id=vehicule_db_id,
            date_depart=date_depart,
            duree=duree,
            nombre_personnes=nombre_personnes,
            hebergement=hebergement,
            activite=activite,
            budget=budget,
            nom=nom,
            prenom=prenom,
            email=email,
            telephone=telephone,
            commentaire=commentaire
        )
        return CreateReservationMutation(reservation=reservation)

class UpdateReservationMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        statut = graphene.String()
        date_depart = graphene.DateTime()
        duree = graphene.Int()
        nombre_personnes = graphene.Int()
        hebergement = graphene.String()
        activite = graphene.String()
        budget = graphene.String()
        commentaire = graphene.String()

    reservation = graphene.Field(ReservationType)

    def mutate(self, info, id, **kwargs):
        _, reservation_id = from_global_id(id)
        Reservation.objects.filter(id=reservation_id).update(**kwargs)
        reservation = Reservation.objects.get(id=reservation_id)
        return UpdateReservationMutation(reservation=reservation)

class DeleteReservationMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        _, reservation_id = from_global_id(id)
        try:
            Reservation.objects.get(id=reservation_id).delete()
            success = True
        except Reservation.DoesNotExist:
            success = False
        return DeleteReservationMutation(success=success)

# Utilisateur
class CreateUtilisateurMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        nom = graphene.String(required=True)
        prenom = graphene.String(required=True)
        telephone = graphene.String()
        role = graphene.String()

    utilisateur = graphene.Field(UtilisateurType)

    def mutate(self, info, email, password, nom, prenom, telephone=None, role="CLIENT"):
        user = Utilisateur.objects.create_user(
            username=email,  # Django exige un username
            email=email,
            password=password,
            nom=nom,
            prenom=prenom,
            telephone=telephone,
            role=role
        )
        return CreateUtilisateurMutation(utilisateur=user)

class UpdateUtilisateurMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        email = graphene.String()
        nom = graphene.String()
        prenom = graphene.String()
        telephone = graphene.String()
        role = graphene.String()

    utilisateur = graphene.Field(UtilisateurType)

    def mutate(self, info, id, **kwargs):
        _, user_id = from_global_id(id)
        
        # Si l'email change, mettre à jour aussi username
        if 'email' in kwargs:
            kwargs['username'] = kwargs['email']
            
        Utilisateur.objects.filter(id=user_id).update(**kwargs)
        user = Utilisateur.objects.get(id=user_id)
        return UpdateUtilisateurMutation(utilisateur=user)

class DeleteUtilisateurMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        _, user_id = from_global_id(id)
        try:
            Utilisateur.objects.get(id=user_id).delete()
            success = True
        except Utilisateur.DoesNotExist:
            success = False
        return DeleteUtilisateurMutation(success=success)

# Blog
class CreateBlogMutation(graphene.Mutation):
    class Arguments:
        titre = graphene.String(required=True)
        contenu = graphene.String(required=True)
        auteur = graphene.String(required=True)
        image_url = graphene.String()
        tags = graphene.List(graphene.String)

    blog = graphene.Field(BlogType)

    def mutate(self, info, titre, contenu, auteur, image_url=None, tags=None):
        if tags is None:
            tags = []
            
        blog = Blog.objects.create(
            titre=titre,
            contenu=contenu,
            auteur=auteur,
            image_url=image_url,
            tags=tags
        )
        return CreateBlogMutation(blog=blog)

class UpdateBlogMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        titre = graphene.String()
        contenu = graphene.String()
        auteur = graphene.String()
        image_url = graphene.String()
        tags = graphene.List(graphene.String)

    blog = graphene.Field(BlogType)

    def mutate(self, info, id, **kwargs):
        _, blog_id = from_global_id(id)
        Blog.objects.filter(id=blog_id).update(**kwargs)
        blog = Blog.objects.get(id=blog_id)
        return UpdateBlogMutation(blog=blog)

class DeleteBlogMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        _, blog_id = from_global_id(id)
        try:
            Blog.objects.get(id=blog_id).delete()
            success = True
        except Blog.DoesNotExist:
            success = False
        return DeleteBlogMutation(success=success)

# Véhicule
class CreateVehiculeMutation(graphene.Mutation):
    class Arguments:
        immatriculation = graphene.String(required=True)
        marque = graphene.String(required=True)
        modele = graphene.String(required=True)
        annee = graphene.Int(required=True)
        type_vehicule_id = graphene.ID(required=True)
        capacite_id = graphene.ID(required=True)
        prix = graphene.Float(required=True)
        etat = graphene.String()
        image_url = graphene.String()

    vehicule = graphene.Field(VehiculeType)

    def mutate(self, info, immatriculation, marque, modele, annee, type_vehicule_id, 
               capacite_id, prix, etat="DISPONIBLE", image_url=None):
        
        _, type_db_id = from_global_id(type_vehicule_id)
        _, capacite_db_id = from_global_id(capacite_id)
        
        vehicule = Vehicule.objects.create(
            immatriculation=immatriculation,
            marque=marque,
            modele=modele,
            annee=annee,
            type_id=type_db_id,
            capacite_id=capacite_db_id,
            prix=prix,
            etat=etat,
            image_url=image_url
        )
        return CreateVehiculeMutation(vehicule=vehicule)

class UpdateVehiculeMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        immatriculation = graphene.String()
        marque = graphene.String()
        modele = graphene.String()
        annee = graphene.Int()
        type_vehicule_id = graphene.ID()
        capacite_id = graphene.ID()
        prix = graphene.Float()
        etat = graphene.String()
        image_url = graphene.String()

    vehicule = graphene.Field(VehiculeType)

    def mutate(self, info, id, **kwargs):
        _, vehicule_id = from_global_id(id)
        
        # Conversion des IDs
        if 'type_vehicule_id' in kwargs:
            _, kwargs['type_id'] = from_global_id(kwargs['type_vehicule_id'])
            del kwargs['type_vehicule_id']
            
        if 'capacite_id' in kwargs:
            _, kwargs['capacite_id'] = from_global_id(kwargs['capacite_id'])
            
        Vehicule.objects.filter(id=vehicule_id).update(**kwargs)
        vehicule = Vehicule.objects.get(id=vehicule_id)
        return UpdateVehiculeMutation(vehicule=vehicule)

class DeleteVehiculeMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        _, vehicule_id = from_global_id(id)
        try:
            Vehicule.objects.get(id=vehicule_id).delete()
            success = True
        except Vehicule.DoesNotExist:
            success = False
        return DeleteVehiculeMutation(success=success)

#FAQ
class CreateFaqMutation(graphene.Mutation):
    class Arguments:
        question = graphene.String(required=True)
        reponse = graphene.String(required=True)
        categorie = graphene.String()
        order_affichage = graphene.Int(default_value=0)
        active = graphene.Boolean(default_value=True)

    faq = graphene.Field(FaqType)

    def mutate(self, info, question, reponse, categorie=None, order_affichage=0, active=True):
        faq = Faq.objects.create(
            question=question,
            reponse=reponse,
            categorie=categorie,
            order_affichage=order_affichage,
            active=active
        )
        return CreateFaqMutation(faq=faq)

class UpdateFaqMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        question = graphene.String()
        reponse = graphene.String()
        categorie = graphene.String()
        order_affichage = graphene.Int()
        active = graphene.Boolean()

    faq = graphene.Field(FaqType)

    def mutate(self, info, id, **kwargs):
        try:
            # Imprimez l'ID pour déboguer
            print(f"ID reçu dans updateFaq: {id}")
            
            # Ne pas utiliser from_global_id si vos IDs sont des UUID standards
            faq_id = id
                
            # Vérifiez que l'objet existe
            faq = Faq.objects.get(id=faq_id)
            
            # Mise à jour des champs fournis
            if 'question' in kwargs:
                faq.question = kwargs['question']
            if 'reponse' in kwargs:
                faq.reponse = kwargs['reponse']
            if 'categorie' in kwargs:
                faq.categorie = kwargs['categorie']
            if 'order_affichage' in kwargs:
                faq.order_affichage = kwargs['order_affichage']
            if 'active' in kwargs:
                faq.active = kwargs['active']
                
            faq.save()
            return UpdateFaqMutation(faq=faq)
        except Faq.DoesNotExist:
            print(f"FAQ avec ID {faq_id} non trouvée")
            raise Exception(f"FAQ avec ID {faq_id} non trouvée")
        except Exception as e:
            print(f"Erreur inattendue: {str(e)}")
            raise Exception(f"Erreur inattendue: {str(e)}")

class DeleteFaqMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        try:
            # Imprimez l'ID pour déboguer
            print(f"ID reçu dans deleteFaq: {id}")
            
            # Ne pas utiliser from_global_id si vos IDs sont des UUID standards
            faq_id = id
                
            faq = Faq.objects.get(id=faq_id)
            faq.delete()
            return DeleteFaqMutation(success=True)
        except Faq.DoesNotExist:
            print(f"FAQ avec ID {faq_id} non trouvée")
            raise Exception(f"FAQ avec ID {faq_id} non trouvée")
        except Exception as e:
            print(f"Erreur inattendue: {str(e)}")
            raise Exception(f"Erreur inattendue: {str(e)}")