import graphene
from graphene_django import DjangoObjectType

from .models import (
    Utilisateur, Destination, Saison, Circuit, PointInteret,
    TypeVehicule, Capacite, Vehicule, Reservation, Guide,
    Message, Blog, BlogCommentaire, Faq
)


class UtilisateurType(DjangoObjectType):
    class Meta:
        model = Utilisateur
        filter_fields = {
            'email': ['exact', 'icontains'],
            'nom': ['exact', 'icontains'],
            'prenom': ['exact', 'icontains'],
            'role': ['exact'],
            'date_inscription': ['gte', 'lte'],
        }
        interfaces = (graphene.relay.Node,)
        exclude = ('password',)

class DestinationType(DjangoObjectType):
    class Meta:
        model = Destination
        filter_fields = {
            'nom': ['exact', 'icontains'],
            'region': ['exact', 'icontains'],
            'pays': ['exact', 'icontains'],
        }
        interfaces = (graphene.relay.Node,)

class SaisonType(DjangoObjectType):
    class Meta:
        model = Saison
        filter_fields = {
            'nom': ['exact', 'icontains'],
            'date_debut': ['gte', 'lte'],
            'date_fin': ['gte', 'lte'],
        }
        interfaces = (graphene.relay.Node,)

class CircuitType(DjangoObjectType):
    class Meta:
        model = Circuit
        filter_fields = {
            'titre': ['exact', 'icontains'],
            'duree': ['exact', 'gte', 'lte'],
            'prix': ['exact', 'gte', 'lte'],
            'difficulte': ['exact'],
            'destination__nom': ['exact', 'icontains'],
            'saison__nom': ['exact', 'icontains'],
        }
        interfaces = (graphene.relay.Node,)

class PointInteretType(DjangoObjectType):
    class Meta:
        model = PointInteret
        filter_fields = {
            'nom': ['exact', 'icontains'],
            'circuit__titre': ['exact', 'icontains'],
        }
        interfaces = (graphene.relay.Node,)

class TypeVehiculeType(DjangoObjectType):
    class Meta:
        model = TypeVehicule
        filter_fields = {
            'libelle': ['exact', 'icontains'],
        }
        interfaces = (graphene.relay.Node,)

class CapaciteType(DjangoObjectType):
    class Meta:
        model = Capacite
        filter_fields = {
            'nombre_places': ['exact', 'gte', 'lte'],
        }
        interfaces = (graphene.relay.Node,)

class VehiculeType(DjangoObjectType):
    class Meta:
        model = Vehicule
        filter_fields = {
            'immatriculation': ['exact', 'icontains'],
            'marque': ['exact', 'icontains'],
            'modele': ['exact', 'icontains'],
            'annee': ['exact', 'gte', 'lte'],
            'prix': ['exact', 'gte', 'lte'],
            'etat': ['exact'],
        }
        interfaces = (graphene.relay.Node,)

class ReservationType(DjangoObjectType):
    class Meta:
        model = Reservation
        filter_fields = {
            'statut': ['exact'],
            'date_reservation': ['gte', 'lte'],
            'date_depart': ['gte', 'lte'],
            'circuit__titre': ['exact', 'icontains'],
            'utilisateur__email': ['exact', 'icontains'],
        }
        interfaces = (graphene.relay.Node,)

class GuideType(DjangoObjectType):
    class Meta:
        model = Guide
        filter_fields = {
            'nom': ['exact', 'icontains'],
            'prenom': ['exact', 'icontains'],
            'specialite': ['exact', 'icontains'],
            'disponibilite': ['exact'],
        }
        interfaces = (graphene.relay.Node,)

class MessageType(DjangoObjectType):
    class Meta:
        model = Message
        filter_fields = {
            'sujet': ['exact', 'icontains'],
            'date_envoi': ['gte', 'lte'],
            'lu': ['exact'],
        }
        interfaces = (graphene.relay.Node,)

class BlogType(DjangoObjectType):
    class Meta:
        model = Blog
        filter_fields = {
            'titre': ['exact', 'icontains'],
            'auteur': ['exact', 'icontains'],
            'date_publication': ['gte', 'lte'],
        }
        interfaces = (graphene.relay.Node,)

class BlogCommentaireType(DjangoObjectType):
    class Meta:
        model = BlogCommentaire
        filter_fields = {
            'blog__titre': ['exact', 'icontains'],
            'utilisateur__email': ['exact', 'icontains'],
            'date_commentaire': ['gte', 'lte'],
        }
        interfaces = (graphene.relay.Node,)

class FaqType(DjangoObjectType):
    class Meta:
        model = Faq
        filter_fields = {
            'question': ['exact', 'icontains'],
            'categorie': ['exact', 'icontains'],
            'active': ['exact'],
        }
        interfaces = (graphene.relay.Node,)