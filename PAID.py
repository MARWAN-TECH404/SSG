import os,platform
os.system('git pull')
 
trt=platform.architecture()[0]
if ssg34_enc=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif trt=="64bit":
    __import__("ssg34_enc")
