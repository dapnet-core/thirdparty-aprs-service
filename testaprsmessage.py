import logging
import aprslib
# Uses https://aprs-python.readthedocs.io/en/stable/index.html
# pip install aprslib

#logging.basicConfig(level=logging.DEBUG) # level=10


# a valid passcode for the callsign is required in order to send
AIS = aprslib.IS(callsign="DB0SDA-13", passwd="17330", host="aprs.db0sda.ampr.org", port=14580)
AIS.connect()
# send a single status message
AIS.sendall("DB0SDA-13>APRS,TCPIP*::DH3WR-5  :Test von DAPNET567")

#AIS.consumer(lambda x: None, raw=True)
