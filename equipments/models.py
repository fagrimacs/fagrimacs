from django.db import models
from accounts.models import CustomUser


class Implement(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    age = models.CharField(max_length=100)


    def __str__(self):
        return self.name

