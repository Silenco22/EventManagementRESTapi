from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    #User endpoints:
    path('users', views.Users, name="Users"),
    path('users/login', obtain_auth_token, name="login"),
    #Event endpoints:
    path('events', views.Events, name="Events"),
    path('events/participants', views.addParticipant, name="add_participant"),
    path('events/participants/<int:pk>', views.getParticipants, name="get_participants"),   
    #Meeting endpoints
    path('meetings', views.Meetings, name="Meetings"),
    path('meetings/schedule', views.scheduleMeeting, name="schedule_meeting"),
    path('meetings/users/<int:pk>', views.getMeetings, name="get_meetings"),
    path('meetings/<int:pk>', views.statusMeeting, name="status_meeting"),
    #Invitation endpoints
    path('invitations', views.createInvitation, name="create_invitation"),
    path('invitations/<int:pk>', views.StatusInvitation, name="status_invitation"),
    path('invitations/users/<int:pk>', views.getIvnitations, name="get_ivnitations"),
    
]



