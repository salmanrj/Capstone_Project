import subprocess
import time

def nfc_raw():
    lines=subprocess.check_output("/usr/bin/nfc-poll", stderr=open('/dev/null','w'))
    return lines

def read_nfc():
    lines=nfc_raw()
    return lines

try:
    while True:
        myLines=read_nfc()
        buffer=[]
        for line in myLines.splitlines():
            line_content=line.split()
            if(not line_content[0] =='UID'):
                pass
            else:
                buffer.append(line_content)
#         for dum in range(4):
#             buffer.append(dum)
        str=buffer[0]
        id_str=[]
        for i in range(2,len(str)):
            id_str.append(str[i])
        #id_str=str[2]+" "+str[3]+" "+str[4]+" "+str[5]+" "+str[6]+" "+str[7]+" "+str[8]
        uid="".join(id_str)
        print ("UID adalah : {}").format(uid)
        #print (myLines)
        print (buffer)


except KeyboardInterrupt:
        pass
