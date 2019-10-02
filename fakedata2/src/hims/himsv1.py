from faker import Faker
import csv
import os

fake = Faker('en_GB')

def himsv1_file_generator(numberofrows):

    hims_headers = ["ServerID", "ServerName", "DNSName", "Owner", "Responsability", "OS", "Version", "Status", "ClientName",
                    "Siebel", "Backups", "AccountID", "Room", "Cabinet", "Row", "Shelf", "Location", "Vault", "VaultNo",
                    "Switchname", "Switchport", "Patchpoint", "Manufacturer", "Model", "PSU", "Power", "Height", "RAM",
                    "Serial", "ISSerial", "MaintType", "MaintVendor", "MaintStart", "MaintEnd", "IP", "SubNet", "NIC",
                    "Category", "Port", "CommunityRO", "CommunityRW", "SNMPManaged", "ISMManaged", "ServiceManaged",
                    "ServicePurchased", "ISMPurchased", "SNMPPurchased", "ISMChanged", "SNMPChanged", "ServiceChanged",
                    "IEng", "TEng", "Idate", "Sdate", "SEng", "Ddate", "DEng", "Alias", "HDDConfig", "ProcessorNum",
                    "ProcessorHT", "Processor", "ProcessorSpeed", "MAC", "DisableReason", "MonitorFrom", "Notification",
                    "BackupName", "Datalog", "ProvisionID"]

    # hims file
    csv_hims_file = open(os.path.join(os.path.expanduser("~"), "Documents\\hims.csv"), 'w')
    hims_writer = csv.writer(csv_hims_file)
    hims_writer.writerow(hims_headers)


    count = 0
    for _i in range(numberofrows):

        hims_writer.writerow([])

        count = count + 1

    csv_hims_file.close()