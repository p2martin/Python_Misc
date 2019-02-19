#!/bin/python
import whois,time

"""
Using python 3.7.2 / whois module to perform multiple whois queries on ip / domains from text file and write results out to
a txt file
"""

def parse_ip_to_list():
	f = open('IPaddresses.txt','r')						
	ips = []									                
	for ip_addr in f:
		ips.append(ip_addr)						          
	f.close() 									              
	return ips


def whois_lookup():
	f = open("whoisinfo.txt","w")
	ips = parse_ip_to_list()
	for current_ip in ips:
		print ("\t[+]--Current info being saved for \t%s" % current_ip)
    current_info = whois.whois(current_ip.strip())	
		f.write(str(current_info))
		time.sleep(1)							                        #allow time for reading next socket obj
	f.close()

whois_lookup()
