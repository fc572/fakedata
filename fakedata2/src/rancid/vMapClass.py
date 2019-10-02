import csv
import os

class vMapClass:

    def open(self):
        return open(os.path.join(os.path.expanduser("~"), "Documents\\vMapClass.csv"), 'w', newline='')

    def column_name(self, writer):
        vmap_headers = ["name", "device", "cir	mincir", "policyMapIn", "policyMapOut", "bc", "fragment",
                        "fairQueue", "be"]
        writer.writerow(vmap_headers)
