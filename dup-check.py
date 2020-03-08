import sys
import os
import hashlib
from functools import partial

def calchash(file):
    ha = hashlib.sha1()
    with open(file,'rb') as f:
        for buf in iter(partial(f.read, 1024*1024), b''):
            ha.update(buf)
    return ha.hexdigest()


args=sys.argv

dir1=args[1]
print("basedir:"+dir1)

htable = dict()

for curdir , dirs, files  in os.walk(dir1):
    for file in files:
        fpath =os.path.join(curdir,file)
        fhash = calchash(fpath)
        if fhash in htable:
            print("duplicated!:"+htable[fhash] +":" +fpath)
            print('"'+fpath+'"')
            continue
        htable[fhash] =  fpath
