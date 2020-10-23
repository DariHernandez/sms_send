#! python3
# Defines the textmyself(9 function that texts a menssage passed to it as string

import os, csv, pprint
from twilio.rest import Client
from interfaz import Interfaz

def textmyself (accountSID, authToken, fromNumber, toNumber, text): 
    """ Send menssage with twilio"""
    client = Client(accountSID, authToken)

    client.messages.create(
        body=text,
        from_=fromNumber,
        to=toNumber
    )

    print ('Menssage "%s" sent to: %s' % (text, toNumber))

# Initital files
currentPath = os.path.dirname (__file__)
pathCredentials = os.path.join (currentPath, 'credentials.json')
pathConfig = os.path.join (currentPath, 'config.json')
pathCSV = os.path.join (currentPath, 'numbers.csv')

# Run interfaz
myInterfaz = Interfaz (pathCredentials, pathConfig)

# Get credentials
credentials = myInterfaz.getCredentials()
accountSID   = credentials ['accountSID']
authToken    = credentials ['authToken']
twilioNumber = credentials ['twilioNumber']

# Get numbers
numbersCSV = open (pathCSV, 'r')
readerCSV = csv.reader (numbersCSV)
numbersCSV = list (readerCSV)

# Send menssage
for numberCSV in numbersCSV: 
    toNumber = numberCSV[0]
    text = numberCSV[1]

    # Send menssage
    textmyself (accountSID, authToken, twilioNumber, toNumber, text)
    
