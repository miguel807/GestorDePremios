from django.contrib import admin
from .models import Premios,Obrass, Cronograma, Jurado
# Register your models here.
admin.site.register(Premios)
admin.site.register(Obrass)
admin.site.register( Cronograma)
admin.site.register( Jurado)