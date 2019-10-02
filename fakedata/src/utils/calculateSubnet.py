
class IpAddressUtilities:

    def get_simple_ip(self, ip_address_with_subnet_mask):
        return ip_address_with_subnet_mask[:-3]

    def get_subnet_mask_from_ip(self, ip_address_with_subnet_mask):
        suffix = ip_address_with_subnet_mask[-2:]
        if suffix[0] == "/":
            return suffix[1]
        else:
            return suffix

    def subnet_value_in_binary(self, ip_address_with_subnet_mask):
        mask = int(self.get_subnet_mask_from_ip(ip_address_with_subnet_mask))
        bin_mask = ""

        for _i in range(mask):
            if _i > 0 and _i % 8 == 0:
                bin_mask += '.'
            bin_mask += '1'

        for _i in range(mask, 32):
            if _i % 8 == 0:
                bin_mask += '.'
            bin_mask += '0'
        return bin_mask

    def binary_value_to_decimal(self, bin_value):
        octets = bin_value.split('.')
        subnet_mask_decimal = ""
        for octet in octets:
            subnet_mask_decimal += str(int(octet, 2))
            subnet_mask_decimal += '.'
        return subnet_mask_decimal[:-1]

    def ip_to_binary(self, ip_address_with_subnet_mask):
        ip_address = self.get_simple_ip(ip_address_with_subnet_mask)
        ip_octets = ip_address.split('.')
        ip_in_binary = ""

        for octet in ip_octets:
            if octet == '':
                octet = 0
            octet = int(octet)
            binary = "{0:b}".format(octet)
            binary_len = len(binary)
            if binary_len < 8:
                binary = binary.rjust(8, "0")
            ip_in_binary = ip_in_binary + binary + '.'
        return ip_in_binary[:-1]

    def calculate_network_address(self, ip_address_in_binary, subnet_mask_binary):
        network_address = ""
        for pos in range(0, 35):
            if ip_address_in_binary[pos] == '.':
                network_address += '.'
            else:
                digit = int(ip_address_in_binary[pos]) & int(subnet_mask_binary[pos])
                network_address += str(digit)
        return network_address

    def calculate_broadcast_address(self, ip_address_with_subnet_mask):
        ip_bin = self.ip_to_binary(ip_address_with_subnet_mask)
        mask = self.get_subnet_mask_from_ip(ip_address_with_subnet_mask)
        int_mask = int(mask)
        host_part = ''

        for i in range(int_mask, 32):
            if i % 8 == 0:
                host_part += '.'
            host_part += '1'

        if int_mask < 9:
            network_addr = ip_bin[:int_mask]
        elif int_mask < 17:
            network_addr = ip_bin[:(int_mask + 1)] #one dots
        elif int_mask < 25:
            network_addr = ip_bin[:(int_mask + 2)] #two dots
        else:
            network_addr = ip_bin[:(int_mask + 3)] #three dots

        broadcast_address = network_addr + host_part
        broadcast_address_devimal = self.binary_value_to_decimal(broadcast_address)
        return broadcast_address

    def max_number_of_hosts(self, ip_address_with_subnet_mask):
        mask = self.get_subnet_mask_from_ip(ip_address_with_subnet_mask)
        max_number = 2 ** (32 - int(mask)) - 2
        print("max_number_hosts", max_number)
        return max_number

    def generate_ip_addresses_for_fake_network(self, ip_address_with_subnet_mask):
        addresses = []
        ip_bin = self.ip_to_binary(ip_address_with_subnet_mask)
        subnet_bin = self.subnet_value_in_binary(ip_address_with_subnet_mask)

        network_address = self.calculate_network_address(ip_bin, subnet_bin)

        ip_broad = self.calculate_broadcast_address(ip_address_with_subnet_mask)

        start_host_address = self.binary_value_to_decimal(network_address)
        end_host_address = self.binary_value_to_decimal(ip_broad)

        strings_start_ip_octets = start_host_address.split('.')
        strings_end_ip_octets = end_host_address.split('.')

        start_ip_octets = []
        end_ip_octets = []

        for s_octects in strings_start_ip_octets:
            start_ip_octets.append(int(s_octects))

        for l_octects in strings_end_ip_octets:
            end_ip_octets.append(int(l_octects))

        def oct4(start4_ip_octets, end4_ip_octets, first_term=start_ip_octets[0], second_term=start_ip_octets[1],
                 third_term=start_ip_octets[2]):
            while start4_ip_octets != end4_ip_octets:
                self.form_ip_addresses(addresses, first_term, second_term, third_term, start4_ip_octets)
                start4_ip_octets += 1

        def oct3(start3_ip_octets, end3_ip_octets, first_term=start_ip_octets[0], second_term=start_ip_octets[1],
                 fourth_term=start_ip_octets[3]):
            while start3_ip_octets != end3_ip_octets:
                start_ip_octets[3] = int(strings_start_ip_octets[3])
                self.form_ip_addresses(addresses, first_term, second_term, start3_ip_octets, fourth_term)
                start3_ip_octets += 1
                oct4(start_ip_octets[3], end_ip_octets[3], first_term, second_term, start3_ip_octets)

        def oct2(start2_ip_octets, end2_ip_octets, first_term=start_ip_octets[0], third_term=start_ip_octets[2],
                 fourth_term=start_ip_octets[3]):
            while start2_ip_octets != end2_ip_octets:
                start_ip_octets[2] = int(strings_start_ip_octets[2])
                self.form_ip_addresses(addresses, first_term, start2_ip_octets, third_term, fourth_term)
                start2_ip_octets += 1
                oct3(start_ip_octets[2], end_ip_octets[2], first_term, start2_ip_octets, fourth_term)

        def oct1(start1_ip_octets, end1_ip_octets, second_term=start_ip_octets[1], third_term=start_ip_octets[2],
                 fourth_term=start_ip_octets[3]):
            while start1_ip_octets != end1_ip_octets:
                start_ip_octets[1] = int(strings_start_ip_octets[1])
                self.form_ip_addresses(addresses, start1_ip_octets, second_term, third_term, fourth_term)
                start1_ip_octets += 1
                oct2(start_ip_octets[1], end_ip_octets[1], start1_ip_octets, third_term, fourth_term)

        oct4(start_ip_octets[3], end_ip_octets[3])

        oct3(start_ip_octets[2], end_ip_octets[2])

        oct2(start_ip_octets[1], end_ip_octets[1])

        oct1(start_ip_octets[0], end_ip_octets[0])

        return addresses

    def form_ip_addresses(self, addresses, n1, n2, n3, n4):
        return addresses.append(str(n1) + '.' + str(n2) + '.' + str(n3) + '.' + str(n4))