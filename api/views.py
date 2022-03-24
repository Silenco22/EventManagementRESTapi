from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from api.serializers import ( 
	ScheduleMeetSerializer,
	UserSerializer, 
	CreateUserSerializer,
	CreateEventSerializer, 
	EventParticipantSerializer,
	CreateMeetingSerializer,
	CreateInvitationSerializer,
	InvitationSerializer,
	StatusInvitationSerializer,
	
)
from account.models import Account
from event.models import Event, Meeting, Invitation,EventParticipant

from api.utils import autoCreateInvtitaions

"""
All user authentication is disabled/commented.
"""



# Get all users 



@api_view(['POST', 'GET'])
def Users(request):
    # Create user
	if request.method == 'POST':
		data = {}
		serializer = CreateUserSerializer(data=request.data)

		if serializer.is_valid():
			account = serializer.save()
			data['response'] = 'successfully registered new user.'
			data['username'] = account.username
			data['pk'] = account.pk
			token = Token.objects.get(user=account).key # creating token for authentication
			data['token'] = token
			return Response(data=data, status=status.HTTP_201_CREATED)
		else:
			data = serializer.errors
		return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
	#Get all users
	elif request.method == 'GET':
		users = Account.objects.all() #query all users from database 
		serializer = UserSerializer(users, many=True)
		return Response(data=serializer.data, status=status.HTTP_200_OK)

# Create Event
@api_view(['POST','GET'])
# @permission_classes((IsAuthenticated,))
def Events(request):
	if request.method == 'POST':
		# Creating event
		data = {}
		serializer = CreateEventSerializer(data=request.data) #serializing data
		
		if serializer.is_valid(): # validating serilaizer
			serializer.save() # saving serializer 
			data['response'] = 'successfully created event'
		else:
			data = serializer.errors
			return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
		
		# Adding creator of the event to the event
		event = Event.objects.get(event_name=request.data['event_name'])
		event_pk = event.id
		creator_pk = request.data['creator']
		dict = {'user': creator_pk, 'event': event_pk}
		serializer = EventParticipantSerializer(data=dict)
		if serializer.is_valid():
			serializer.save()
			return Response(data=data, status=status.HTTP_201_CREATED)
		else:
			data = serializer.errors
		return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
	# Get all Events
	elif request.method == 'GET':
		events = Event.objects.all()
		serializer = CreateEventSerializer(events, many=True)
		return Response(data=serializer.data, status=status.HTTP_200_OK)



# Add participant to event
@api_view(['POST'])
def addParticipant(request):
	data = {}
	serializer = EventParticipantSerializer(data=request.data)
	# to do: dont allow to add same user multiple times
	if serializer.is_valid():
		serializer.save()
		data['response'] = 'successfully added participant'
		return Response(data=data, status=status.HTTP_200_OK)
	else:
		data = serializer.errors
	return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

# Get all the participants by event id
@api_view(['GET'])
def getParticipants(request, pk): #pk = id eventa
	users = EventParticipant.objects.filter(event=pk)
	serializer = EventParticipantSerializer(users, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)

# Create meeting
@api_view(['POST','GET'])
# @permission_classes((IsAuthenticated,))
def Meetings(request):
    
	if request.method == 'POST':
		event_participants =EventParticipant.objects.filter(event=request.data['event']) #query all event participants
		meetings_with_same_date = Meeting.objects.filter(meeting_date = request.data['meeting_date']) #query all objects with the same date created
		user = int(request.data['creator'])
		data = {}
		data['response'] = 'meeting with the same date exist or user is not in the event'
		try:
			string = request.data['string'] 
		except:
			string = None
		# if no meeting with the same date and meeting creator is in the event, create meeting:
		if not meetings_with_same_date:
			for participant in event_participants:
				if participant.user.id == user:
					user = request.data['creator']
					meeting_name = request.data['meeting_name']
					meeting_date = request.data['meeting_date']
					event = request.data['event']
					dict = {'creator': user,
							'meeting_name': meeting_name,
							'meeting_date':meeting_date,
							'event':event
							}
					serializer = CreateMeetingSerializer(data=dict)
					
					if serializer.is_valid():
						serializer.save()
						data['response'] = 'successfully created meeting'
					else:
						data = serializer.errors
						return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

					# optional filed: "string", with ids of users to invite to meeting 
					# autoCreateInvitaions() will auto create invitations
					# to do: dont allow auto creation of invitations for users who are not in the event
					if string:
						http_status = ''
						data, http_status = autoCreateInvtitaions(request.data) # auto creating invitations for user id in "string"
						return Response(data=data, status=http_status)
					return Response(data=data, status=status.HTTP_200_OK)

		return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'GET':
		meetings = Meeting.objects.all()
		serializer = CreateMeetingSerializer(meetings, many=True)
		return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT','DELETE'])
