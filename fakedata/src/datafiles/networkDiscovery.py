class CreateTextContent:
    @staticmethod
    def networkdiscoveryentries():
        return (
            "\n @prefix : <http://ontology.com/queryResultViewExport#> . \
             \n@base <http://ontology.com/queryResultViewExport> .\
            \nnetwork_discovery:Entity \
                \na rdfs:Class, owl:Class; \
                \nrdfs:subClassOf owl:Thing. \
                \nnetwork_discovery:entityType \
                \na owl:DatatypeProperty; \
                \nrdfs:domain network_discovery:Entity. \
                \nnetwork_discovery:entityName \
                \na owl:DatatypeProperty; \
                \nrdfs:domain network_discovery:Entity. \
                \nnetwork_discovery:entityHasExtraInfo \
                \na owl:ObjectProperty; \
                \nrdfs:domain network_discovery:Entity. \
                \nnetwork_discovery:extraInfoMBaseName \
                \na owl:DatatypeProperty; \
                \nrdfs:domain network_discovery:ExtraInfo. \
                \nnetwork_discovery:extraInfoMIfAdminStatus \
                \na owl:DatatypeProperty; \
                \nrdfs:domain network_discovery:ExtraInfo. \
                \nnetwork_discovery:extraInfoMIfDescr \
                \na owl:DatatypeProperty; \
                \nrdfs:domain network_discovery:ExtraInfo. \
                \nnetwork_discovery:extraInfoMIfType \
                \na owl:DatatypeProperty; \
                \nrdfs:domain network_discovery:ExtraInfo. \
                \nnetwork_discovery:extraInfoMIpAddress \
                \na owl:DatatypeProperty; \
                \nrdfs:domain network_discovery:ExtraInfo. \
                \nnetwork_discovery:extraInfoMSysContact \
                \na owl:DatatypeProperty; \
                \nrdfs:domain network_discovery:ExtraInfo. \
                \nnetwork_discovery:extraInfoMSysDescr \
                \na owl:DatatypeProperty; \
                \nrdfs:domain network_discovery:ExtraInfo. \
                \nnetwork_discovery:extraInfoHasMIfIndex \
                \na owl:ObjectProperty; \
                \nrdfs:domain network_discovery:ExtraInfo; \
                \nrdfs:range network_discovery:MIfIndex. \
                \nnetwork_discovery:mIfIndexContent \
                \na owl:DatatypeProperty; \
                \nrdfs:domain network_discovery:MIfIndex. \
                \nnetwork_discovery:extraInfoHasMIfOperStatus \
                \na owl:ObjectProperty; \
                \nrdfs:domain network_discovery:ExtraInfo; \
                \nrdfs:range network_discovery:MIfOperStatus. \
                \nnetwork_discovery:mIfOperStatusContent \
                \na owl:DatatypeProperty; \
                \nrdfs:domain network_discovery:MIfOperStatus. \
                \nnetwork_discovery:mIfOperStatusEntityPosition \
                \na owl:DatatypeProperty; \
                \nrdfs:domain network_discovery:MIfOperStatus."
        )

    @staticmethod
    def networddiscoveryobj1(
            object_1_id,
            name,
            assoc_index_number_for_obj1,
            if_oper_status_for_obj1,
            if_index_for_obj1,
            entity_oid,
    ):
        return (
                "\n[] a network_discovery:Entity ; \
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
                    \nnetwork_discovery:entityType \"1\";\
                    \nnetwork_discovery:entityOid \""
                + entity_oid
                + "\" ; \
                    \nnetwork_discovery:entityHasExtraInfo [ a network_discovery:ExtraInfo ; \
                        \n\trdfs:label \"ExtraInfo\" ; \
                        \n\tnetwork_discovery:extraInfoMSysDescr \"DESCRIPTION\";\
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
                + "\"]; \
                            \n\tnetwork_discovery:extraInfoHasMIfOperStatus [ a network_discovery:MIfOperStatus ; \
                            \n\t\trdfs:label \"MIfOperStatus"
                + if_oper_status_for_obj1
                + "\"] ;\
                         \n];\
                    \nnetwork_discovery:extraInfoMBaseName \""
                + name
                + "\"  . \
        ")

    @staticmethod
    def networkdiscoveryobj2(
            name,
            object2_id,
            assoc_index_number,
            if_admin_status,
            if_oper_status,
            if_index,
            entity_oid,
            ip_address,
            subnet_mask,
            m_subnet,
            localnbrphysaddr,
    ):
        return (
                "\n[] a network_discovery:Entity ; \
                \nrdfs:label \"Entity "
                + object2_id
                + " ," + name
                + "[0["
                + object2_id
                + "]], 2\" ; \
                   \nnetwork_discovery:entityName \""
                + name
                + "[0["
                + assoc_index_number
                + "]]\"; \
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
                             \n\tnetwork_discovery:extraInfoHasMIfIndex [ a network_discovery:MIfIndex ; \
                             \n\trdfs:label \"MIfIndex"
                + if_index
                + " \"; \
                             \n\tnetwork_discovery:mIfIndexContent \""
                + if_index
                + "\" ] ; \
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
                             \n\tnetwork_discovery:extraInfoMIfDescr \"GigabitEthernet6/0.20\"] ; \
                \nnetwork_discovery:extraInfoMBaseName \""
                + name
                + "\"  . "
        )
