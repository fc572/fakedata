import csv
import os

class vClassMapMatchStatement:

    def open(self):
        return open(os.path.join(os.path.expanduser("~"), "Documents\\vClassMapMatchStatement.csv"), 'w', newline='')

    def column_name(self, writer):
        vmap_headers = ["matchAny", "matchIpRtpPort", "matchIpPrecedence", "matchIpDscp", "matchAccessGroup",
                        "matchProtocolHttp", "matchMplsExpTopmost", "matchMplsExp", "matchIpRtpRange", "matchQoSGroup",
                        "matchGenericProtocol", "matchClassMap", "sequence", "classMap", "device"]
        writer.writerow(vmap_headers)
