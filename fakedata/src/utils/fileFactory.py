import os
import csv


class FileFactory:

    def open_file(self, file_name):
        return open(os.path.join(os.path.expanduser("~"), "Documents\\" + file_name + " "), 'w', newline='')

    def write_file_headers(self, file, file_headers):
        writer = csv.writer(file)
        writer.writerow(file_headers)
        return writer

    def close_all(self, networkDiscovery_file, equipment_on_site_file, equipment_file, account_file, customer_file, service_file):

        networkDiscovery_file.close()
        equipment_on_site_file.close()
        equipment_file.close()
        account_file.close()
        customer_file.close()
        service_file.close()
