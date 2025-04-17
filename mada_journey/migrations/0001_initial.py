# Generated by Django 5.2 on 2025-04-17 07:03

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=200)),
                ('contenu', models.TextField()),
                ('date_publication', models.DateTimeField(default=django.utils.timezone.now)),
                ('auteur', models.CharField(max_length=100)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('tags', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Capacite',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('nombre_places', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('region', models.CharField(max_length=100)),
                ('pays', models.CharField(default='Madagascar', max_length=100)),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=255)),
                ('reponse', models.TextField()),
                ('categorie', models.CharField(blank=True, max_length=100, null=True)),
                ('order_affichage', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['order_affichage'],
            },
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('date_naissance', models.DateField()),
                ('specialite', models.CharField(max_length=100)),
                ('langues', models.JSONField()),
                ('biographie', models.TextField(blank=True, null=True)),
                ('photo_url', models.URLField(blank=True, null=True)),
                ('disponibilite', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Saison',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100, unique=True)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeVehicule',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('role', models.CharField(choices=[('CLIENT', 'Client'), ('ADMIN', 'Admin'), ('GUIDE', 'Guide'), ('COMMERCIAL', 'Commercial')], default='CLIENT', max_length=20)),
                ('date_inscription', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BlogCommentaire',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('contenu', models.TextField()),
                ('date_commentaire', models.DateTimeField(default=django.utils.timezone.now)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='mada_journey.blog')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires_blog', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Circuit',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('duree', models.IntegerField(help_text='Durée en jours')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('difficulte', models.CharField(choices=[('FACILE', 'Facile'), ('MOYEN', 'Moyen'), ('DIFFICILE', 'Difficile')], default='FACILE', max_length=10)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='circuits', to='mada_journey.destination')),
                ('saison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='circuits', to='mada_journey.saison')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=20)),
                ('sujet', models.CharField(max_length=200)),
                ('contenu', models.TextField()),
                ('date_envoi', models.DateTimeField(default=django.utils.timezone.now)),
                ('lu', models.BooleanField(default=False)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PointInteret',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image_url', models.URLField(blank=True, null=True)),
                ('circuit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points_interet', to='mada_journey.circuit')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('immatriculation', models.CharField(max_length=20, unique=True)),
                ('marque', models.CharField(max_length=100)),
                ('modele', models.CharField(max_length=100)),
                ('annee', models.IntegerField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('etat', models.CharField(choices=[('DISPONIBLE', 'Disponible'), ('RESERVE', 'Réservé'), ('MAINTENANCE', 'En maintenance')], default='DISPONIBLE', max_length=20)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('capacite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicules', to='mada_journey.capacite')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicules', to='mada_journey.typevehicule')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('date_reservation', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_depart', models.DateTimeField()),
                ('statut', models.CharField(choices=[('EN_ATTENTE', 'En attente'), ('CONFIRMEE', 'Confirmée'), ('ANNULEE', 'Annulée'), ('TERMINEE', 'Terminée')], default='EN_ATTENTE', max_length=20)),
                ('duree', models.IntegerField()),
                ('nombre_personnes', models.IntegerField()),
                ('hebergement', models.CharField(choices=[('STANDARD', 'Standard'), ('CONFORT', 'Confort'), ('LUXE', 'Luxe')], default='STANDARD', max_length=20)),
                ('activite', models.CharField(choices=[('RANDONNEE', 'Randonnée'), ('PLAGE', 'Plage'), ('SAFARI', 'Safari'), ('PLONFEE', 'Plongée'), ('CULTURE', 'Culture'), ('GASTRONOMIE', 'Gastronomie')], default='RANDONNEE', max_length=20)),
                ('budget', models.CharField(blank=True, max_length=100, null=True)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=20)),
                ('commentaire', models.TextField(blank=True, null=True)),
                ('circuit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='mada_journey.circuit')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL)),
                ('vehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='mada_journey.vehicule')),
            ],
        ),
    ]
