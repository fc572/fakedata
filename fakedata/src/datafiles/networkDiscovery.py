

class CreateTextContent:

    def networddiscoveryobj1(self, object_1_id, name, assoc_index_number_for_obj1, if_oper_status_for_obj1,
                             if_index_for_obj1, if_number, timestamp, entity_oid):

        return "\n{\
        \nObjectId = '" + object_1_id + "' \
        \nEntityName = 'ddl5-" + name + "-gt1'; \
        \nDescription = 'Cisco Internetwork Operating System Software IOS (tm) 7200 Software (C7200-P-M), \
        Version 12.3(1a), RELEASE SOFTWARE (fc1) Copyright(c)1986 - 2003 by cisco Systems, Inc.' \
        \nEntityType = 1;\
        \nEntityOID  = '" + entity_oid + "'; \
        \nExtraInfo = {\
            \n\tm_IpForwarding = 1;\
            \n\tm_SysName = 'ddl7-york-gt2';\
            \n\tm_SysDescr = 'DESCRIPTION' \
            \n\tm_SysContact = 'owner: north_east_ops | email: ne_ops@example.com | extension: 1145 | site: hull';\
            \n\tm_SysUpTime = 89971641;\
            \n\tm_SysServices = 6;\
            \n\tm_IfNumber = '" + if_number + "'; \
            \n\tm_AssocIndex  = " + assoc_index_number_for_obj1 + "; \
            \n\tm_IfIndex = " + if_index_for_obj1 + "; \
            \n\tm_IfOperStatus = " + if_oper_status_for_obj1 + "; \
            \n\tm_As = 3741;\
            \n\tm_BaseName = '" + name + "'; \
            \n\tm_AddressSpace = '';\
        \n};\
        \nActionType = 0;\
        \nIsActive = 1;\
        \nLingerTime = 3;\
        \nCreateTime = '" + timestamp + "'; \
        \nChangeTime  = '" + timestamp + "'; \
        \nClassName = 'Cisco72xx';\
        \n}"

    def networkdiscoveryobj2(self, name, object2_id, assoc_index_number, if_admin_status, if_oper_status, if_index,
                             entity_oid, ip_address, timestamp, subnet_mask, m_subnet, localnbrphysaddr):

        return "\n{ \
          \nObjectId = '" + object2_id + "'; \
          \nEntityName = '" + name + "[0 [" + assoc_index_number + "] ]'; \
          \nEntityType = 2; \
          \nEntityOID = '" + entity_oid + "'; \
          \nExtraInfo = { \
                  \n\tm_IfIndex = '" + if_index + "'; \
                  \n\tm_IfType = 135; \
                  \n\tm_IpAddress = '" + ip_address + "'; \
                  \n\tm_SubnetMask = '" + subnet_mask + "'; \
                  \n\tm_Subnet = '" + m_subnet + "'; \
                  \n\tm_LocalNbrPhysAddr = '" + localnbrphysaddr + "'; \
                  \n\tm_IfAdminStatus = " + if_admin_status + "; \
                  \n\tm_IfOperStatus = " + if_oper_status + "; \
                  \n\tm_IfDescr = 'GigabitEthernet6/0.20'; \
                  \n\tm_IfName = 'Gi6/0.20'; \
                  \n\tm_IfSpeed = 2560000; \
                  \n\tm_IfMTU = 1500; \
                  \n\tm_IfHighSpeed = 3; \
                  \n\tm_IfPromiscuousMode = 2; \
                  \n\tm_IfConnectorPresent = 2; \
                  \n\tm_BgpPeers=['0.0.0.0'];\
                  \n\tm_MultiNetList = ['0.0.0.0', '0.0.0.0'];\
                  \n\tm_MultiNetSubnet = ['0.0.0.0', '0.0.0.0'];\
                  \n\tm_MultiNetMask = ['0.0.0.0', '0.0.0.0'];\
                  \n\tm_LocalNbrStatus = 1;\
                  \n\tm_VPNRoutingData = { \
                      \n\t\tm_VrfName = 'Prontodynamics'; \
                      \n\t\tm_RD = '3741:659'; \
                      \n\t\tm_ExportRTs = ['3741:659']; \
                      \n\t\tm_ImportRTs = ['3741:659']; \
                      \n\t\tm_LabelImpositionData = ''; \
                      \n\t\t}; \
                  \n\tm_MPLSVPNMemberships = ['Prontodynamics']; \
                  \n\tm_DeviceId = '" + name + "'; \
                  \n\tm_BaseName = '" + name + "'; \
                  \n\tm_AddressSpace = ''; \
                  \n\tm_NoPing = 0; \
                  \n\t}; \
              \nActionType = 0; \
              \nIsActive = 1; \
              \nLingerTime = 3; \
              \nCreateTime = '" + timestamp + "'; \
              \nChangeTime = '" + timestamp + "'; \
              \nClassName = 'Cisco72xx'; \
              \n}"