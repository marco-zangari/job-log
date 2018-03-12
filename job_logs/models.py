"""Models in django."""

from django.db import models


# Create your models here.
class Topic(models.Model):
    """Topic the user learns about."""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about the company."""

    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """."""

        verbose_name_plural = 'entries'

    def __str__(self):
        """Return string representation of model."""
        return self.text[:50] + "..."
