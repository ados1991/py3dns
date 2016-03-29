#!/usr/bin/python3

import sys ; sys.path.insert(0, '..')
import DNS
req = DNS.DnsRequest('google.com', qtype='AAAA', protocol='tcp')
resp = req.req()
print(resp.answers[0]['name'], resp.answers[0]['data'])

req1 = DNS.DnsRequest('google.com', qtype='AAAA', protocol='udp')
resp1 = req1.req(resulttype='binary')
print(resp1.answers[0]['name'], resp1.answers[0]['data'])

req2 = DNS.DnsRequest('google.com', qtype='AAAA', protocol='tcp')
resp2 = req2.req(resulttype='text')
print(resp2.answers[0]['name'], resp2.answers[0]['data'])

req3 = DNS.DnsRequest('mailout03.controlledmail.com', qtype='TXT', protocol='tcp')
resp3 = req3.req()
print(resp3.answers[0]['name'], resp3.answers[0]['data'])

req4 = DNS.DnsRequest('mailout03.controlledmail.com', qtype='TXT', protocol='udp', resulttype='binary')
resp4 = req4.req(resulttype='binary')
print(resp4.answers[0]['name'], resp4.answers[0]['data'])

req5 = DNS.DnsRequest('mailout03.controlledmail.com', qtype='TXT', protocol='tcp')
resp5 = req5.req(resulttype='text')
print(resp5.answers[0]['name'], resp5.answers[0]['data'])

req6 = DNS.DnsRequest('controlledmail.com', qtype='MX', protocol='tcp')
resp6 = req6.req()
print(resp6.answers[0]['name'], resp6.answers[0]['data'])

req7 = DNS.DnsRequest('controlledmail.com', qtype='MX', protocol='udp', resulttype='binary')
resp7 = req6.req(resulttype='binary')
print(resp7.answers[0]['name'], resp7.answers[0]['data'])

req8 = DNS.DnsRequest('controlledmail.com', qtype='MX', protocol='tcp')
resp8 = req8.req(resulttype='text')
print(resp8.answers[0]['name'], resp8.answers[0]['data'])

