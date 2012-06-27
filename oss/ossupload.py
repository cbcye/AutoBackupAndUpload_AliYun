from oss_api import *
from oss_xml_handler import *
from optparse import *
import os,sys
#HOST = 'storage.aliyun.com' #Internet Transport
HOST ='storage-vm.aliyun-inc.com' #Internal Transport
ACCESS_ID = 'xxxxx'
SECRET_ACCESS_KEY = 'xxxxxx'
def parseArgs():
    parser = OptionParser()
    parser.add_option('-d','--dest',action="store",type='string',
                      dest = 'dest',help='upload dest file names')
    parser.add_option('-l','--local',action="store",type='string',
                      dest = 'local',help='upload local file names')
    (options, args) = parser.parse_args()
    if not options.dest:
        parser.error('option dest must exist')
    if not options.local:
        parser.error('option local must exist')
    return options
def uploadFile(options):
    oss = OssAPI(HOST, ACCESS_ID, SECRET_ACCESS_KEY)
    for path, dirs, files in os.walk(options.local, 'topdown'):
        for name in files:
            res = oss.put_object_from_file('gpoogp_backup', os.path.join(options.dest,name),
                                           os.path.join(path,name),
                                           'application/octet-stream') #Bucket Name
            if (res.status / 100) == 2:
                print "File:%s upload succeed" % os.path.join(path,name)
            else:
                body = res.read()
                print "Fail\n%s" % body
if __name__ == '__main__':
    options = parseArgs()
    uploadFile(options)
