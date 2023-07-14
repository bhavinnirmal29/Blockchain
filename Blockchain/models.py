from django.db import models

# Create your models here.
class Block(models.Model):
    index = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.TextField()
    previous_hash = models.CharField(max_length=64)
    hash = models.CharField(max_length=64)

    def __str__(self):
        return f"Block {self.index}"


class Blockchain(models.Model):
    name = models.CharField(max_length=100)
    blocks = models.ManyToManyField(Block)

    def __str__(self):
        return self.name