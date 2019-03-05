#!/usr/bin/env python
# coding: utf-8
import unittest
import sys
import secureROS

class TestStringMethods(unittest.TestCase):

    #def test_noRouter(self):
    #    router = secureROS.getRouter(-1);
    #    self.assertTrue ( router==None )

    #def test_Router0_RO_connect(self): 
    #    router = secureROS.getRouter(0,True);
    #    self.assertTrue ( router!=None )
    #    router.disconnect()

    #def test_Router0_RW_connect(self): 
    #    router = secureROS.getRouter(0,False);
    #    self.assertTrue ( router!=None )
    #    router.disconnect()

    #def test_Router1_RO_connect(self): 
    #    router = secureROS.getRouter(1,True);
    #    self.assertTrue ( router!=None )
    #    router.disconnect()

    #def test_Router1_RW_connect(self): 
    #    router = secureROS.getRouter(1,False);
    #    self.assertTrue ( router!=None )
    #    router.disconnect()

    #def test_RouterPrimary_RO_connect(self):
    #    router = secureROS.getRouter("Primary",True);
    #    self.assertTrue ( router!=None )
    #    router.disconnect()

    #def test_RouterPrimary_RW_connect(self):
    #    router = secureROS.getRouter("Primary",False);
    #    self.assertTrue ( router!=None )
    #    router.disconnect()

    #def test_RouterPrimary_RO_console(self):
    #    router = secureROS.getRouter("Primary",True);
    #    self.assertTrue ( router!=None )
    #    router.console()
    #    router.disconnect()

    #def test_RouterPrimary_RO_console(self):
    #    router = secureROS.getRouter("Primary",True);
    #    self.assertTrue ( router!=None )
    #    router.get_AddressListItems("Blacklist")
    #    router.disconnect()

    def test_parse(self): 
        #expr="NOT A==4 ANND A==123 OR C!=D" #error
        #expr="Not HaS A AND (A==123 And B==321 AND C!=D or has 'B' )"
        #expr="type=='ether' or type=='vlan'"
        #expr="has type and type=='ether' or type=='vlan'"
        #expr="has type and (type=='ether' or type!='vlan')"
        expr="has type and type=='ether' and type!='vlan'"
        print(secureROS.RouterContext.parse(expr))

if __name__ == '__main__':
    unittest.main()
