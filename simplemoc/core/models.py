from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.TextField('Nome', max_length=100)
    description = models.TextField('Descrição', max_length=250)
    created_at = models.DateTimeField('criado em', auto_now_add=True, blank=True, null=True)
    status = models.TextField('Estatos', blank=True, null=True)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        ordering = ['name']

