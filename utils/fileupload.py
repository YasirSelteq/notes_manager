import io
import ftplib
import os
from PIL import Image
import datetime


def imageUploadToServer(img):
    try:
        ts =str(datetime.datetime.now().timestamp()) 
        image = Image.open(img)
        file_obj=img
        filename=ts+file_obj.name.split(".")[0]
        file_extension = img.name.split(".")[-1]
        if file_extension in ['jpg', 'jpeg']:
            output_format = 'JPEG'
        elif file_extension in ['png']:
            output_format = 'PNG'
        # Compress the image
        output_format = 'JPEG'
        image.save(filename+"." + output_format, optimize=True, quality=30)

        # Connect to the FTP server
        ftp = ftplib.FTP_TLS("push-30.cdn77.com")
        ftp.login(user="user_wbbxroeu", passwd="lwy2k7p6a65f4a98B9ID")
        ftp.cwd('www/notesmanager/images')

        # Upload the compressed image to the FTP server
        with open(filename+"." + output_format, 'rb') as fp:
            ftp.storbinary('STOR ' + filename+"." + output_format, fp)

        image_path = 'https://1864597015.rsc.cdn77.org/notesmanager/images' + '/' + filename+"." + output_format
        os.remove(filename+"." + output_format)
        ftp.quit()
        return image_path
    except Exception as e:
          print(e)


def audioUploadToServer(audio):
      try:
        print(audio)
        ftp = ftplib.FTP_TLS("push-30.cdn77.com")
        ftp.debug = True
        ftp.login(user="user_wbbxroeu", passwd="lwy2k7p6a65f4a98B9ID")
        ftp.cwd('www/notesmanager/audios')
        file_obj = audio[0]
        ftp.storbinary('STOR ' + file_obj.name, file_obj.file)
        image_path = 'https://1864597015.rsc.cdn77.org/notesmanager/audios' + '/' + file_obj.name
        ftp.quit()
        return image_path
      except Exception as e:
            print(e)


def videoUploadToServer(video):
    try:
        print(video)
        ftp = ftplib.FTP_TLS("push-30.cdn77.com")
        ftp.debug = True
        ftp.login(user="user_wbbxroeu", passwd="lwy2k7p6a65f4a98B9ID")
        ftp.cwd('www/notesmanager/videos')
        file_obj = video[0]
        ftp.storbinary('STOR ' + file_obj.name, file_obj.file)
        image_path = f'https://1864597015.rsc.cdn77.org/notesmanager/videos' + '/' + file_obj.name
        ftp.quit()
        return image_path
    except Exception as e:
          print(e)




# def mediaUploadToServer(media_files):
#     try:
#         ftp = ftplib.FTP_TLS("push-30.cdn77.com")
#         ftp.debug = True
#         ftp.login(user="user_wbbxroeu", passwd="lwy2k7p6a65f4a98B9ID")
#         ftp.cwd('www/notesmanager/media')
#         file_paths = []
#         for file_obj in media_files:
#             ftp.storbinary('STOR ' + file_obj.name, file_obj.file)
#             file_path = ftp.pwd() + '/' + file_obj.name
#             file_paths.append(file_path)
#         ftp.quit()
#         return file_paths
#     except Exception as e:
#           print(e)