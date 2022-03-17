from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    #User endpoints:
    path('users', views.getUsers),
    path('user', views.createUser, name="create_User"),
    path('user/login', obtain_auth_token, name="login"),
    #Event endpoints:
    path('event', views.createEvent, name="create_Event"),
    path('event/participant', views.addParticipant, name="add_participant"),
    path('event/<int:pk>/participants', views.getParticipants, name="get_participants"),   
    path('events', views.getAllEvents, name="get_all_events"),   
    #Meeting endpoints
    path('meeting', views.createMeeting, name="create_meeting"),
    path('meeting/schedule', views.scheduleMeeting, name="schedule_meeting"),
    path('meetings/user/<int:pk>', views.getMeetings, name="get_meetings"),
    path('meetings', views.getAllMeetings, name="get_all_meetings"),
    path('meeting/<int:pk>', views.statusMeeting, name="status_meeting"),
    #Invitation endpoints
    path('invitation', views.createInvitation, name="create_invitation"),
    path('invitation/<int:pk>', views.StatusInvitation, name="status_invitation"),
    path('invitations/user/<int:pk>', views.getIvnitations, name="get_ivnitations"),
    
]



