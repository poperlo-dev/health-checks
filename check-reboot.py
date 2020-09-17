""" This is check reboot file """
""" Add some feature """
""" Some code here """

import socket

def check_root_full():
	return check_disk_full("disk="/", min_gb=2, min_percent=10)

def check_no_network():
	try:
		socket,gethostbyname("www.google.com")
		return False
	except:
		return True

def main():
	checks=[
		(check_reboot, "Pending Reboot"),
		(check_root_full, "Root partition full"),
		(check_no_network, "No working network."),
	]

	everything_ok = True

	for check, msg in checks:
		if check():
			print(msg)
			everything_ok = False
	if not everything_ok:
		sys.exit(1)

	print("Everything is ok.")
	sys.exit(0)

main()

""" Some corrections to he code"""
