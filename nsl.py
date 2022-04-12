from nslookup import Nslookup
import sys,os

host = input("Host: ")

dns_query = Nslookup()
dns_query = Nslookup(dns_servers=["1.1.1.1"], verbose=False, tcp=False)
ips_record = dns_query.dns_lookup(host)
print(ips_record.response_full)
print(" ")
soa_record = dns_query.soa_lookup(host)
print(soa_record.response_full, soa_record.answer)

print("\n")
met = input("back to method y/n?: ")
if met == 'y':
	os.system("python3 WORK")
else:
	sys.exit()
