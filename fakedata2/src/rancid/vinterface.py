import csv
import os


class Vinterfacefile:

    def open(self):
        return open(os.path.join(os.path.expanduser("~"), "Documents\\vinterface.csv"), 'w', newline='')

    def column_name(self, writer):
        vinterface_headers = ["intName", "vrfName", "ipAddress", "netmask", "description", "policyMapIn",
                              "policyMapOut",
                              "parent", "isChannelGroup", "shutdown", "runLdp", "runXConnect", "frClass",
                              "accessGroupIn",
                              "accessGroupOut", "rateLimit", "multilinkGroup", "lineTag", "ospfMessageDigestKeyId",
                              "ospfMessageDigestPassword", "ospfMessageDigestPasswordEncrypted", "bandwidth",
                              "maxReservedBandwidth", "ipVerifyAcl", "uRPF", "frDlci", "mplsNetFlowEgress",
                              "ipRouteCacheFlow", "ipUnnumbered", "atmPvc", "atmPolicyMapIn", "atmPolicyMapOut",
                              "isFrameRelay", "frTrafficShaping", "loadSharePerPacket", "encapsulation",
                              "ipRTPHeaderCompression", "device", "highAvailabilityConfigured", "switchport",
                              "ipDirectedBroadcast", "ipRedirects", "ipUnreachables", "ipProxyArp", "clnsRouteCache",
                              "mplsForwarding", "mplsTrafficEngTunnels", "runCdp", "portSecurityConfigured",
                              "switchportMode", "mplsLabelProtocol", "tagRewrite", "snmpLinkStatus", "loggingEvent",
                              "ipArpInspectionLimit", "ipPimMode", "repPortType", "ethernetVlanColorBlock", "mediaType",
                              "udld", "mtu", "ipMtu", "mplsMtu", "loadInterval", "firstVlan", "secondVlan",
                              "bridgeDomain",
                              "ipPimDrPriority", "repSegment", "ospfCost", "keepalive"]

        writer.writerow(vinterface_headers)
