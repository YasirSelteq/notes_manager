
import traceback
# from scheduler_backend import secrets
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.core.paginator import Paginator
from api.models import Audio, Image, Notes, Video
from api.serializers import AudioSerializer, ImageSerializer, NotesSerializer, VideoSerializer
from api import services
from utils.filedelete import audioDeleteFromServer, imageDeleteFromServer, videoDeleteFromServer
from utils.fileupload import imageUploadToServer,audioUploadToServer,videoUploadToServer
from utils.responses import internal_server_error, bad_request, created, not_found, ok
from utils.util import validate_page_number,check_file_size,convert_to_mb,compress_media_file
from django.http import JsonResponse
import uuid
from utils.kafkaProducer import producer
# Create your views here.

class TaskApi(APIView):
    def post(self, request):
        try:
            img=request.FILES.getlist('imageFile')
            audio=request.FILES.getlist('audioFile')
            video=request.FILES.getlist('videoFile')
            data=request.data
            serializer = NotesSerializer(data=data)
            if not serializer.is_valid(raise_exception=True):
                    return bad_request(data=serializer.errors, message='Failed to create Notes')
            else:
                serializer.save()
                note= serializer.data['notesId']
                if img:
                    for image in img:
                        path=imageUploadToServer(image)
                        serializerImg=ImageSerializer(data={"note":note,'imageUrl':path})
                        if not serializerImg.is_valid(raise_exception=True):
                            return bad_request(data=serializerImg.errors, message='Failed to create Notes')
                        else:
                            serializerImg.save()
                if audio:
                    for aud in audio:
                        path=audioUploadToServer(aud)
                        serializerAud=AudioSerializer(data={"note":note,'audioUrl':path})  
                        if not serializerAud.is_valid(raise_exception=True):
                            return bad_request(data=serializerAud.errors, message='Failed to create Notes')
                        else:
                            serializerAud.save()
                if video:
                    for vid in video:
                        path=videoUploadToServer(vid)
                        serializerVid=VideoSerializer(data={"note":note,'videoUrl':path}) 
                        if not serializerVid.is_valid(raise_exception=True):
                            return bad_request(data=serializerVid.errors, message='Failed to create Notes')
                        else:
                            serializerVid.save()  
            return created(data=note, message='Notes created successfully')

        except Exception as err:
            print(traceback.format_exc())
            return internal_server_error(message='Failed to create Notes')

    def get(self, request):
        try:
            data = {'key': 'value'}
            producer.send('testing-name', b'value')
            userId = request.GET.get('userId',None)
            bookingId = request.GET.get('bookingId',None)
            noteType = request.GET.get('noteType','self')
            data=services.getNotes(userId,bookingId,noteType)
            return ok(data=data)
        except Exception as err:
            print(traceback.format_exc())
            return internal_server_error(message='Failed to get Notes')

    def patch(self, request, ):
        try:
            fileId = request.query_params.get('fileId',None)  
            fileType = request.query_params.get('fileType',None) 
            if(fileType=="image"):
                data = Image.objects.get(imageId=fileId)
                serializer = ImageSerializer(data)
                json_data = serializer.data
                if json_data['isEnable']==True:
                    Image.objects.filter(imageId=fileId).update(isEnable=False)
                else:
                    Image.objects.filter(imageId=fileId).update(isEnable=True)
            elif(fileType=="audio"):
                data = Audio.objects.get(audioId=fileId)
                serializer = AudioSerializer(data)
                json_data = serializer.data
                if json_data['isEnable']==True:
                    Audio.objects.filter(audioId=fileId).update(isEnable=False)
                else:
                    Audio.objects.filter(audioId=fileId).update(isEnable=True)

            elif(fileType=="vidoe"):
                data = Video.objects.get(videoId=fileId)
                serializer = VideoSerializer(data)
                json_data = serializer.data
                if json_data['isEnable']==True:
                    Video.objects.filter(videoId=fileId).update(isEnable=False)
                else:
                    Video.objects.filter(videoId=fileId).update(isEnable=True)
            return created(data={'name':"Ok"},
                            message='Event updated successfully')

        except Exception as err:
            print(traceback.format_exc())
            return internal_server_error(message='Failed to update feeds')

    def delete(self, request):
        try:
            notesId = request.query_params.get('notesId',None)
            data = Notes.objects.get(notesId=notesId)
            serializer = NotesSerializer(data)
            json_data = serializer.data
            if json_data['isEnable']==True:
                Notes.objects.filter(notesId=notesId).update(isEnable=False)
            else:
                Notes.objects.filter(notesId=notesId).update(isEnable=True)
        
            return ok(message='Notes deleted successfully')

        except Exception as err:
            print(err)
            return internal_server_error(message='Failed to delete notes')

