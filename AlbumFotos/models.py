from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver  
from django.urls import reverse


# Create your models here.
class Categoria(models.Model):
        """ Categorias para clasificar las fotos """
        nombre = models.CharField(max_length=50)
        def __str__(self):
            return self.nombre 

class Foto(models.Model):
        """ Fotos del album """
        titulo = models.CharField(max_length=70)
        foto = models.ImageField(upload_to='foto/')
        pub_fecha = models.DateField(auto_now_add=True)
        favorita = models.BooleanField(default=False)
        comentario = models.CharField(max_length=200, blank=True)
        categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True, blank=True)
        def __str__(self):
            return self.titulo
        def get_absolute_url(self):
            return reverse('foto-list')
@receiver(post_delete, sender=Foto)
def eliminar_foto(sender, instance, **kwargs):
        instance.foto.delete(False)



     
