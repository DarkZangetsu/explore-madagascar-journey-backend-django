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
        fields = "__all__"

class DestinationType(DjangoObjectType):
    class Meta:
        model = Destination
        fields = "__all__"

class SaisonType(DjangoObjectType):
    class Meta:
        model = Saison
        fields = "__all__"

class CircuitType(DjangoObjectType):
    class Meta:
        model = Circuit
        fields = "__all__"

class PointInteretType(DjangoObjectType):
    class Meta:
        model = PointInteret
        fields = "__all__"

class TypeVehiculeType(DjangoObjectType):
    class Meta:
        model = TypeVehicule
        fields = "__all__"

class CapaciteType(DjangoObjectType):
    class Meta:
        model = Capacite
        fields = "__all__"

class VehiculeType(DjangoObjectType):
    class Meta:
        model = Vehicule
        fields = "__all__"

class ReservationType(DjangoObjectType):
    class Meta:
        model = Reservation
        fields = "__all__"

class GuideType(DjangoObjectType):
    class Meta:
        model = Guide
        fields = "__all__"

class MessageType(DjangoObjectType):
    class Meta:
        model = Message
        fields = "__all__"

class BlogType(DjangoObjectType):
    class Meta:
        model = Blog
        fields = "__all__"

class BlogCommentaireType(DjangoObjectType):
    class Meta:
        model = BlogCommentaire
        fields = "__all__"

class FaqType(DjangoObjectType):
    class Meta:
        model = Faq
        fields = "__all__"