import csv
import os

class vE1:

    def open(self):
        return open(os.path.join(os.path.expanduser("~"), "Documents\\vE1.csv"), 'w', newline='')

    def column_name(self, writer):
        vmap_headers = ["name", "device", "description", "shutdown", "framing", "priGroupTimeslots", "clockSource",
                        "ccsVoice"]
        writer.writerow(vmap_headers)
