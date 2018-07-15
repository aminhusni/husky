#Amin Husni - 2018
from django.db import models

class Supervisor(models.Model):

    CLEANER = "CL"
    ADMIN = "AD"
    SUPERVISOR_CHOICES = (
        (CLEANER, 'Cleaner'), 
        (ADMIN, 'Admin'),
    )

    supervisor = models.IntegerField()
    supervisor_type = models.CharField(max_length=2, choices=SUPERVISOR_CHOICES, default=CLEANER,)
    name = models.TextField(max_length=100)
    authorization_token = models.TextField(max_length=100, default=None, blank=True)
    authorization_expire = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        final = str(self.supervisor) + " - " + self.name
        return str(final)


class Checklist(models.Model):

    employee_number = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    location_id = models.TextField(max_length=100)
    
    
    def __str__(self):
        return str(self.created)


class Check_item(models.Model):

    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    floor = models.BooleanField("Floor", default=False)
    smell = models.BooleanField("Smell", default=False)
    wall = models.BooleanField("Wall", default=False)
    dustbin = models.BooleanField("Dustbin", default=False)
    toilet_bowl = models.BooleanField("Toilet bowl", default=False)
    urinal_bowl = models.BooleanField("Urinal bowl", default=False)
    wash_basin = models.BooleanField("Wash basin", default=False)
    mirror = models.BooleanField("Mirror", default=False)
    tissue = models.BooleanField("Tissue", default=False)
    handsoap = models.BooleanField("Handsoap", default=False)

    def __str__(self):
        date = Checklist.objects.get(created=self.checklist.created)
        date = date.created
        return str(date)


