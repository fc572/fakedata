import random

from faker.providers import BaseProvider


# Our custom provider inherits from the BaseProvider
class CustomValues(BaseProvider):

    def custom_list(self, word_list, sentence_length):
        data_dictionary = {
                              "fake_site_name": ["Residential", "Business", ""],
                              "fake_service_name": ["12Mbps Business Plus", "1Mbps Value", "2Mbps Value",
                                                    "3Mbps Value+",
                                                    "5Mbps Business Plus",
                                                    "8Mbps Business Plus", "Broadband XL 30Mbps", "Broadband Xtra",
                                                    "Broadband XXL 50Mbps",
                                                    "Business Wireless 12Mbps", "Business Wireless 5Mbps",
                                                    "Business Wireless 8Mbps",
                                                    "Freedom Extra (wireless)",
                                                    "Freedom unlimited (pro)", "Freedom unlimited 30Mb",
                                                    "Freedom unlimited 50Mb",
                                                    "Freedom unlimited 8Mb",
                                                    "Freedom unlimited xtra", "Freedom XL 30Mbps", "Freedom XXL 50Mbps",
                                                    "Home starter (Internet essentials)",
                                                    "Internet + phone + TV essentials", "Weekend and Evening FlexiMax",
                                                    "Weekend Flexi"],
                              "fake_product_code": ["B1HD", "B1HDW", "B1LO", "B1LOW", "B1MD", "B1MDW", "C3PO", "R2D2",
                                                    "R2HD", "R2HDW",
                                                    "R2LO",
                                                    "R2LOW", "R2MD", "R2MDW", "R3HD", "R3HDW", "R3LO", "R3LOW", "R3MD",
                                                    "R3MDW"],
                              "fake_payment_method": ["DD", "X", ""],
                              "fake_bill_cycle": [1, 2, 3]
        }
        return ''.join(random.sample(data_dictionary[word_list], sentence_length))

    def equipment_list(self, sentence_length=0, pos=-1):
        fake_equipment_list = [['1', 'Baltic 125R', '6', '100', '1', '4'],
                               ['2', 'Baltic 800', '88', '150', '2', '4'],
                               ['3', 'Baltic 8002', '168', '150', '3', '4'],
                               ['4', 'Baltic 8004', '168', '150', '4', 'NULL'],
                               ['5', 'Baltic P-660HN', '99', '150', '5', '7'],
                               ['6', 'Baltic P-660FK', '99', '150', '6', '7'],
                               ['7', 'Baltic P-660FK2', '99', '150', '7', 'NULL'],
                               ['8', 'Iris 8133K', '40', '0', '8', '14'],
                               ['9', 'Iris 8133U', '45', '0', '9', '14'],
                               ['10', 'Iris DSL-B13', '20', '0', '10', '13'],
                               ['11', 'Netgo BR-6214', '788', '350', '11', '12'],
                               ['12', 'Netgo BR-6214K', '788', '350', '12', 'NULL'],
                               ['13', 'Netgo DGV558-100', '598', '350', '13', '14'],
                               ['14', 'Netgo DSL-260R', '609', '350', '14', 'NULL'],
                               ['15', 'Netgo DSL-580', '609', '350', '15', '16'],
                               ['16', 'Netgo DSL-590', '609', '350', '16', 'NULL']]

        if pos < 0:
            return fake_equipment_list
        else:
            line = random.sample(fake_equipment_list, sentence_length)
            return line[0]
