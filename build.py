#!/usr/bin/python
import os,re,sys,getopt

class build():
    def __init__(self):
        b = "docker run --rm"
        goPath = self.getGoVersion()
        o = 'golang:%s bash -c'%(goPath) 
        c = 'CGO_ENABLED=1 GOOS=%s GOARCH=%s go build'%(self.getGOOS(),self.getGOARCH())
        e = 'export GOPATH=%s&&cd %s&&%s'%(os.getenv('GOPATH'),os.getenv('PWD'),c)
        gopath = os.getenv('GOPATH').split(':', 1 )
        for path in gopath:
            b = '%s -v %s:%s'%(b,path,path)
        cmd = '%s %s \'%s\''%(b,o,e)
        print(cmd)
        os.system(cmd)
    
    def getGOARCH(self):
        _,_,arch = self.arg()
        if arch != "":
            return arch
        return "amd64"

    def getGOOS(self):
        _,goos,_ = self.arg()
        if goos != "":
            return goos
        return "linux"

    def getGoVersion(self):
        version,_,_ = self.arg()
        if version != "":
            return version
        output = os.popen('go version')
        pattern = re.compile(r'\d+\.\d+\.\d+')
        m = pattern.findall(output.read())
        if m is not None:
            if len(m) == 1:
                return  m[0]

    def arg(self):
        verison = ''
        GOOS = ''
        GOARCH = ''
        try:
            opts, _ = getopt.getopt(sys.argv[1:],"hv:",["golangVersion=","GOOS=","GOARCH="])
        except getopt.GetoptError:
            print('build.py -v <golangversion> --GOOS=<goos> --GOARCH=<goarch>')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print('build.py -v <golangversion> --GOOS=<goos> --GOARCH=<goarch>')
                sys.exit()
            elif opt in ("-v", "--golangVersion"):
                verison = arg
            elif opt in ("--GOOS"):
                GOOS = arg
            elif opt in ("--GOARCH"):
                GOARCH = arg
        return verison,GOOS,GOARCH

if __name__ == "__main__":
    b = build()