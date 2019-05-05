#!/usr/bin/python
import os,re,sys,getopt

class build():
    GOVersion = ''
    GOOS = ''
    GOARCH = ''
    def __init__(self):
        self.arg()

    def run(self):
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
        if self.GOARCH != "":
            return self.GOARCH
        return "amd64"

    def getGOOS(self):
        if self.GOOS != "":
            return self.GOOS
        return "linux"

    def getGoVersion(self):
        if self.GOVersion != "":
            return self.GOVersion
        output = os.popen('go version')
        pattern = re.compile(r'\d+\.\d+\.\d+')
        m = pattern.findall(output.read())
        if m is not None:
            if len(m) == 1:
                return  m[0]

    def arg(self):
        try:
            opts, _ = getopt.getopt(sys.argv[1:],"h",["GOVersion=","GOOS=","GOARCH="])
        except getopt.GetoptError:
            print('build.py --GOVersion=<goversion> --GOOS=<goos> --GOARCH=<goarch>')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print('build.py --GOVersion=<goversion> --GOOS=<goos> --GOARCH=<goarch>')
                sys.exit()
            elif opt in ("--GOVersion"):
                self.GOVersion = arg
            elif opt in ("--GOOS"):
                self.GOOS = arg
            elif opt in ("--GOARCH"):
                self.GOARCH = arg
        # return verison,GOOS,GOARCH

if __name__ == "__main__":
    b = build()
    b.run()