Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import netmiko
>>> 
=================== RESTART: C:/Users/jecql/Documents/2.2.py ===================
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.48     YES NVRAM  up                    up      
GigabitEthernet2       unassigned      YES NVRAM  administratively down down    
GigabitEthernet3       unassigned      YES NVRAM  administratively down down    
>>> 
>>> 
=================== RESTART: C:/Users/jecql/Documents/2.2.py ===================
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
csr1000v-1(config)#int loopback 1ipv4 add 1.1.1.1 255.255.255.0no shutdowndescription LABORATORIO 2
                                 ^
% Invalid input detected at '^' marker.

csr1000v-1(config)#end
csr1000v-1#
>>> 
=================== RESTART: C:/Users/jecql/Documents/2.2.py ===================
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
csr1000v-1(config)#int loopback 1ipv4 add 1.1.1.1 255.255.255.0no shutdowndescription LABORATORIO 2
                                 ^
% Invalid input detected at '^' marker.

csr1000v-1(config)#end
csr1000v-1#
>>> 
========================================= RESTART: C:/Users/jecql/Documents/2.2.py =========================================
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
csr1000v-1(config)#int loopback 1
csr1000v-1(config-if)#ipv4 add 1.1.1.1 255.255.255.0
                         ^
% Invalid input detected at '^' marker.

csr1000v-1(config-if)#description LABORATORIO 2.2
csr1000v-1(config-if)#end
csr1000v-1#
>>> 
========================================= RESTART: C:/Users/jecql/Documents/2.2.py =========================================
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
csr1000v-1(config)#int loopback 1
csr1000v-1(config-if)#ip add 1.1.1.1 255.255.255.0
csr1000v-1(config-if)#description LABORATORIO 2.2
csr1000v-1(config-if)#end
csr1000v-1#
>>> 