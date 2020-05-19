import os
import requests
import json
import getpass
from requests.auth import HTTPBasicAuth




# 'http://c349-node2.squadron.support.hortonworks.com:8188/ws/v1/timeline/HIVE_QUERY_ID'
from subprocess import Popen, PIPE

kinit = '/usr/bin/kinit'
# # password = 'Rajind12'
# kinit_args = [ kinit, '%s@%s' % ('rajesh', 'SUPPORT.COM') ]
# kinit = Popen(kinit_args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
# kinit.stdin.write('%s\n' % password)
# kinit.wait()
#kinit -kt /etc/security/keytabs/hive.service.keytab hive/c349-node2.squadron.support.hortonworks.com@SUPPORT.COM
command = [kinit, ]
