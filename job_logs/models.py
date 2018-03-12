"""Models in django."""

from django.db import models


# Create your models here.
class Topic(models.Model):
    """Topic the user learns about."""

    company = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string of the model."""
        return self.text
