import io
import ftplib
import os
from PIL import Image
import datetime
from task_manager import secrets



def imageDeleteFromServer(filename):
    try:
        # Connect to the FTP server
        newfileName=filename.replace(secrets.CDN_ROUTE_IMAGE, "")
        ftp = ftplib.FTP_TLS(secrets.FTP_HOST)
        ftp.login(user=secrets.FTP_USER_NAME, passwd=secrets.FTP_PASSWORD)
        ftp.cwd(secrets.FTP_CWD_IMAGE)
        ftp.delete(newfileName)
        ftp.quit()
        return "success"
    except Exception as e:
          print(e)


def audioDeleteFromServer(filename):
      try:
        newfileName=filename.replace(secrets.CDN_ROUTE_AUDIO, "")
        ftp = ftplib.FTP_TLS(secrets.FTP_HOST)
        ftp.login(user=secrets.FTP_USER_NAME, passwd=secrets.FTP_PASSWORD)
        ftp.cwd(secrets.FTP_CWD_AUDIO)
        ftp.delete(newfileName)
        ftp.quit()
        return "success"
      except Exception as e:
            print(e)


def videoDeleteFromServer(filename):
    try:
        newfileName=filename.replace(secrets.CDN_ROUTE_VIDEO, "")
        ftp = ftplib.FTP_TLS(secrets.FTP_HOST)
        ftp.login(user=secrets.FTP_USER_NAME, passwd=secrets.FTP_PASSWORD)
        ftp.cwd(secrets.FTP_CWD_VIDEO)
        ftp.delete(newfileName)
        ftp.quit()
        return "success"
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