# @permission_classes((IsAuthenticated,))
def statusMeeting(request, pk):
	meeting = Meeting.objects.get(pk=pk)
	# if request.user != meeting.user.id:
		# only user whos invitation this is can update status
	# 	return Response(data="Not allowed", status=status.HTTP_403_FORBIDDEN)
	if request.method == 'DELETE':
    		
		meeting.delete()
		return Response(data="deleted", status=status.HTTP_200_OK)

	if request.method == 'PUT':
		serializer = CreateMeetingSerializer(meeting, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(data=serializer.data, status=status.HTTP_200_OK)
		else:
			return Response(data=serializer.erros, status=status.HTTP_400_BAD_REQUEST)
		
# Create invitation (event id,meeting id, invitee > participant of the event id)
@api_view(['POST'])
def createInvitation(request):
    # to do: dont allow same multiple invitations for same user
	meeting_id = int(request.data['meeting'])
	event_id = int(request.data['event'])
	participants = EventParticipant.objects.filter(event=request.data['event'])
	meeting = Meeting.objects.filter(pk=meeting_id)
	print(meeting)
	data = {}
	data['response'] = "invitation cant be created"
	if meeting[0].event.id == event_id:  # checks if meeting is from right event	
		invitee = int(request.data['invitee'])
		data['response'] = "invitee is not in the event"
		# checks if invitee is in the right Event
		for participant in participants:
			if participant.user.id == invitee:

				serializer = CreateInvitationSerializer(data=request.data)
				
				if serializer.is_valid():
					serializer.save()
					data['response'] = 'successfully created invitation'
					return Response(data=data, status=status.HTTP_200_OK)
				else:
					data = serializer.errors
					return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
			
	return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

# get all invitations for user id
@api_view(['GET'])
def getIvnitations(request, pk): # pk = id user
	print(pk)
	users = Invitation.objects.filter(invitee=pk)
	print(users)
	serializer = InvitationSerializer(users, many=True)
	return Response(data = serializer.data, status=status.HTTP_200_OK)

# Update invitation status
@api_view(['PUT','DELETE'])
# @permission_classes((IsAuthenticated,))
def StatusInvitation(request, pk):
	data={}
	invitation = Invitation.objects.get(id=pk)
	# if request.user != invitation.invite_name.id:
	# 		# only user whos invitation this is can update status
	# 	return Response(data="Not allowed", status=status.HTTP_403_FORBIDDEN)
	if request.method == 'PUT':
    	#updating status of the invitation	
		serializer = StatusInvitationSerializer(invitation, data=request.data)
		if serializer.is_valid():
			serializer.save()
			data['response'] = 'updated invitation'
			return Response(data=data, status=status.HTTP_200_OK)
		else:
			data = serializer.errors
			return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
	# delete method, deleting invitation
	if request.method == 'DELETE':
		invitation.delete()
		return Response(data="deleted", status=status.HTTP_200_OK)



# get all meetings for user id
@api_view(['GET'])
def getMeetings(request, pk): #pk = id user

	meeting = Meeting.objects.filter(creator=pk)

	serializer = CreateMeetingSerializer(meeting, many=True)
	return Response(data=serializer.data, status=status.HTTP_200_OK)

# Schedule meeting(send meeting id, and it will schedule meting with accepted invitations)
@api_view(['POST'])
def scheduleMeeting(request):
	meeting = request.data['meeting'] #meeting id
	attendees = Invitation.objects.filter(meeting=meeting, status='accept')
	# print(attendees)	
	data={}
	attendee_id = 0
	for attendee in attendees:
		attendee_id = attendee.invitee.id
		# print(attendee_id)
		dict ={'attendee':attendee_id,'meeting':meeting}
		serializer = ScheduleMeetSerializer(data=dict)
		
		if serializer.is_valid():
			serializer.save()
			data['response'] = 'meeting scheduled'
			return Response(data=data, status=status.HTTP_201_CREATED)
		else:
			data = serializer.errors
	return Response(data=data, status=status.HTTP_400_BAD_REQUEST)



# #Delete invitaiton
# @api_view(['DELETE'])
# # @permission_classes((IsAuthenticated,))
# def delIvnitation(request, pk): #pk = invitation id
# 	print(pk)
# 	invitation = Invitation.objects.get(id=pk)
# 	if request.user != invitation.invite_name.id: #only user whos invitation this is can delete it
# 		return Response(data="Not allowed", status=status.HTTP_403_FORBIDDEN)


