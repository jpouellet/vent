#!/usr/bin/env python

import select
from sys import stderr, exit, argv
import pybonjour
import Queue

def resolve(fullname, regtype):
    q = Queue.Queue()

    def resolve_callback(sdRef, flags, interfaceIndex, errorCode, this_fullname, hosttarget, port, txtRecord):
        if errorCode == pybonjour.kDNSServiceErr_NoError and this_fullname == fullname:
            q.put((hosttarget, port))

    def browse_callback(sdRef, flags, interfaceIndex, errorCode, serviceName, regtype, replyDomain):
        if errorCode != pybonjour.kDNSServiceErr_NoError:
            return

        if not (flags & pybonjour.kDNSServiceFlagsAdd):
            return

        resolve_sdRef = pybonjour.DNSServiceResolve(0, interfaceIndex, serviceName, regtype, replyDomain, resolve_callback)

        try:
            while q.empty():
                ready = select.select([resolve_sdRef], [], [])
                pybonjour.DNSServiceProcessResult(resolve_sdRef)
        except KeyboardInterrupt:
            pass
        finally:
            resolve_sdRef.close()

    browse_sdRef = pybonjour.DNSServiceBrowse(
      regtype = regtype,
      callBack = browse_callback)

    while q.empty():
        ready = select.select([browse_sdRef], [], [])
        pybonjour.DNSServiceProcessResult(browse_sdRef)

    return q.get()

if __name__ == '__main__':
    if len(argv) != 3:
        stderr.write('Usage: %s name _service._type\n' % argv[0])
        exit(1)
    #host, port = resolve('my_service._http._tcp.local.', '_http._tcp')
    name = '%s.%s.local.' % (argv[1], argv[2])
    regtype = argv[2]
    host, port = resolve(name, regtype)
    print '%s:%d' % (host, port)
