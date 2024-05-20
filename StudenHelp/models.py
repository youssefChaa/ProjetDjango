from django.db import models
from datetime import date
from django.views.generic import ListView
from django.contrib.auth.models import User
ts = (
    (1, 'ouvrier'),
    (2, 'technicien'),
    (3, 'PFE')
)
tp = (
    (0, 'offre'),
    (1, 'demmande')

)


class Poste(models.Model):
    image = models.ImageField(blank=True)
    type = models.IntegerField(default=0, choices=tp)
    date = models.DateTimeField(auto_now_add=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Image: {self.image}, Type: {self.type}, Date: {self.date}, Utilisateur: {self.uc}"

    class Meta:
        ordering = ['-date']


class Recommandation(Poste):
    text = models.CharField(max_length=255)

    def __str__(self):
        return f"Texte: {self.text}"


class Transport(Poste):
    depart = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    heure_dep = models.TimeField()
    nbre_sieges = models.IntegerField()
    contactinfo = models.CharField(max_length=255)

    def __str__(self):
        return f"Départ: {self.depart}, Destination: {self.destination}, Heure de départ: {self.heure_dep}, Nombre de sièges: {self.nbre_sieges}, Contact: {self.contactinfo}"


class Logement(Poste):
    localisation = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    contactinfo = models.CharField(max_length=255)

    def __str__(self):
        return f"Localisation: {self.localisation}, Description: {self.description}, Contact: {self.contactinfo}"


class Stage(Poste):
    typestg = models.IntegerField(default=1, choices=ts)
    societe = models.CharField(max_length=255)
    duree = models.IntegerField()
    sujet = models.CharField(max_length=255)
    contactinfo = models.CharField(max_length=255)
    specialite = models.CharField(max_length=255)

    def __str__(self):
        return f"Type: {self.typestg}, Société: {self.societe}, Durée: {self.duree}, Sujet: {self.sujet}, Contact: {self.contactinfo}, Spécialité: {self.specialite}"


class Evenement(Poste):
    intitule = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    lieu = models.CharField(max_length=255)
    contactinfo = models.CharField(max_length=255)

    def __str__(self):
        return f"Intitulé: {self.intitule}, Lieu: {self.lieu}, Description: {self.description}, Contact: {self.contactinfo}"


class EvenClub(Evenement):
    club = models.CharField(max_length=255)

    def __str__(self):
        return f"Club: {self.club}"


class EvenSocial(Evenement):
    prix = models.FloatField()

    def __str__(self):
        return f"Prix: {self.prix}"


class Reaction(models.Model):
    comment = models.TextField(max_length=50, default='')
    like = models.BooleanField(default=False)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Poste, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return f"Commentaire: {self.comment}, Like: {self.like}, Utilisateur: {self.users}"
