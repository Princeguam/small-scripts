from notifypy import Notify
import sys 

def send_notifification():
	notification = Notify()
	notification.title = "Brazzers mom"
	notification.message = "Test work with pythons notification module"
	notification.send()

argument1 = sys.argv[1]

if argument1.lower() == "Y":
	send_notifification()
# else:
# 	print('nothing to print')