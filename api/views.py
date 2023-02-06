
import traceback
# from scheduler_backend import secrets
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.core.paginator import Paginator
from api.models import NotesManager
from api.serializers import NotesSerlizer
from api import services
from utils.filedelete import audioDeleteFromServer, imageDeleteFromServer, videoDeleteFromServer
from utils.fileupload import imageUploadToServer,audioUploadToServer,videoUploadToServer
from utils.responses import internal_server_error, bad_request, created, not_found, ok
from utils.util import validate_page_number,check_file_size,convert_to_mb,compress_media_file
from django.http import JsonResponse
import uuid
# Create your views here.

class TaskApi(APIView):
    def post(self, request):
        try:
            img=request.FILES.getlist('image')
            audio=request.FILES.getlist('audio')
            video=request.FILES.getlist('video')
            img_notes=[]
            print(img)
            for image in img:
                print(image)
                path=imageUploadToServer(image)
                print(path)
                img_notes.append(path)
            imgstring= ','.join(img_notes)
            audio_notes= audioUploadToServer(audio)
            video_notes= videoUploadToServer(video)
            data=request.data
            data.pop('image')
            data.pop('audio')
            data.pop('video')
            data['image']=imgstring
            data['audio']=audio_notes
            data['video']=video_notes
            print(data)
            serializer = NotesSerlizer(data=data)
            if not serializer.is_valid(raise_exception=True):
                    return bad_request(data=serializer.errors, message='Failed to create Notes')
            else:
                verified_notes = serializer.validated_data
                serializer.save()
                return created(data={'name': verified_notes.get('note')},
                            message='Notes created successfully')

        except Exception as err:
            print(traceback.format_exc())
            return internal_server_error(message='Failed to create Notes')

    def get(self, request):
        try:
            userId = request.query_params.get('userId',None)
            bookingId = request.query_params.get('bookingId',None)
            data = NotesManager.objects.get(userId=userId,bookingId=bookingId)
            serializer = NotesSerlizer(data)
            json_data = serializer.data
            print(json_data)
            return ok(data=json_data)
        except Exception as err:
            print(traceback.format_exc())
            return internal_server_error(message='Failed to get Notes')

    def patch(self, request, ):
        try:
            request_data = request.data    
                # mongo_collection.insert_one(dict(verified_events))
            return created(data={'name':"Ok"},
                            message='Event updated successfully')

        except Exception as err:
            print(traceback.format_exc())
            return internal_server_error(message='Failed to update feeds')

    def delete(self, request):
        try:
            notesId = request.query_params.get('notesId',None)
            data = NotesManager.objects.get(notesId=notesId)
            serializer = NotesSerlizer(data)
            json_data = serializer.data
            image= json_data['image']
            audio= json_data['audio']
            video= json_data['video']
            my_list = image.split(",")
            for data in my_list:
                img_result= imageDeleteFromServer(data)
            audio_result=audioDeleteFromServer(audio)
            video_result=videoDeleteFromServer(video)
            if img_result and audio_result and video_result == "success":
               NotesManager.objects.get(notesId=notesId).delete()
               return ok(message='Notes deleted successfully')

        except Exception as err:
            print(err)
            return internal_server_error(message='Failed to delete notes')

