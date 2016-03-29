#!/usr/bin/python3

import sys ; sys.path.insert(0, '..')
import DNS

def Error(mesg):
    import sys
    print(sys.argv[0],"ERROR:")
    print(mesg)
    sys.exit(1)

def main():
    import sys
    if len(sys.argv) != 2:
        Error("usage: %s somedomain.com"%sys.argv[0])
    domain = sys.argv[1]
    nslist = GetNS(domain)
    print("According to the primary, the following are nameservers for this domain")
    for ns in nslist:
        print("  ",ns)
        CheckNS(ns,domain)


def GetNS(domain):
    import DNS
    # hm. this might fail if a server is off the air.
    r = DNS.Request(domain,qtype='SOA').req()
    if r.header['status'] != 'NOERROR':
        Error("received status of %s when attempting to look up SOA for domain"%
                (r.header['status']))
    if r.header['status'] == 'NXDOMAIN':
        print("SOA request was NXDOMAIN")
        primary = ''
    else:
        if r.answers:
            primary,email,serial,refresh,retry,expire,minimum = r.answers[0]['data']
            print("Primary nameserver for domain %s is: %s"%(domain,primary))
        else:
            print("No answer to SOA query")
            primary = ''
    r = DNS.Request(domain,qtype='NS',server=primary,aa=1).req()
    if r.header['status'] != 'NOERROR':
        Error("received status of %s when attempting to query %s for NSs"%
                (r.header['status']))
    if r.header['aa'] != 1 and primary is not '':
        Error("primary NS %s doesn't believe that it's authoritative!"% primary)
    nslist = [x['data'] for x in r.answers]
    print("Full list of nameservers for domain %s is: %s"%(domain,nslist))
    return nslist

def CheckNS(nameserver,domain):
    r = DNS.Request(domain,qtype='SOA',server=nameserver,aa=1).req()
    if r.header['status'] != 'NOERROR':
        Error("received status of %s when attempting to query %s for NS"%
                (r.header['status']))
    if r.header['aa'] != 1:
        Error("NS %s doesn't believe that it's authoritative!"% nameserver)
    primary,email,serial,refresh,retry,expire,minimum = r.answers[0]['data']
    print("      NS has serial",serial[1])

if __name__ == "__main__":
    main()
