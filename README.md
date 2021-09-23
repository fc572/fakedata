# fakedata

This project helps with the creation of related records that can be then used by a runtime. 
These files are based on the simple demo project, and have a similar structure.

Account details file has Document number to which the final 4 digits are extracted and matched with the 
Customer account column in the customer_site_and_service.csv file.

From the customer_site_and_service.csv file the ServiceID column is read and matched with the numberic part
of the serviceTag column in the service_and_equipment.csv file

From the service_and_equipment.csv file the InterfaceIpAddress column is read and matched with the IpAddress
in the equipment_on_site.csv file.
The ip address from this file is also matched against the network_discovery:extraInfoMIpAddress in the NetworkDiscoveryFile.rdf

At last, in the equipment_on_site.csv file, the EntityName column is read and matched with the Name column in the equipment_list.csv file
