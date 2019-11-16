#!/usr/bin/env python3
# -.- coding: utf-8 -.-
# scan.py

"""
Copyright (C) 2019 Ferdi S Kennedy (ferdi.kennedy@protonmail.com.com)
"""

import nmap

# perform a network scan with nmap
def scanNetwork(network):
    returnlist = []
    nm = nmap.PortScanner()
    a = nm.scan(hosts=network, arguments='-sn')

    for k, v in a['scan'].items():
        if str(v['status']['state']) == 'up':
            try:
                returnlist.append([str(v['addresses']['ipv4']), str(v['addresses']['mac'])])
            except:
                pass

    return returnlist
