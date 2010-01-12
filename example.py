# encoding=utf-8

from dnswh import Swher

s = Swher.Swher()
print s.getDNSServers()
print s.setDNSServers(['192.168.0.152'])
