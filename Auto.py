import sys 
import clr 
import sys

print('Adding location of Newport.ESP301.CommandInterface.dll to sys.path')
sys.path.append (r'C\Newport\Motion Control\ESP301\Bin')

clr.AddReferenceToFile('Newport.ESP301.CommandInterfface.dll') 
from CommandInterface import * 
 
instrument= Port_#0002.Hub_#0001 
BAUDRATE = 921600 
print ('Instrument Key=>', instrument) 

ESP301Device = ESP301() 

ret = esp301.OpenInstrument(instrument, BAUDRATE); 

result, response, errString = ESP301Device.SR_Get(1) 
if result == 0 : print ('positive software limit=>', response) 
else: print ('Error=>',errString) 
 
# get negative software limit

result, response, errString = ESP301Device.SL_Get(1) 
if result == 0 : print ('negative software limit=>', response )
else: print ('Error=>',errString)
 
result, response, errString = ESP301Device.VE() 
if result == 0 : print ('controller revision=>', response )
else: print ('Error=>',errString )

result, response, errString = ESP301Device.TP(1) 
if result == 0 : print ('position=>', response) 
else: print ('Error=>',errString) 

esp301.CloseInstrument();