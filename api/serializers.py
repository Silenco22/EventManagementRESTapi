from rest_framework import serializers
from account.models import Account
from event.models import Event, EventParticipant, Invitation, Meeting, MeetingScheduled


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username','email','id']

class CreateUserSerializer(serializers.ModelSerializer):


    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
                'password': {'write_only': True},
        }	

    def	save(self):

        account = Account(
                    email=self.validated_data['email'],
                    username=self.validated_data['username']
                )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account

class CreateEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['pk','creator', 'event_name']

    

class EventParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventParticipant
        fields = ['user','event']

class CreateMeetingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Meeting
        fields = ['pk','creator','event', 'meeting_name','meeting_date']


class CreateInvitationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Invitation
        fields = ['event','meeting', 'invitee']

class StatusInvitationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Invitation
        fields = ['status']

class InvitationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invitation
        fields = ['id','event','meeting','invitee','status']

class ScheduleMeetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MeetingScheduled
        fields = ['attendee', 'meeting']