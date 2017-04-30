from django.contrib import admin
from .models import Cliente, Veiculo, Servicos
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Veiculo)
admin.site.register(Servicos)