import csv
import os

class vcSTM1:

    def open(self):
        return open(os.path.join(os.path.expanduser("~"), "Documents\\vcSTM1.csv"), 'w', newline='')

    def column_name(self, writer):
        vmap_headers = ["cSTM1Name", "device", "description", "shutdown", "framing", "overhead", "augMapping", "mode",
                        "ais_shut", "sts_1", "clockSource", "delayTriggersLevel", "delayTriggersMsec"]
        writer.writerow(vmap_headers)
