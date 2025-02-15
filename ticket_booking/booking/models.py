from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    purchaser_name = models.CharField(max_length=100)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.purchaser_name} - {self.event.name}"