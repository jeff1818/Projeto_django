from django.db import models
from datetime import datetime

class Artigo(models.Model):
    class Meta:
        ordering = ('-publicacao',)
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField()

    def __unicode__(self):
        return self.titulo


