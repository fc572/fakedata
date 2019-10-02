
from faker import Faker
from customdata.customData import CustomValues
from customdata.serviceBandwith import BandwithProvider
from rancid.vClassMap import vClassMap
from rancid.vClassMapMatchStatement import vClassMapMatchStatement
from rancid.vE1 import vE1
from rancid.vE1ChannelGroup import vE1ChannelGroup
from rancid.vMapClass import vMapClass
from rancid.vRateLimit import vRateLimit
from rancid.vVrf import vVrf
from rancid.vcSTM1 import vcSTM1
from rancid.vinterface import Vinterfacefile
from rancid.vpolicymap import PolicyMap
from rancid.vmappolicystatement import PolicyMapStatement


from utils import calculateSubnet
from utils import random_generator
from utils import fileUtils

fake = Faker('en_GB')
fake.add_provider(CustomValues)
fake.add_provider(BandwithProvider)

subnet = calculateSubnet.IpAddressUtilities()
rn = random_generator.RandomCustom()
fu = fileUtils.FileUtilities()


def rancid_files_generator(numberofnetworks):
    vint = Vinterfacefile()
    vpolicy_map = PolicyMap()
    vpolicy_map_statement = PolicyMapStatement()
    vcstm1 = vcSTM1()
    vrate_limit = vRateLimit()
    ve1 = vE1()
    ve1channel_group = vE1ChannelGroup()
    vmap_class = vMapClass()
    vclass_map = vClassMap()
    vclass_map_match_statement = vClassMapMatchStatement()
    vvrf = vVrf()

    vint_file_handle = vint.open()
    vint_writer = fu.writer(vint_file_handle)
    vint.column_name(vint_writer)

    vmapPolicy_file_handler = vpolicy_map.open()
    vmap_writer = fu.writer(vmapPolicy_file_handler)
    vpolicy_map.column_name(vmap_writer)

    vmapPolicyStatements_file_handle = vpolicy_map_statement.open()
    vmap_policy_statement_writer = fu.writer(vmapPolicyStatements_file_handle)
    vpolicy_map_statement.column_name(vmap_policy_statement_writer)

    vcstm1_file_handle = vcstm1.open()
    vcstm1_writer = fu.writer(vmapPolicyStatements_file_handle)
    vcstm1.column_name(vcstm1_writer)

    vrate_limit_file_handle = vrate_limit.open()
    vrate_limit_writer = fu.writer(vrate_limit_file_handle)
    vrate_limit.column_name(vrate_limit_writer)

    ve1_file_handle = ve1.open()
    ve1_writer = fu.writer(ve1_file_handle)
    ve1.column_name(ve1_writer)

    ve1channel_group_file_handle = ve1channel_group.open()
    ve1channel_group_writer = fu.writer(ve1channel_group_file_handle)
    ve1channel_group.column_name(ve1channel_group_writer)

    vmap_class_file_handle = vmap_class.open()
    vmap_class_writer = fu.writer(vmap_class_file_handle)
    vmap_class.column_name(vmap_class_writer)

    vclass_map_file_handle = vclass_map.open()
    vclass_map_writer = fu.writer(vclass_map_file_handle)
    vclass_map.column_name(vclass_map_writer)

    vclass_map_match_statement_file_handle = vclass_map_match_statement.open()
    vclass_map_match_statement_writer = fu.writer(vclass_map_match_statement_file_handle)
    vclass_map_match_statement.column_name(vclass_map_match_statement_writer)

    vvrf_file_handle = vvrf.open()
    vvrf_writer = fu.writer(vvrf_file_handle)
    vvrf.column_name(vvrf_writer)


    for _i in range(0, numberofnetworks):
        # take ip from fake library
        ip_address_with_mask = fake.ipv4(network=True, address_class=None, private=False)
        netmask = subnet.binary_value_to_decimal(subnet.subnet_value_in_binary(ip_address_with_mask))
        # use the submask to determine the addresses range and fill the spreadsheet with it
        ip_addresses = subnet.generate_ip_addresses_for_fake_network(ip_address_with_mask)
        # vmapPolicy

        parent = ""
        reserved_bandwith = ""
        atmpvc = ""
        high_availibility = ""

        # vmapPolicyStats

        for ip_address in ip_addresses:
            linetag = rn.random_letter(7)
            int_name = fake.custom_list("connection_type_names", 1) + '/' + rn.random_letter(2) + \
                       rn.random_number(3)

            if parent == "":
                parent = int_name
                reserved_bandwith = 1000
                atmpvc = rn.random_number(2) + '/' + rn.random_number(3)
                high_availibility = "TRUE"

            description = linetag + '|' + " some text " + '|' + "iscircuit-Number"

            in_or_out = rn.random_number(1)
            if int(in_or_out) < 5:
                policy_map_in = "MI-P-P-INPUT-" + linetag[:5] + '-' + rn.random_letter(3)
                policy_map_out = ""
            else:
                policy_map_out = "MI-P-P-OUTPUT-" + linetag[:5] + '-' + rn.random_letter(3)
                policy_map_in = ""

            device = rn.random_letter(2) + '-' + rn.random_letter(2) + '-' + rn.random_letter(3) + '-' + \
                    rn.random_letter(5) + rn.random_number(1)

            vint_writer.writerow([int_name, fake.word(), ip_address, netmask, description, policy_map_in,
                                        policy_map_out, parent, "False", rn.true_or_false_seeded(3), "False", "False",
                                        "", "", "", "False", "", linetag, "", "", "", fake.bandwidth(),
                                        reserved_bandwith,
                                        "", "", "", "False", "False", "False", atmpvc, "", "", "False", "False", "False",
                                        "", "False", device, high_availibility, "False", "False", "False", "False",
                                        "False", "False", "False", "False", "False", "False"])

            if policy_map_in != "":
                vmap_writer.writerow([policy_map_in, "", device])
                policy_name = policy_map_in
            else:
                vmap_writer.writerow([policy_map_out, "", device])
                policy_name = policy_map_out

            vmap_policy_statement_writer.writerow(["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", device, policy_name, ""])
            vmap_class_writer.writerow(["name", device])


    fu.close(vint_file_handle)
    fu.close(vmapPolicy_file_handler)
    fu.close(vmapPolicyStatements_file_handle)
    fu.close(vcstm1_file_handle)
    fu.close(vrate_limit_file_handle)
    fu.close(ve1_file_handle)
    fu.close(vmap_class_file_handle)
    fu.close(vclass_map_file_handle)
    fu.close(vclass_map_match_statement_file_handle)
    fu.close(vvrf_file_handle)