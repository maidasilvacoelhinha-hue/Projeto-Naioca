from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    # Caminho da imagem na pasta static
    imagem = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Pedido(models.Model):

    FORMAS = [
        ("PIX", "PIX"),
        ("CARTAO", "Cartão"),
        ("DINHEIRO", "Dinheiro"),
    ]

    STATUS = [
        ("RECEBIDO", "Pedido recebido"),
        ("PREPARANDO", "Preparando"),
        ("ENTREGA", "Saiu para entrega"),
        ("FINALIZADO", "Entregue"),
    ]


    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)

    forma_pagamento = models.CharField(
        max_length=15,
        choices=FORMAS
    )

    total = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    
    

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id}"


class ItemPedido(models.Model):

    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE
    )

    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE
    )

    quantidade = models.PositiveIntegerField()

    subtotal = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )