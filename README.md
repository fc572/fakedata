# fakedata

This project helps with the creation of related records that can be then used by a runtime. 
These files are based on the simple demo project, and have a similar structure.

The number of records can be customised by changing one of both of:
In /datafiles/service_and_equipment.py at line 82 by modifying the desidered ip length
returned, which is basically the number of IP per network that are wanted.

The type and number of network is the other variable that can be customised;
To change the number of network desidered change the value of numberOfNetworks in line
10 of starthere.py and to change the class of network change the value of address_class
in line 80 of /datafiles/service_and_equipment.py
