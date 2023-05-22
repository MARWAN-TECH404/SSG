import os,platform

os.system('git pull')

 

SSG31_enc=platform.architecture()[0]

if SSG31_enc=="32bit":

    print('Sorry 32 Bit Not Supported...')

elif SSG31_enc=="64bit":

    #print('Command is in update wait we will fix it soon !')

    __import__("SSG31_enc")






