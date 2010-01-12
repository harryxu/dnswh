# encoding=utf-8

import sys

class SwherBase(object):
    def getCurrentDNS(self):
        """docstring for getCurrentDNS"""
        pass
    
    def setDNS(self, dns):
        """docstring for setDNS"""
        pass

    def useInterface(self):
        """docstring for userInterface"""
        pass

class WinSwher(SwherBase):
    def __init__(self):
        c = wmi.WMI()
        interfaces = c.Win32_NetworkAdapterConfiguration(IPEnabled = 1)

        if len(interfaces) > 0:
            self.interfae = interfaces[0]

    def getDNSServers(self):
        if not self.interfae:
            raise Exception('no netword interfaces found')

        return self.interfae.DNSServerSearchOrder
    
    def setDNSServers(self, dnsServers):
        if not self.interfae:
            raise Exception('no netword interfaces found')

        result = self.interfae.SetDNSServerSearchOrder(
                                DNSServerSearchOrder = dnsServers)
        return result

########################
        
os = sys.platform

if os == 'win32':
    import wmi
    Swher = WinSwher

