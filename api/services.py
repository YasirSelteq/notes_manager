from api.models import Image, Notes,Video,Audio
from api.serializers import AudioSerializer, ImageSerializer, NotesSerializer, VideoSerializer
from task_manager import secrets
import json

def getNotes(userId,bookingId):
    data=Notes.objects.get(userId=userId,bookingId=bookingId)
    serializer = NotesSerializer(data)
    json_data = serializer.data
    noteId=json_data['notesId']
    if json_data['isEnable']==True:
        print(noteId)
        videos=Video.objects.filter(note=noteId, isEnable=True)
        serializervid = VideoSerializer(videos,many=True)
        vid_data = serializervid.data
        audios=Audio.objects.filter(note=noteId, isEnable=True)
        serializervid = AudioSerializer(audios,many=True)
        aud_data = serializervid.data
        images=Image.objects.filter(note=noteId, isEnable=True)
        serializerimg = ImageSerializer(images,many=True)
        img_data = serializerimg.data
        responsData= {
        'notes': json_data,
        'images':img_data,
        'audio':aud_data,
        'videos':vid_data
    }
    else:
        responsData="No data"
      
    return responsData
