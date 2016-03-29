#!/usr/bin/python3

import sys ; sys.path.insert(0, '..')

import DNS

DNS.ParseResolvConf()

print(DNS.mxlookup("hotmail.com"))
print(DNS.mxlookup("connect.com.au"))
