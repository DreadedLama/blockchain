import hashlib
import re
from time import *
import itertools

def mine(string, max_zeros):
	nonce = 0
	while True: 
		hash_str = str(string + str(nonce)).encode()
		sha256_hash = hashlib.sha256(hash_str).hexdigest()
		noOfZeros = 0	

		for i in sha256_hash:
			if i == '0':
				noOfZeros += 1
			else:
				break
		
		if noOfZeros < max_zeros:
			nonce += 1
			continue
		else:
			break		
	print(nonce)
	return nonce, sha256_hash


def find_difficulty(string, max_zeros):
	nounce =0
	start_time = time()
	while True:
		hash_str = str(string + str(nounce)).encode()
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
			print ("Zeros = "+str(max_zeros) + " Time = "+str(stop_time - start_time)+ "Nounce = "+str(nounce)+" Hash= "+str(sha256_hash))
			max_zeros += 1
			nounce = 0
			start_time = time()
			continue
			
			
if __name__ == "__main__":
	#Find difficulty of this string
	string = '1temporary data5783c476b17ea32d0770d32ae0458b1fe0e2d9eacab7da86377eba8b484954182018-03-31 01:57:34.766748'

	time = find_difficulty(string , 4)
	print (time)
