import io
import ftplib
import os
from PIL import Image
import datetime
from task_manager import secrets


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
        ftp = ftplib.FTP_TLS(secrets.FTP_HOST)
        ftp.login(user=secrets.FTP_USER_NAME, passwd=secrets.FTP_PASSWORD)
        ftp.cwd(secrets.FTP_CWD_IMAGE)

        # Upload the compressed image to the FTP server
        with open(filename+"." + output_format, 'rb') as fp:
            ftp.storbinary('STOR ' + filename+"." + output_format, fp)

        image_path = secrets.CDN_ROUTE_IMAGE + '/' + filename+"." + output_format
        os.remove(filename+"." + output_format)
        ftp.quit()
        return image_path
    except Exception as e:
          print(e)


def audioUploadToServer(audio):
      try:
        ts =str(datetime.datetime.now().timestamp()) 
        ftp = ftplib.FTP_TLS(secrets.FTP_HOST)
        ftp.login(user=secrets.FTP_USER_NAME, passwd=secrets.FTP_PASSWORD)
        ftp.cwd(secrets.FTP_CWD_AUDIO)
        file_obj = audio
        filename=ts+file_obj.name
        ftp.storbinary('STOR ' + filename, file_obj.file)
        image_path = secrets.CDN_ROUTE_AUDIO + '/' + filename
        ftp.quit()
        return  image_path
      except Exception as e:
            print(e)


def videoUploadToServer(video):
    try:
        ts =str(datetime.datetime.now().timestamp()) 
        ftp = ftplib.FTP_TLS(secrets.FTP_HOST)
        ftp.login(user=secrets.FTP_USER_NAME, passwd=secrets.FTP_PASSWORD)
        ftp.cwd(secrets.FTP_CWD_VIDEO)
        file_obj = video
        filename=ts+file_obj.name
        ftp.storbinary('STOR ' + filename, file_obj.file)
        image_path = secrets.CDN_ROUTE_VIDEO + '/' + filename
        ftp.quit()
        return image_path
    except Exception as e:
          print(e)
