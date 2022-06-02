import visa 

rm = visa.ResourceManager('@py')

scope = rm.open_resource('TCPIP::192.16.13.181::INSTR')
scope = rm.open_resource('USB0::{Vendor ID}::{Model ID}::{Serial Number}::INSTR')
scope = rm.open_resource('USB0::0x0699::0x0409::C010730::INSTR')

scope.write("*IDN?")
print(scope.read())