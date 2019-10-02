import csv
import os

class vVrf:

    def open(self):
        return open(os.path.join(os.path.expanduser("~"), "Documents\\vVrf.csv"), 'w', newline='')

    def column_name(self, writer):
        vmap_headers = ["vrfName", "rd", "rtExportPrimary", "rtImportPrimary", "rtExportList", "rtImportList",
                        "maxRoutes", "maxRoutesNotify", "importMap", "exportMap", "device", "description"]
        writer.writerow(vmap_headers)
