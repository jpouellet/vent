#!/usr/bin/env python

import select
from sys import argv, exit, stderr
import pybonjour

def advertise_service(name, regtype, port):
    def register_callback(sdRef, flags, errorCode, name, regtype, domain):
        if errorCode == pybonjour.kDNSServiceErr_NoError:
            print 'Registered service:'
            print '  name    =', name
            print '  regtype =', regtype
            print '  domain  =', domain
            print '  port    =', port


    sdRef = pybonjour.DNSServiceRegister(
      name = name, regtype = regtype, port = port,
      callBack = register_callback)

    print 'Registering zeroconf service...'
    while True:
        ready = select.select([sdRef], [], [])
        if sdRef in ready[0]:
            pybonjour.DNSServiceProcessResult(sdRef)

if __name__ == '__main__':
    if len(argv) != 4:
        stderr.write('Usage: %s name _service._type port\n' % argv[0])
        exit(1)

    name = argv[1]
    regtype = argv[2]
    port = int(argv[3])
    #print 'Advertising: name=%s type=%s port=%d' % (name, type, port)
    advertise_service(name, regtype, port)
