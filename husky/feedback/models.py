#Amin Husni - 2018
from django.db import models

# Create your models here.
class Feedback(models.Model):

    # Fields
    rating = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    location_id = models.TextField(max_length=100)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.created)


class Problem(models.Model):

    # Fields
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    clogged = models.BooleanField(default=False)
    toilet_paper = models.BooleanField(default=False)
    lighting = models.BooleanField(default=False)
    soap = models.BooleanField(default=False)
    hose = models.BooleanField(default=False)
    temperature = models.BooleanField(default=False)
    bowl = models.BooleanField(default=False)
    sink = models.BooleanField(default=False)
    smell = models.BooleanField(default=False)
    fault = models.BooleanField(default=False)


    def __str__(self):
        return str(self.feedback)