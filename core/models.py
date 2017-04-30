from django.db import models

class Veiculo(models.Model):
    placa = models.CharField('placa', max_length=20, unique=True)
    tipo = models.CharField('tipo', max_length=20, blank=True)
    modelo = models.CharField('modelo', max_length=20, blank=True)
    id_cliente = models.IntegerField('id_cliente')

    class Meta:
        ordering = ['placa']
        verbose_name = 'veiculo'
        verbose_name_plural = 'veiculos'

    def __str__(self):
        return self.placa


class Cliente(models.Model):
    nome = models.CharField('nome', max_length=20)
    end = models.CharField('end', max_length=20, blank=True)
    tel = models.CharField('tel', max_length=20, blank=True)


    class Meta:
        ordering = ['nome']
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return self.nome


class Servicos(models.Model):
    servico = models.CharField('serviço', max_length=20)
    valor = models.DecimalField('valor', max_digits=5, decimal_places=2)
    id_cliente = models.IntegerField('id_cliente')
    id_veiculo = models.IntegerField('id_veiculos')

    class Meta:
        ordering = ['servico']
        verbose_name = 'serviço'
        verbose_name_plural = 'serviços'

    def __str__(self):
        return self.servico
