import csv
import os

class vClassMap:

    def open(self):
        return open(os.path.join(os.path.expanduser("~"), "Documents\\vClassMap.csv"), 'w', newline='')

    def column_name(self, writer):
        vmap_headers = ["classMap", "matchCriteria", "description", "device"]
        writer.writerow(vmap_headers)
