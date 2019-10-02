import csv
import os

class vRateLimit:

    def open(self):
        return open(os.path.join(os.path.expanduser("~"), "Documents\\vRateLimit.csv"), 'w', newline='')

    def column_name(self, writer):
        vmap_headers = ["sequence", "device", "policeCir", "policeBc", "policeBe", "direction", "accessGroup",
                        "conformAction", "exceedAction", "intName", "conformTransformValue", "conformTransformType",
                        "exceedTransformValue", "exceedTransformType"]
        writer.writerow(vmap_headers)