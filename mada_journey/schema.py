from mada_journey.models import Faq
from .djangoObjectType import BlogCommentaireType, BlogType, CapaciteType, CircuitType, DestinationType, FaqType, GuideType, MessageType, PointInteretType, ReservationType, SaisonType, TypeVehiculeType, UtilisateurType, VehiculeType
from .mutation import CreateBlogMutation, CreateCircuitMutation, CreateDestinationMutation, CreateFaqMutation, CreatePointInteretMutation, CreateReservationMutation, CreateSaisonMutation, CreateUtilisateurMutation, CreateVehiculeMutation, DeleteBlogMutation, DeleteCircuitMutation, DeleteDestinationMutation, DeleteFaqMutation, DeletePointInteretMutation, DeleteReservationMutation, DeleteSaisonMutation, DeleteUtilisateurMutation, DeleteVehiculeMutation, UpdateBlogMutation, UpdateCircuitMutation, UpdateDestinationMutation, UpdateFaqMutation, UpdatePointInteretMutation, UpdateReservationMutation, UpdateSaisonMutation, UpdateUtilisateurMutation, UpdateVehiculeMutation
import graphene

class Query(graphene.ObjectType):
    utilisateur = graphene.Field(UtilisateurType)
    destination = graphene.Field(DestinationType)
    saison = graphene.Field(SaisonType)
    circuit = graphene.Field(CircuitType)
    point_interet = graphene.Field(PointInteretType)
    type_vehicule = graphene.Field(TypeVehiculeType)
    capacite = graphene.Field(CapaciteType)
    vehicule = graphene.Field(VehiculeType)
    reservation = graphene.Field(ReservationType)
    guide = graphene.Field(GuideType)
    message = graphene.Field(MessageType)
    blog = graphene.Field(BlogType)
    blog_commentaire = graphene.Field(BlogCommentaireType)
   
    all_utilisateurs = graphene.List(UtilisateurType)
    all_destinations = graphene.List(DestinationType)
    all_saisons = graphene.List(SaisonType)
    all_circuits = graphene.List(CircuitType)
    all_points_interet = graphene.List(PointInteretType)
    all_types_vehicule = graphene.List(TypeVehiculeType)
    all_capacites = graphene.List(CapaciteType)
    all_vehicules = graphene.List(VehiculeType)
    all_reservations = graphene.List(ReservationType)
    all_guides = graphene.List(GuideType)
    all_messages = graphene.List(MessageType)
    all_blogs = graphene.List(BlogType)
    all_blog_commentaires = graphene.List(BlogCommentaireType)

    # Faqs
    faq = graphene.Field(FaqType, id=graphene.String(required=True))
    all_faqs = graphene.List(FaqType)
    def resolve_faq (self,info, id):
        return Faq.objects.get(id=id)
    def resolve_all_faqs(self, info):
        return Faq.objects.all()


# Mutation
class Mutation(graphene.ObjectType):
    # Destination
    create_destination = CreateDestinationMutation.Field()
    update_destination = UpdateDestinationMutation.Field()
    delete_destination = DeleteDestinationMutation.Field()
    
    # Saison
    create_saison = CreateSaisonMutation.Field()
    update_saison = UpdateSaisonMutation.Field()
    delete_saison = DeleteSaisonMutation.Field()
    
    # Circuit
    create_circuit = CreateCircuitMutation.Field()
    update_circuit = UpdateCircuitMutation.Field()
    delete_circuit = DeleteCircuitMutation.Field()
    
    # Point d'intérêt
    create_point_interet = CreatePointInteretMutation.Field()
    update_point_interet = UpdatePointInteretMutation.Field()
    delete_point_interet = DeletePointInteretMutation.Field()
    
    # Réservation
    create_reservation = CreateReservationMutation.Field()
    update_reservation = UpdateReservationMutation.Field()
    delete_reservation = DeleteReservationMutation.Field()
    
    # Utilisateur
    create_utilisateur = CreateUtilisateurMutation.Field()
    update_utilisateur = UpdateUtilisateurMutation.Field()
    delete_utilisateur = DeleteUtilisateurMutation.Field()
    
    # Blog
    create_blog = CreateBlogMutation.Field()
    update_blog = UpdateBlogMutation.Field()
    delete_blog = DeleteBlogMutation.Field()
    
    # Véhicule
    create_vehicule = CreateVehiculeMutation.Field()
    update_vehicule = UpdateVehiculeMutation.Field()
    delete_vehicule = DeleteVehiculeMutation.Field()

    #faq
    create_faq = CreateFaqMutation.Field()
    update_faq = UpdateFaqMutation.Field()
    delete_faq = DeleteFaqMutation.Field()

# Schéma
schema = graphene.Schema(query=Query, mutation=Mutation)