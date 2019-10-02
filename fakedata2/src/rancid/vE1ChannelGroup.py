import csv
import os

class vE1ChannelGroup:

    def open(self):
        return open(os.path.join(os.path.expanduser("~"), "Documents\\vE1ChannelGroup.csv"), 'w', newline='')

    def column_name(self, writer):
        vmap_headers = ["E1Name", "device", "channelNumber", "timeslots", "unframed"]
        writer.writerow(vmap_headers)
