from rest_framework.exceptions import ValidationError
from rest_framework.serializers import Serializer, CharField, ModelSerializer

from api.models import NotesManager


class NotesSerlizer(ModelSerializer):
    bookingId= CharField(allow_blank=False,max_length=250)
    userId= CharField(allow_blank=False,max_length=250)
    notes= CharField(allow_blank=False,max_length=500)
    image= CharField(allow_blank=True)
    audio= CharField(allow_blank=True)
    video= CharField(allow_blank=True)

    class Meta:
            model = NotesManager
            fields = '__all__'
