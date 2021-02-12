class CreateTextContent:
    def networkdiscoveryentries(self):
        return (
            "\n @prefix : <http://ontology.com/queryResultViewExport#> . \
             \n@base <http://ontology.com/queryResultViewExport> .\
            \nnetwork_discovery:Entity\
              \na rdfs:Class , owl:Class ;\
              \nrdfs:subClassOf owl:Thing .\
            \nnetwork_discovery:entityActionType\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:Entity .\
            \nnetwork_discovery:entityChangeTime\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:Entity .\
            \nnetwork_discovery:entityClassName\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:Entity .\
            \nnetwork_discovery:entityCreateTime\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:Entity .\
            \nnetwork_discovery:entityDescription\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:Entity .\
            \nnetwork_discovery:entityFileUri\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:Entity .\
            \nnetwork_discovery:entityHasExtraInfo\
              \na owl:ObjectProperty ;\
              \nrdfs:domain network_discovery:Entity ;\
              \nrdfs:range network_discovery:ExtraInfo .\
            \nnetwork_discovery:entityIsActive\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:Entity .\
            \nnetwork_discovery:entityLingerTime\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:Entity .\
            \nnetwork_discovery:entityName\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:Entity .\
            \nnetwork_discovery:entityObjectId\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:Entity .\
            \nnetwork_discovery:entityOid\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:Entity .\
            \nnetwork_discovery:entityPosition\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:Entity .\
            \nnetwork_discovery:entityType\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:Entity .\
            \nnetwork_discovery:ExtraInfo\
              \na rdfs:Class , owl:Class ;\
              \nrdfs:subClassOf owl:Thing .\
            \nnetwork_discovery:extraInfoEntityPosition\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoHasMAssocIndex\
              \na owl:ObjectProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo ;\
              \nrdfs:range network_discovery:MAssocIndex .\
              \nnetwork_discovery:extraInfoHasMBgpPeers\
              \na owl:ObjectProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo ;\
              \nrdfs:range network_discovery:MBgpPeers .\
            \nnetwork_discovery:extraInfoHasMIfIndex\
              \na owl:ObjectProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo ;\
              \nrdfs:range network_discovery:MIfIndex .\
            \nnetwork_discovery:extraInfoHasMIfOperStatus\
              \na owl:ObjectProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo ;\
              \nrdfs:range network_discovery:MIfOperStatus .\
            \nnetwork_discovery:extraInfoHasMMplsvpnmemberships\
              \na owl:ObjectProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo ;\
              \nrdfs:range network_discovery:MMplsvpnmemberships .\
            \nnetwork_discovery:extraInfoHasMMultiNetList\
              \na owl:ObjectProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo ;\
              \nrdfs:range network_discovery:MMultiNetList .\
            \nnetwork_discovery:extraInfoHasMMultiNetMask\
              \na owl:ObjectProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo ;\
              \nrdfs:range network_discovery:MMultiNetMask .\
            \nnetwork_discovery:extraInfoHasMMultiNetSubnet\
              \na owl:ObjectProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo ;\
              \nrdfs:range network_discovery:MMultiNetSubnet .\
            \nnetwork_discovery:extraInfoHasMVpnroutingData\
              \na owl:ObjectProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo ;\
              \nrdfs:range network_discovery:MVpnroutingData .\
            \nnetwork_discovery:extraInfoMAddressSpace\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo ;\
              \nrdfs:range xsd:boolean .\
            \nnetwork_discovery:extraInfoMAs\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMBaseName\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMDeviceId\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMIfAdminStatus\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMIfConnectorPresent\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMIfDescr\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMIfHighSpeed\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMIfMtu\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMIfName\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMIfNumber\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMIfPromiscuousMode\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMIfSpeed \
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMIfType\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMIpAddress\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMIpForwarding\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
              \nnetwork_discovery:extraInfoMLocalNbrPhysAddr\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMLocalNbrStatus\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMNoPing\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMSubnet\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMSubnetMask\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMSysContact\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain \nnetwork_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMSysDescr\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMSysName\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMSysServices\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:extraInfoMSysUpTime\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:ExtraInfo .\
            \nnetwork_discovery:MAssocIndex\
              \na rdfs:Class , owl:Class ;\
              \nrdfs:subClassOf owl:Thing .\
            \nnetwork_discovery:mAssocIndexEntityPosition\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain \nnetwork_discovery:MAssocIndex .\
            \nnetwork_discovery:mAssocIndexListItem\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain \nnetwork_discovery:MAssocIndex .\
            \nnetwork_discovery:MBgpPeers\
              \na rdfs:Class , owl:Class ;\
              \nrdfs:subClassOf owl:Thing .\
            \nnetwork_discovery:mBgpPeersEntityPosition\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain \nnetwork_discovery:MBgpPeers .\
            \nnetwork_discovery:mBgpPeersListItem\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MBgpPeers .\
            \nnetwork_discovery:MExportRts\
              \na rdfs:Class , owl:Class ;\
              \nrdfs:subClassOf owl:Thing .\
            \nnetwork_discovery:mExportRtsEntityPosition\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MExportRts .\
            \nnetwork_discovery:mExportRtsListItem\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MExportRts .\
            \nnetwork_discovery:MIfIndex\
              \na rdfs:Class , owl:Class ;\
              \nrdfs:subClassOf owl:Thing .\
            \nnetwork_discovery:mIfIndexContent\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MIfIndex .\
            \nnetwork_discovery:mIfIndexEntityPosition\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MIfIndex .\
            \nnetwork_discovery:mIfIndexListItem\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MIfIndex .\
            \nnetwork_discovery:MIfOperStatus\
              \na rdfs:Class , owl:Class ;\
              \nrdfs:subClassOf owl:Thing .\
            \nnetwork_discovery:mIfOperStatusContent\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MIfOperStatus .\
            \nnetwork_discovery:mIfOperStatusEntityPosition\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MIfOperStatus .\
            \nnetwork_discovery:mIfOperStatusListItem\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MIfOperStatus .\
            \nnetwork_discovery:MImportRts\
              \na rdfs:Class , owl:Class ;\
              \nrdfs:subClassOf owl:Thing .\
            \nnetwork_discovery:mImportRtsEntityPosition\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MImportRts .\
            \nnetwork_discovery:mImportRtsListItem\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MImportRts .\
            \nnetwork_discovery:MMplsvpnmemberships\
              \na rdfs:Class , owl:Class ;\
              \nrdfs:subClassOf owl:Thing .\
            \nnetwork_discovery:mMplsvpnmembershipsEntityPosition\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MMplsvpnmemberships .\
            \nnetwork_discovery:mMplsvpnmembershipsListItem\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MMplsvpnmemberships .\
            \nnetwork_discovery:MMultiNetList\
              \na rdfs:Class , owl:Class ;\
              \nrdfs:subClassOf owl:Thing .\
            \nnetwork_discovery:mMultiNetListEntityPosition\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MMultiNetList .\
            \nnetwork_discovery:mMultiNetListListItem\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MMultiNetList .\
            \nnetwork_discovery:MMultiNetMask\
              \na rdfs:Class , owl:Class ;\
              \nrdfs:subClassOf owl:Thing .\
            \nnetwork_discovery:mMultiNetMaskEntityPosition\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MMultiNetMask .\
            \nnetwork_discovery:mMultiNetMaskListItem\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MMultiNetMask .\
            \nnetwork_discovery:MMultiNetSubnet\
              \na rdfs:Class , owl:Class ;\
              \nrdfs:subClassOf owl:Thing .\
            \nnetwork_discovery:mMultiNetSubnetEntityPosition\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MMultiNetSubnet .\
            \nnetwork_discovery:mMultiNetSubnetListItem\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MMultiNetSubnet .\
            \nnetwork_discovery:MVpnroutingData\
              \na rdfs:Class , owl:Class ;\
              \nrdfs:subClassOf owl:Thing .\
            \nnetwork_discovery:mVpnroutingDataEntityPosition\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MVpnroutingData .\
            \nnetwork_discovery:mVpnroutingDataHasMExportRts\
              \na owl:ObjectProperty ;\
              \nrdfs:domain network_discovery:MVpnroutingData ;\
              \nrdfs:range network_discovery:MExportRts .\
            \nnetwork_discovery:mVpnroutingDataHasMImportRts\
              \na owl:ObjectProperty ;\
              \nrdfs:domain network_discovery:MVpnroutingData ;\
              \nrdfs:range network_discovery:MImportRts .\
            \nnetwork_discovery:mVpnroutingDataMLabelImpositionData\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MVpnroutingData ;\
              \nrdfs:range xsd:boolean .\
            \nnetwork_discovery:mVpnroutingDataMRd\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MVpnroutingData .\
            \nnetwork_discovery:mVpnroutingDataMVrfName\
              \na owl:DatatypeProperty ;\
              \nrdfs:domain network_discovery:MVpnroutingData ."
        )

    def networddiscoveryobj1(
            self,
            object_1_id,
            name,
            assoc_index_number_for_obj1,
            if_oper_status_for_obj1,
            if_index_for_obj1,
            if_number,
            timestamp,
            entity_oid,
    ):
        return (
                "\n[]\
              \na network_discovery:Entity ; \
              \nrdfs:label \"Entity "
                + object_1_id
                + "; "
                + name
                + "; 1\" ; \
            \nnetwork_discovery:entityObjectId \""
                + object_1_id
                + "\";  \
            \nnetwork_discovery:entityName \"ddl5-"
                + name
                + "-gt1\"; \
            \nnetwork_discovery:entityDescription \"Cisco Internetwork Operating System Software IOS (tm) 7200 Software (C7200-P-M) \
            Version 12.3(1a), RELEASE SOFTWARE (fc1) Copyright(c)1986 - 2003 by cisco Systems, Inc.\";  \
            \nnetwork_discovery:entityType \"1\";\
            \nnetwork_discovery:entityOid \""
                + entity_oid
                + "\" ; \
            \nnetwork_discovery:entityHasExtraInfo [ a network_discovery:ExtraInfo ; \
                \n\trdfs:label \"ExtraInfo\" ; \
                \n\tnetwork_discovery:extraInfoEntityPosition \"Line "
                + object_1_id
                + "\" ; \
                \n\tnetwork_discovery:extraInfoMIpForwarding \"1\";\
                \n\tnetwork_discovery:extraInfoMSysName \"ddl5-"
                + name
                + "-gt1\";\
                \n\tnetwork_discovery:extraInfoMSysDescr \"DESCRIPTION\";\
                \n\tnetwork_discovery:extraInfoMSysUpTime \"89971641\";\
                \n\tnetwork_discovery:extraInfoMSysServices \"6\";\
                \n\tnetwork_discovery:extraInfoMIfNumber \""
                + if_number
                + "\" ; \
                \n\tnetwork_discovery:extraInfoHasMAssocIndex [ a network_discovery:MAssocIndex ;\
                    \n\t\trdfs:label \""
                + assoc_index_number_for_obj1
                + "\"; \
                    \n\t\tnetwork_discovery:mAssocIndexEntityPosition \"Line"
                + assoc_index_number_for_obj1
                + "\"; \
                    \n\t\tnetwork_discovery:mAssocIndexListItem  \""
                + assoc_index_number_for_obj1
                + "\" ] ; \
                    \n\tnetwork_discovery:extraInfoHasMIfIndex [ a network_discovery:MIfIndex ; \
                    \n\t\trdfs:label \"MIfIndex"
                + if_index_for_obj1
                + "\"; \
                    \n\t\tnetwork_discovery:mIfIndexEntityPosition \"Line "
                + if_index_for_obj1
                + "\" ;\
                    \n\t\tnetwork_discovery:mIfIndexListItem \""
                + if_index_for_obj1
                + "\"] ;\
                    \n\tnetwork_discovery:extraInfoHasMIfOperStatus [ a network_discovery:MIfOperStatus ; \
                    \n\t\trdfs:label \"MIfOperStatus"
                + if_oper_status_for_obj1
                + "\"; \
                    \n\t\tnetwork_discovery:mIfOperStatusEntityPosition \"Line "
                + if_oper_status_for_obj1
                + "\"; \
                    \n\t\tnetwork_discovery:mIfOperStatusListItem \""
                + if_oper_status_for_obj1
                + "\"] ;\
                 \n];\
            \nnetwork_discovery:extraInfoMBaseName \""
                + name
                + "\"  ; \
            \nnetwork_discovery:extraInfoMAddressSpace \"true\"; \
            \nnetwork_discovery:entityActionType  \"0\";\
            \nnetwork_discovery:entityIsActive \"1\";\
            \nnetwork_discovery:entityLingerTime \"3\";\
            \nnetwork_discovery:entityCreateTime \""
                + timestamp
                + "\"  ; \
            \nnetwork_discovery:entityChangeTime \""
                + timestamp
                + "\"  ; \
            \nnetwork_discovery:entityClassName \"Cisco72xx  \". "
        )

    def networkdiscoveryobj2(
            self,
            name,
            object2_id,
            assoc_index_number,
            if_admin_status,
            if_oper_status,
            if_index,
            entity_oid,
            ip_address,
            timestamp,
            subnet_mask,
            m_subnet,
            localnbrphysaddr,
    ):
        return (
                "\n[]\
              \na network_discovery:Entity ; \
                \nrdfs:label \"Entity "
                + object2_id
                + "," + name
                + "[0 ["
                + object2_id
                + "] ], 2\" ; \
            \nnetwork_discovery:entityObjectId \""
                + object2_id
                + "\"; \
            \nnetwork_discovery:entityName \""
                + name
                + "[0 ["
                + assoc_index_number
                + "] ]\"; \
            \nnetwork_discovery:entityType \"2\"; \
            \nnetwork_discovery:entityOid \""
                + entity_oid
                + "\"; \
            \nnetwork_discovery:entityHasExtraInfo [ a network_discovery:ExtraInfo ; \
              \n\trdfs:label\"ExtraInfo "
                + object2_id
                + "; "
                + ip_address
                + "; "
                + subnet_mask
                + "\" ; \
                      \n\tnetwork_discovery:extraInfoEntityPosition \"Line "
                + entity_oid
                + "\" ; \
                      \n\tnetwork_discovery:extraInfoHasMIfIndex [ a network_discovery:MIfIndex ; \
                      \n\trdfs:label \"MIfIndex"
                + if_index
                + " \"; \
                      \n\tnetwork_discovery:mIfIndexContent \""
                + if_index
                + "\" ] ; \
                      \n\tnetwork_discovery:extraInfoMIfType \"135\"; \
                      \n\tnetwork_discovery:extraInfoMIpAddress \""
                + ip_address
                + "\"; \
                      \n\tnetwork_discovery:extraInfoMSubnetMask \""
                + subnet_mask
                + "\"; \
                      \n\tnetwork_discovery:extraInfoMSubnet \""
                + m_subnet
                + "\"; \
                      \n\tnetwork_discovery:extraInfoMLocalNbrPhysAddr \""
                + localnbrphysaddr
                + "\"; \
                      \n\tnetwork_discovery:extraInfoMIfAdminStatus \""
                + if_admin_status
                + "\"; \
                      \n\tnetwork_discovery:extraInfoHasMIfOperStatus [ a network_discovery:MIfOperStatus ; \
                         \n\t\trdfs:label \"MIfOperStatus "
                + if_oper_status
                + "\" ; \
                         \n\t\tnetwork_discovery:mIfOperStatusContent \""
                + if_oper_status
                + "\" ] ; \
                      \n\tnetwork_discovery:extraInfoMIfDescr \"GigabitEthernet6/0.20\"; \
                      \n\tnetwork_discovery:extraInfoMIfName \"Gi6/0.20\"; \
                      \n\tnetwork_discovery:extraInfoMIfSpeed \"2560000\"; \
                      \n\tnetwork_discovery:extraInfoMIfMtu \"1500\"; \
                      \n\tnetwork_discovery:extraInfoMIfHighSpeed \"3\"; \
                      \n\tnetwork_discovery:extraInfoMIfPromiscuousMode \"2\"; \
                      \n\tnetwork_discovery:extraInfoMIfConnectorPresent \"2\"; \
                      \n\tnetwork_discovery:extraInfoHasMVpnroutingData [ a network_discovery:MVpnroutingData ; \
                          \n\t\trdfs:label \"MVpnroutingData Prontodynamics; "
                + object2_id
                + ":"
                + assoc_index_number
                + ", true \"; \
                          \n\t\tnetwork_discovery:mVpnroutingDataMVrfName \"Prontodynamics\"; \
                          \n\t\tnetwork_discovery:mVpnroutingDataMRd \"3741:659\"]; \
                          \n\t\tnetwork_discovery:mVpnroutingDataHasMExportRts [ a network_discovery:MExportRts ; \
                             \n\t\t\trdfs:label \"MExportRts 3741:659\" ; \
                             \n\t\t\tnetwork_discovery:mExportRtsEntityPosition \"Line 25\" ; \
                             \n\t\t\tnetwork_discovery:mExportRtsListItem \"3741:659\" ]; \
                          \n\tnetwork_discovery:mVpnroutingDataHasMImportRts [ a network_discovery:MImportRts ; \
                             \n\t\t\trdfs:label \"MImportRts 3741:659\" ; \
                             \n\t\t\tnetwork_discovery:mImportRtsEntityPosition \"Line 26\" ; \
                             \n\t\t\tnetwork_discovery:mImportRtsListItem \"3741:659\" ] ; \
                      \n\tnetwork_discovery:mVpnroutingDataMLabelImpositionData \"true\" ; \
                      \n\tnetwork_discovery:extraInfoHasMMplsvpnmemberships \"[Prontodynamics]\"; \
                      \n\tnetwork_discovery:extraInfoMBaseName  \""
                + name
                + "\"; \
                      \n\tnetwork_discovery:extraInfoMAddressSpace \"true\"; \
                      \n\tnetwork_discovery:extraInfoMNoPing \"0\"; \
                      \n\t]; \
                  \nnetwork_discovery:entityActionType \"0\"; \
                  \nnetwork_discovery:entityIsActive \"1\"; \
                  \nnetwork_discovery:entityLingerTime \"3\"; \
                  \nnetwork_discovery:entityCreateTime  \""
                + timestamp
                + "\"; \
                  \nnetwork_discovery:entityChangeTime \""
                + timestamp
                + "\"; \
                  \nnetwork_discovery:entityClassName \"Cisco72xx\" . "
        )
