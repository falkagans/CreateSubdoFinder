#!/usr/bin/env python
import requests, os, sys, multiprocessing
try :
	CGR = '\33[34m'
	CEN = '\33[0m'
	CRE = '\33[91m'

	os.system('clear')
	print(CGR+""" #####  ####### ######      #####  #     #  #####  #       #       
#     # #     # #     #    #     # #     # #     # #       #       
#       #     # #     #    #       #     #       # #       #       
#  #### #     # #     #     #####  #######  #####  #       #       
#     # #     # #     #          # #     #       # #       #       
#     # #     # #     #    #     # #     # #     # #       #       
 #####  ####### ######      #####  #     #  #####  ####### ####### 
                                        
Subdomain Finder"""+CEN)
	#domain = raw_input("Masukkan Domain (Example =  falkapink.id) : ")
	wordlist=""
	print("==================================================")
	print(CRE+" Coder  : FALKA (GOD SHEEL) "+CEN)
	print(CRE+" Github : https://github.com/falkagans)"+CEN)
	print("==================================================")
	print(CGR+"OPTION :"+CEN)
	print("1. Bruteforce Subdomain Using Big Wordlist [500++ List]")
	print("2. Bruteforce Subdomain Using BigBang Wordlist [500k++ List]")
	choose = raw_input("Choose "+CGR+"[1/2]"+CEN+" : ")



	def request(url):
		try :
			return requests.get("http://"+url)
		except requests.exceptions.ConnectionError:
			pass
		except requests.exceptions.InvalidURL:
			pass
		except UnicodeError:
			pass
		except KeyboardInterrupt:
			print("Program Terminated")
			sys.exit(0)

	if choose==str("1"):
		wordlist="big.txt"
		domain = raw_input("Input Target Domain Here (ex:"+CGR+"falkapink.id"+CEN+") : ")
		request(domain)
	elif choose==str("2"):
		wordlist="subdomain.list"
		domain = raw_input("Input Target Domain Here (ex:"+CGR+"falkapink.id"+CEN+") : ")
		request(domain)
	else :
		print("Wrong Input")
		sys.exit(0)


	with open(wordlist,"r") as wordlist:
		for line in wordlist:
			word = line.strip()
			test_url = word+"."+domain
			response = request(test_url)
			proc = multiprocessing.Process(target=response, args=(10,20))
			if proc:
				print(CGR+"[+]"+CEN+" Subdomain Ditemukan >> "+CGR+test_url+CEN)

except KeyboardInterrupt:
			print("Program Terminated")
			sys.exit(0)
