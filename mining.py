import hashlib
import re
from time import *
import itertools


def find_difficulty(string, max_zeros):
	nounce =0
	start_time = time()
	while True:
		hash_str = string + str(nounce)
		sha256_hash = hashlib.sha256(hash_str).hexdigest()
		initial_zeros = 0
		for i in sha256_hash:
			if i =='0':
				initial_zeros += 1
			else:
				break
		if initial_zeros < max_zeros:
			nounce = nounce +1
			continue
		else:
			
			stop_time = time()
			print "Zeros = "+str(max_zeros) + " Time = "+str(stop_time - start_time)+ "Nounce = "+str(nounce)+" Hash= "+str(sha256_hash)
			max_zeros += 1
			nounce = 0
			start_time = time()
			continue
			
			

#Find dicciculty of this string
string = 'Any Strings'

time = find_difficulty(string , 0)
print time
