import csv
import os

class PolicyMap:

    def open(self):
        return open(os.path.join(os.path.expanduser("~"), "Documents\\vpolicyMap.csv"), 'w', newline='')

    def column_name(self, writer):
        vmap_headers = ["name", "description", "device"]
        writer.writerow(vmap_headers)
