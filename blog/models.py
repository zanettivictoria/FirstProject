from django.db import models
from django.utils import timezone

class Post(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    texto = models.TextField(blank=True, null=True)
    criar_data = models.DateTimeField(default=timezone.now)
    publicar_data = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publicar_data = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo