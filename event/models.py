from enum import unique
from django.db import models
from django.db.models.deletion import CASCADE
from account.models import Account

class Event(models.Model):
    creator = models.ForeignKey(Account, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.event_name 

class EventParticipant(models.Model):
    user =  models.ForeignKey(Account, on_delete=models.CASCADE)
    event =  models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Meeting(models.Model):
    creator = models.ForeignKey(Account, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    meeting_name = models.CharField(max_length=100, unique=True)
    meeting_date = models.DateTimeField()

    def __str__(self):
        return f"{self.meeting_name} by {self.creator}"


class Invitation(models.Model):
    STATUS_TYPE = (
        ('pennding', 'pennding'),
        ('accept', 'accepted'),
        ('decline', 'declined'),
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    invitee = models.ForeignKey(Account, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=STATUS_TYPE, default=STATUS_TYPE[0][0])
    

    def __str__(self):
        return str(self.invitee)



class MeetingScheduled(models.Model):
    attendee = models.ForeignKey(Account, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.attendee} {self.meeting}" 
