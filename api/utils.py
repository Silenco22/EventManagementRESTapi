from event.models import Meeting
from api.serializers import CreateInvitationSerializer
from rest_framework import status



def autoCreateInvtitaions(data):
    meeting = Meeting.objects.get(meeting_name=data['meeting_name'])
    meeting_id = meeting.id
    event_name = data['event_name']
    users = data['array']
    users = list(users.split(" "))
    ser_data = {}
    http_status = ''
    for user in users:
        #to do: check if user is in the right event and if not do something
        serializer = CreateInvitationSerializer(data={'meeting_name': meeting_id, 
                                                        'invite_name': user,
                                                        'event_name':event_name
                                                        })
        if serializer.is_valid():
            serializer.save()
            ser_data['response'] = 'successfully created meeting and invitations'
            http_status = status.HTTP_200_OK
        else:
            ser_data = serializer.errors
            http_status = status.HTTP_400_BAD_REQUEST
    return ser_data, http_status
    