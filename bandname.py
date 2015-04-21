#!/usr/bin/python

"""
REASONABLE BAND NAME GENERATOR
""" 

import random,string,sys

prefix = ['b','bl','br',
		'c','ch','cl','cr',
		'd',
		'f','fl','fn','fr',
		'g','gh','gl','gr',
		'h',
		'l',
		'm',
		'n',
		'p','pl',
		't','tr',
		'sc','scr','sh','sk','sp',
		'w','wh','wr']
vowel = list("aeiou"*5+"y")
mid = ['dder','ff','gg','n','nk','nt','mp','pp','pper','pple','ptas','rb','rd','rk','rn','rp','rt','st','tter']
# suffixes that have all the vowels they need
suffix = ['','','','er','gubbler','ic','in','ington','le','ler','ley','ny','on','ton','tron','ty']
# suffixes that need vowels
vsuffix = ['ng','pple','tang','ting','bbler']
# suffixes for adjectives
suffix_adj = ['','','ing','able','apped','ed','ic']
# non-pluralised suffixes for band names
suffix_bn = ['','','er','erer','ic','in','unt','cunt','nut','nib','nip','nunt']

# Generate 20 band names if no number is specified
if len(sys.argv) > 1:
	times = int(sys.argv[1])
else:
	times = 20

# Generate the band names
for i in xrange(times):
	# first name
	fn = map(random.choice,[prefix,vowel,mid]+random.choice([[suffix],[vowel,vsuffix]]))
	# last name
	ln = map(random.choice,[prefix,vowel,mid]+random.choice([[suffix],[vowel,vsuffix]]))
	# adjective
	adj = map(random.choice,[prefix,vowel,mid,suffix_adj])
	# collective band name
	bn = map(random.choice,[prefix,vowel,mid,suffix_bn])

	fn,ln,adj,bn = map(lambda x:string.capitalize(string.join(x,'')), [fn,ln,adj,bn])
	bn = bn+'s'

	title = random.choice(['his','her','the','featuring'])
	if title in ["featuring"]:
		print "The",adj,bn,title,fn,ln
	else:
		print fn,ln,"and",title,adj,bn