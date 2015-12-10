#!/usr/bin/env python

import json
import sys
import re

x = json.loads(sys.stdin.read())
d = {}

d['mode'] = 'heat'
try:
	if x['mode'] in ('heat', 'cool'):
		d['mode'] = x['mode']
except:
	pass

d['schedule'] = []
try:
	for e in x['schedule']:
		try:
			if e['type'] == 'at' and re.match('(?:1[0-9]|2[0-3]|[1-9]):[0-5][0-9]', e['at']):
				d['schedule'].append({'type':'at', 'at':e['at']})
			elif e['type'] == 'every' and isinstance(e['every']['n'], int) and e['every']['n'] > 0 and e['every']['period'] in ('minutes', 'hours'):
				d['schedule'].append({'type':'every', 'every':{'n':x['every']['n'], 'period':x['every']['period']}})
		except:
			pass
except:
	pass


d['display_units'] = 'F'
try:
	if x['display_units'] in ('C', 'F'):
		d['display_units'] = x['display_units']
except:
	pass

d['lower_bound'] = 15.0
try:
	if instanceof(x['lower_bound'], float):
		d['lower_bound'] = x['lower_bound']
except:
	pass

d['upper_bound'] = 25.0
try:
	if instanceof(x['upper_bound'], float):
		d['upper_bound'] = x['upper_bound']
except:
	pass

open('../data.json', 'w').write(json.dumps(x)+'\n')

print 'Content-Type: text/plain'
print ''
