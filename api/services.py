from api.models import Image, Notes,Video,Audio
from api.serializers import AudioSerializer, ImageSerializer, NotesSerializer, VideoSerializer
from task_manager import secrets
import json

def getNotes(userId,bookingId,noteType):
    data=Notes.objects.filter(userId=userId, bookingId=bookingId, noteType=noteType)
    serializer = NotesSerializer(data,many=True)
    json_data = serializer.data
    responsData=[]
    for data in json_data:
        res=data
        noteId=data['notesId']
        if data['isEnable']==True:
            videos=Video.objects.filter(note=noteId, isEnable=True)
            serializervid = VideoSerializer(videos,many=True)
            vid_data = serializervid.data
            audios=Audio.objects.filter(note=noteId, isEnable=True)
            serializervid = AudioSerializer(audios,many=True)
            aud_data = serializervid.data
            images=Image.objects.filter(note=noteId, isEnable=True)
            serializerimg = ImageSerializer(images,many=True)
            img_data = serializerimg.data
            res['images']= img_data
            res['audio']= aud_data
            res['videos']= vid_data
            responsData.append(res)

      
    return responsData
