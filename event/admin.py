from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Event, EventParticipant, Invitation, Meeting, MeetingScheduled


class AccountAdmin(UserAdmin):
    list_display = ('pk','name')
    search_fields = ('pk',)
    readonly_fields=('pk',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('pk',)


admin.site.register(Event)


admin.site.register(EventParticipant)
admin.site.register(Invitation)
admin.site.register(Meeting)
admin.site.register(MeetingScheduled)
