#!/usr/bin/env python

import json
import sys

print 'Content-Type: text/plain'
print ''

d = json.loads(open('../data.json', 'r').read())
d['cur_temp'] = 21.555
d['state'] = 'open'

print json.dumps(d)
