# EventManagementRESTapi
Event management rest api

## HOW TO INSTALL AND START THE SERVER:

#### 0. install pyhton
#### 1. clone repository: git clone https://github.com/Silenco22/EventManagementRESTapi
#### 2. create virtual env with: pip install venv venv
#### 3. navigate to venv folder and activate venv(commands): a) cd venv/Scripts b) activate
#### 4. install requirements: pip install -r requirements.txt
#### 5. make migrations: py manage.py makemigrations
#### 6. migrate: py manage.py migrate
#### 7. runserver: py manage.py runserver

### Command to run tests: py manage.py test

## ENDPOINTS:

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">GET</th>
    <th class="tg-0pky">api/users</th>
    <th class="tg-0pky">Get all users</th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">POST</td>
    <td class="tg-0pky">api/user</td>
    <td class="tg-0pky">Create user</td>
    <td class="tg-0pky">{"email": "<a href="mailto:&#101;&#x40;&#x65;&#46;&#99;&#x6f;&#x6d;"><span style="color:#905">e@e.com</span></a>", "username":"", "password":"", "password2":""}</td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">POST</td>
    <td class="tg-0pky">api/user/login</td>
    <td class="tg-0pky">Get login token</td>
    <td class="tg-0pky">{"username": "<a href="mailto:&#101;&#64;&#x65;&#46;&#x63;&#x6f;&#x6d;"><span style="color:#905">e@e.com</span></a>", "password":""}</td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">Event endpoints:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">POST</td>
    <td class="tg-0pky">api/event</td>
    <td class="tg-0pky">Create Event</td>
    <td class="tg-0pky">{"creator": "&lt;userId&gt;", "event_name":"&lt;string&gt;"}</td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">POST</td>
    <td class="tg-0pky">api/event/participant</td>
    <td class="tg-0pky">Add participant to Event</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">GET</td>
    <td class="tg-0pky">api/event/{eventId}/participants</td>
    <td class="tg-0pky">Get all event participants by Event id</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">GET</td>
    <td class="tg-0pky">api/events</td>
    <td class="tg-0pky">Get all events</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">Meeting endpoints</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">POST</td>
    <td class="tg-0pky">api/meeting</td>
    <td class="tg-0pky">Create meeting</td>
    <td class="tg-0pky">{"user": "&lt;userid&gt;", "meeting_name":"&lt;string&gt;", "event_name":"&lt;eventId&gt;", "meeting_date":"&lt;YY-MM-DD&gt;", "array":"&lt;userId1&gt; &lt;userId2&gt;"}</td>
    <td class="tg-0pky">"array" is optional parameter and if we add it it will auto create invitations for userIDs but they need to be sent like:<br>"1 2 3 8 9" etc. like string with spaces</td>
  </tr>
  <tr>
    <td class="tg-0pky">POST</td>
    <td class="tg-0pky">api/meeting/schedule</td>
    <td class="tg-0pky">Schedule meeting</td>
    <td class="tg-0pky">{"meeting_name": "&lt;meetingId&gt;"}</td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">GET</td>
    <td class="tg-0pky">api/meetings/user/{userId}</td>
    <td class="tg-0pky">Get all meetings that user created</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">GET</td>
    <td class="tg-0pky">api/meetings</td>
    <td class="tg-0pky">Get all meetings</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">PUT</td>
    <td class="tg-0pky">api/meeting/{meetingId}</td>
    <td class="tg-0pky">Update meeting by meeting id</td>
    <td class="tg-0pky">{"user": "&lt;userId&gt;", "event_name":"&lt;eventId&gt;", "meeting_name":"&lt;string&gt;", "meeting_date":"&lt;YY-MM-DD&gt;"}</td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">DELETE</td>
    <td class="tg-0pky">api/meeting/{meetingId}</td>
    <td class="tg-0pky">Delete meeting by meeting id</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">Invitation endpoints</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">POST</td>
    <td class="tg-0pky">api/invitation</td>
    <td class="tg-0pky">Create invitation</td>
    <td class="tg-0pky">{"event_name": "&lt;eventId&gt;", "meeting_name":"&lt;meetingId&gt;", "invite_name":"&lt;inviteId&gt;"}</td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">PUT</td>
    <td class="tg-0pky">api/invitation/{invitationId}</td>
    <td class="tg-0pky">Update invitation by invitation id</td>
    <td class="tg-0pky">{"status": "(accept, decline)"}</td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">DELETE</td>
    <td class="tg-0pky">api/invitation/{invitationId}</td>
    <td class="tg-0pky">Delete invitation by invitation id</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">GET</td>
    <td class="tg-0pky">api/invitations/user/{userID}</td>
    <td class="tg-0pky">Get invitations by user id</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
</tbody>
</table>
