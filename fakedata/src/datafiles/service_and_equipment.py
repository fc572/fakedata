from faker import Faker

from src.customproviders.serviceTag import TagsProvider
from src.customproviders.serviceBandwidth import BandwidthProvider
from src.customproviders.serialNumber import SerialNumbers
from src.customproviders.documentNumber import DocumentNumbers
from src.data.customData import CustomValues
from src.my_project_utils import random_generator, calculateSubnet
from src.my_project_utils import fileFactory
from src.datafiles import networkDiscovery


class FileGeneration:

    @staticmethod
    def file_generator_iterations(number_of_networks):

        fake = Faker('en_GB')

        # Add the dataProviders to our faker object
        fake.add_provider(TagsProvider)
        fake.add_provider(BandwidthProvider)
        fake.add_provider(SerialNumbers)
        fake.add_provider(CustomValues)
        fake.add_provider(DocumentNumbers)

        customer_headers = ["ServiceID", "ServiceName", "CustomerName", "CustomerAccount", "SiteName", "SiteAddress",
                            "playsGuitar"]
        service_headers = ["ServiceTag", "ServiceBandwidth", "InterfaceIpAddress", "EquipmentSerial", "EquipmentModel",
                           "SiteName", "SiteAddress"]
        account_headers = ["Account Name", "Bill Number", "Payment Method", "Bill Date", "Bill Cycle",
                           "Document Number",
                           "Line Rental", "Bill Total", "Service Code", "Product Code"]
        equipment_headers = ["ModelId", "Name", "InStock", "OnOrder", "ManufacturerId", "UpgradeToModelId"]
        equipment_on_site_headers = ["ObjectId", "EntityName", "EntityType", "IpAddress", "SubnetMask", "Subnet",
                                     "LocalNbrPhysAddr", "IfAdminStatus", "IfSpeed", "IsActive"]

        rn = random_generator.RandomCustom()
        rn.random_seed(3)
        subnet = calculateSubnet.IpAddressUtilities()
        ndf = networkDiscovery.CreateTextContent()
        ff = fileFactory.FileFactory()

        # service file
        service_file = ff.open_file("service_and_equipment.csv")
        service_writer = ff.write_file_headers(service_file, service_headers)

        # customer file
        customer_file = ff.open_file("customer_site_and_service.csv")
        customer_writer = ff.write_file_headers(customer_file, customer_headers)

        # customer account
        account_file = ff.open_file("account_details.csv")
        account_writer = ff.write_file_headers(account_file, account_headers)

        # equipment file
        equipment_file = ff.open_file("equipment_list.csv")
        equipment_writer = ff.write_file_headers(equipment_file, equipment_headers)

        # customer equipment file
        equipment_on_site_file = ff.open_file("equipment_on_site.csv")
        equipment_on_site_writer = ff.write_file_headers(equipment_on_site_file, equipment_on_site_headers)

        # network discovery file
        network_discovery_file = ff.open_file("networkDiscoveryFile.rdf")
        network_discovery_file.write(ndf.networkdiscoveryentries())

        for line in fake.equipment_list():
            equipment_writer.writerow(line)
        ff.close_file(equipment_file)

        for _i in range(number_of_networks):
            # address_class is of type b or c because type a takes too long.
            # address_class=fake.ipv4_network_class() to have options a,b or c available
            # change to address_class=rn.random_b_or_c() for smaller networks of type b or c

            flag = True
            while flag:
                ip_address_with_mask = fake.ipv4_public(network=True, address_class=rn.random_b_or_c())
                ip_addresses = subnet.generate_ip_addresses_for_fake_network(ip_address_with_mask)

                # make sure that there are less than X ips in the network
                if subnet.max_number_of_hosts(ip_address_with_mask) < 1000:
                    flag = False

            print("Printing network number ", (_i + 1), " of ", number_of_networks)
            subnet_mask = subnet.get_subnet_mask_from_ip(ip_address_with_mask)
            m_subnet = subnet.binary_value_to_decimal(subnet.subnet_value_in_binary(ip_address_with_mask))
            equipment_on_site_obj_id = 1
            object_1_id = rn.random_number(3)

            # obj1 and obj2
            object2_id = 1
            name = fake.domain_word()
            assoc_index_number = int(rn.random_number(3))
            assoc_index_number_for_obj1 = []
            if_oper_status_for_obj1 = []
            if_number = int(rn.random_number(3))
            if_index = int(rn.random_number(1))
            if_index_for_obj1 = []
            entity_oid = "1.2.3.{}.{}.{}.{}".format(assoc_index_number, object_1_id, if_index, if_number)

            print("len(ip_addresses) ", len(ip_addresses))

            # end obj1 and obj2
            for ip_address in ip_addresses:
                customer_name = fake.name()
                customer_account_number = rn.random_number(4)
                service_id = rn.random_number(5)
                site_name = fake.custom_list("fake_site_name", 1)
                site_address = fake.street_address()
                bill_cycle = rn.random_range(1, 3)
                line_rental = rn.random_range(0, 11)
                bill_total = (rn.random_number(3) + '.' + rn.random_number(2))
                line = fake.equipment_list(1, 1)
                equipment_name = line[1]
                equipment_manufacturer_id = line[4]
                bandwidth = fake.bandwidth()
                local_nbr_phys_addr = fake.mac_address()
                if_admin_status = rn.one_or_two_seeded(3)
                if_oper_status = rn.one_or_two_seeded(8)
                plays_guitar = rn.true_or_false_seeded(3)

                if site_name:
                    service_code = site_name[:1]
                else:
                    service_code = ""

                equipment_on_site_writer.writerow(
                    [equipment_on_site_obj_id, equipment_name, equipment_manufacturer_id, ip_address, subnet_mask,
                     m_subnet, local_nbr_phys_addr, rn.random_range(0, 1), bandwidth, 1]
                )
                equipment_on_site_file.flush()

                equipment_on_site_obj_id += 1
                service_writer.writerow(
                    [fake.tag(service_id), bandwidth, ip_address, fake.serial_number(), equipment_name, site_name,
                     site_address]
                )
                service_file.flush()

                customer_writer.writerow(
                    [service_id, fake.custom_list("fake_service_name", 1), customer_name, customer_account_number,
                     site_name, site_address, plays_guitar])
                customer_file.flush()

                account_writer.writerow(
                    [customer_name, rn.random_number(2), fake.custom_list("fake_payment_method", 1),
                     fake.date(pattern="%d/%m/%Y"), bill_cycle, fake.document_number(customer_account_number),
                     line_rental,
                     bill_total, service_code, fake.custom_list("fake_product_code", 1)]
                )
                account_file.flush()

                network_discovery_file.write(ndf.networkdiscoveryobj2(name, str(object2_id), str(assoc_index_number),
                                                                      str(if_admin_status),
                                                                      str(if_oper_status), str(if_index), entity_oid,
                                                                      ip_address, subnet_mask, m_subnet,
                                                                      local_nbr_phys_addr) + "\n")

                network_discovery_file.flush()
                assoc_index_number_for_obj1.append(assoc_index_number)
                if_oper_status_for_obj1.append(if_oper_status)
                if_index_for_obj1.append(if_index)
                object2_id += 1
                assoc_index_number += 1
                if_number += 1
                if_index += 1

            network_discovery_file.write(ndf.networddiscoveryobj1(object_1_id, name, str(assoc_index_number_for_obj1),
                                                                  str(if_oper_status_for_obj1), str(if_index_for_obj1),
                                                                  entity_oid) + "\n")

            network_discovery_file.flush()

        ff.close_file(network_discovery_file, equipment_on_site_file, account_file, customer_file, service_file)
