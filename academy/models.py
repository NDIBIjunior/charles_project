from django.db import models

# Create your models here.

from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db.models import F

User = get_user_model()

class Formation(models.Model):
    CATEGORY_CHOICES = [
        ("pisciculture", "Pisciculture"),
        ("agriculture", "Agriculture"),
        ("elevage", "Élevage"),
        ("autres", "Autres"),
    ]

    title = models.CharField("Titre", max_length=255)
    description = models.TextField("Description", blank=True)
    category = models.CharField("Catégorie", max_length=32, choices=CATEGORY_CHOICES, default="autres")
    created_at = models.DateTimeField("Date de création", default=timezone.now)
    updated_at = models.DateTimeField("Dernière modification", auto_now=True)
    views = models.PositiveIntegerField("Nombre de vues", default=0)

    def __str__(self):
        return self.title

class FormationImage(models.Model):
    formation = models.ForeignKey(Formation, related_name="images", on_delete=models.CASCADE, blank=True)
    title = models.CharField("Nom image", max_length=150, blank=True)
    description = models.CharField("Description image", max_length=255, blank=True)
    image = models.ImageField("Fichier image", upload_to="formations/images/")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title or f"Image {self.pk}"

class FormationVideo(models.Model):
    formation = models.ForeignKey(Formation, related_name="videos", on_delete=models.CASCADE, blank=True)
    title = models.CharField("Titre", max_length=255)
    description = models.TextField("Description", blank=True)
    video = models.FileField("Fichier vidéo", upload_to="videos/")
    created_at = models.DateTimeField(default=timezone.now)
    views = models.PositiveIntegerField("Nombre de vues", default=0)

    def __str__(self):
        return self.title

class Video(models.Model):
    
    title = models.CharField("Titre", max_length=255)
    description = models.TextField("Description", blank=True)
    video = models.FileField("Fichier vidéo", upload_to="videos/")
    created_at = models.DateTimeField(default=timezone.now)
    views = models.PositiveIntegerField("Nombre de vues", default=0)

    def __str__(self):
        return self.title


class Image(models.Model):
     """Galerie générale pour les images n'appartenant pas a une formation"""
     title = models.CharField("Titre", max_length=150, blank=True)
     description = models.CharField("Description", max_length=255, blank=True)
     image = models.ImageField("Fichier image", upload_to="gallery/")
     created_at = models.DateTimeField(default=timezone.now)

     def __str__(self):
         return self.title or f"Gallery Image {self.pk}"

class Comment(models.Model):
    formation = models.ForeignKey(Formation, related_name="comments", on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    response = models.TextField(blank=True)
    content = models.TextField("Commentaire")
    email = models.EmailField("Email")
    is_admin = models.BooleanField("Commentaire admin", default=False)
    created_at = models.DateTimeField(default=timezone.now)
   
    def __str__(self):
        return f"{self.autor} - {self.content[:30]}"
