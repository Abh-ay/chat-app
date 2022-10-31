from django.contrib import admin

from room.models import Room
admin.site.register(Room)

from room.models import Message
admin.site.register(Message)