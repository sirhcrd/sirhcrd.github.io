---
type: auto-detected-joins
generated_date: 2026-02-12
relationship_count: 609
---

# Auto-Detected Foreign Key Relationships

These relationships were automatically detected by analyzing sample column values
and matching Salesforce ID prefixes to their source tables.

## Relationships

### imax2_service_order__c

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `esmx_collaborator__c` | → | `imax_user`.id | prefix `005` |
| `esmx_collaborator__c` | → | `ipsa_user`.id | prefix `005` |
| `esmx_csr_activity_rq__c` | → | `imax_activity`.id | prefix `a1x` |
| `esmx_follow_up_contact__c` | → | `imax_contact`.id | prefix `003` |
| `esmx_follow_up_contact__c` | → | `ipsa_contact`.id | prefix `003` |
| `esmx_ip_location_account__c` | → | `imax_account`.id | prefix `001` |
| `esmx_ip_location_account__c` | → | `ipsa_account`.id | prefix `001` |
| `esmx_logged_in_user__c` | → | `imax_user`.id | prefix `005` |
| `esmx_logged_in_user__c` | → | `ipsa_user`.id | prefix `005` |
| `esmx_q_r_contact__c` | → | `imax_contact`.id | prefix `003` |
| `esmx_q_r_contact__c` | → | `ipsa_contact`.id | prefix `003` |
| `esmx_reference_installed_product__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `esmx_reference_ip_product__c` | → | `imax_product2`.id | prefix `01t` |
| `esmx_reference_ip_product__c` | → | `v_products__aa`.id | prefix `01t` |
| `esmx_service_manager__c` | → | `imax_user`.id | prefix `005` |
| `esmx_service_manager__c` | → | `ipsa_user`.id | prefix `005` |
| `esmx_technician_id__c` | → | `imax_user`.id | prefix `005` |
| `esmx_technician_id__c` | → | `ipsa_user`.id | prefix `005` |
| `esmx_work_activity__c` | → | `imax_activity`.id | prefix `a1x` |
| `svmxc__case__c` | → | `imax_case`.id | prefix `500` |
| `svmxc__closed_by__c` | → | `imax_user`.id | prefix `005` |
| `svmxc__closed_by__c` | → | `ipsa_user`.id | prefix `005` |
| `svmxc__company__c` | → | `imax_account`.id | prefix `001` |
| `svmxc__company__c` | → | `ipsa_account`.id | prefix `001` |
| `svmxc__component__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `svmxc__contact__c` | → | `imax_contact`.id | prefix `003` |
| `svmxc__contact__c` | → | `ipsa_contact`.id | prefix `003` |
| `svmxc__group_member__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `svmxc__group_member__c` | → | `ipsa_project_task`.id | prefix `a3V` |
| `svmxc__partner_account__c` | → | `imax_account`.id | prefix `001` |
| `svmxc__partner_account__c` | → | `ipsa_account`.id | prefix `001` |
| `svmxc__partner_contact__c` | → | `imax_contact`.id | prefix `003` |
| `svmxc__partner_contact__c` | → | `ipsa_contact`.id | prefix `003` |
| `svmxc__pm_sc__c` | → | `imax_service_contract`.id | prefix `a3T` |
| `svmxc__preferred_technician__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `svmxc__preferred_technician__c` | → | `ipsa_project_task`.id | prefix `a3V` |
| `svmxc__product__c` | → | `imax_product2`.id | prefix `01t` |
| `svmxc__product__c` | → | `v_products__aa`.id | prefix `01t` |
| `svmxc__related_work_order__c` | → | `imax_service_order_c`.id | prefix `a3d` |
| `svmxc__service_contract__c` | → | `imax_service_contract`.id | prefix `a3T` |
| `svmxc__top_level__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `technician_formula__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `technician_formula__c` | → | `ipsa_project_task`.id | prefix `a3V` |

### imax_account

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `Customer_Portal_Parent_Account__c` | → | `imax_account`.id | prefix `001` |
| `Customer_Portal_Parent_Account__c` | → | `ipsa_account`.id | prefix `001` |

### imax_activity

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `ESMX_Account__c` | → | `imax_account`.id | prefix `001` |
| `ESMX_Account__c` | → | `ipsa_account`.id | prefix `001` |
| `ESMX_Case_Follow_Up__c` | → | `imax_case`.id | prefix `500` |
| `ESMX_Case__c` | → | `imax_case`.id | prefix `500` |
| `ESMX_Contact__c` | → | `imax_contact`.id | prefix `003` |
| `ESMX_Contact__c` | → | `ipsa_contact`.id | prefix `003` |
| `ESMX_Follow_Up_Contact__c` | → | `imax_contact`.id | prefix `003` |
| `ESMX_Follow_Up_Contact__c` | → | `ipsa_contact`.id | prefix `003` |
| `ESMX_Installed_Product__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `ESMX_Product__c` | → | `imax_product2`.id | prefix `01t` |
| `ESMX_Product__c` | → | `v_products__aa`.id | prefix `01t` |
| `ESMX_Recommended_Service_Engineer__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `ESMX_Recommended_Service_Engineer__c` | → | `ipsa_project_task`.id | prefix `a3V` |
| `ESMX_Service_Maintenance_Contract__c` | → | `imax_service_contract`.id | prefix `a3T` |
| `ESMX_Work_Activity__c` | → | `imax_service_order_c`.id | prefix `a3d` |

### imax_case

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `AR_Approver__c` | → | `imax_user`.id | prefix `005` |
| `AR_Approver__c` | → | `ipsa_user`.id | prefix `005` |
| `BC_Queues_Id__c` | → | `ipsa_group`.id | prefix `00G` |
| `EMS_Implementor__c` | → | `imax_contact`.id | prefix `003` |
| `EMS_Implementor__c` | → | `ipsa_contact`.id | prefix `003` |
| `EMS_Product__c` | → | `imax_product2`.id | prefix `01t` |
| `EMS_Product__c` | → | `v_products__aa`.id | prefix `01t` |
| `ESMX_Activity__c` | → | `imax_activity`.id | prefix `a1x` |
| `ESMX_Case_Record_ID__c` | → | `imax_case`.id | prefix `500` |
| `ESMX_Escalated_Installed_Product__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `ESMX_Management_Escalation_Closed_By__c` | → | `imax_user`.id | prefix `005` |
| `ESMX_Management_Escalation_Closed_By__c` | → | `ipsa_user`.id | prefix `005` |
| `ESMX_Reference_IP_Product__c` | → | `imax_product2`.id | prefix `01t` |
| `ESMX_Reference_IP_Product__c` | → | `v_products__aa`.id | prefix `01t` |
| `ESMX_Reference_Installed_Product__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `L1_Owner__c` | → | `imax_user`.id | prefix `005` |
| `L1_Owner__c` | → | `ipsa_user`.id | prefix `005` |
| `L2_Owner__c` | → | `imax_user`.id | prefix `005` |
| `L2_Owner__c` | → | `ipsa_user`.id | prefix `005` |
| `L3_Owner__c` | → | `imax_user`.id | prefix `005` |
| `L3_Owner__c` | → | `ipsa_user`.id | prefix `005` |
| `PAO__c` | → | `imax_user`.id | prefix `005` |
| `PAO__c` | → | `ipsa_user`.id | prefix `005` |
| `PO_Payor_Account__c` | → | `imax_account`.id | prefix `001` |
| `PO_Payor_Account__c` | → | `ipsa_account`.id | prefix `001` |
| `Primary_Case__c` | → | `imax_case`.id | prefix `500` |
| `Primary_Customer_Communicator__c` | → | `imax_user`.id | prefix `005` |
| `Primary_Customer_Communicator__c` | → | `ipsa_user`.id | prefix `005` |
| `Recent_Action_Plan_Creator__c` | → | `imax_user`.id | prefix `005` |
| `Recent_Action_Plan_Creator__c` | → | `ipsa_user`.id | prefix `005` |
| `Reference_Product__c` | → | `imax_product2`.id | prefix `01t` |
| `Reference_Product__c` | → | `v_products__aa`.id | prefix `01t` |
| `SVMXC__BW_Selected_By__c` | → | `imax_user`.id | prefix `005` |
| `SVMXC__BW_Selected_By__c` | → | `ipsa_user`.id | prefix `005` |
| `SVMXC__Component__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `SVMXC__Product__c` | → | `imax_product2`.id | prefix `01t` |
| `SVMXC__Product__c` | → | `v_products__aa`.id | prefix `01t` |
| `SVMXC__Service_Contract__c` | → | `imax_service_contract`.id | prefix `a3T` |
| `SVMXC__Top_Level__c` | → | `imax_installed_product_c`.id | prefix `a2W` |

### imax_case_line

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `ESMX_Account__c` | → | `imax_account`.id | prefix `001` |
| `ESMX_Account__c` | → | `ipsa_account`.id | prefix `001` |
| `ESMX_Action_Owner__c` | → | `imax_user`.id | prefix `005` |
| `ESMX_Action_Owner__c` | → | `ipsa_user`.id | prefix `005` |
| `ESMX_Investigated_Installed_Product__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `ESMX_PM_History__c` | → | `ipsa_assignment__c`.id | prefix `a2g` |
| `ESMX_Related_Case_Line__c` | → | `imax_case_line`.id | prefix `a2J` |
| `ESMX_Related_Case_Line__c` | → | `vsmax_nar_cl_install`.id | prefix `a2J` |
| `ESMX_Work_Detail__c` | → | `imax_service_order_line`.id | prefix `a3c` |
| `SVMXC__Case__c` | → | `imax_case`.id | prefix `500` |
| `SVMXC__Installed_Product__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `SVMXC__Product__c` | → | `imax_product2`.id | prefix `01t` |
| `SVMXC__Product__c` | → | `v_products__aa`.id | prefix `01t` |

### imax_contact

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `ESMX_Backup_Contact__c` | → | `imax_contact`.id | prefix `003` |
| `ESMX_Backup_Contact__c` | → | `ipsa_contact`.id | prefix `003` |
| `ESMX_Trade_Partner_Account__c` | → | `imax_account`.id | prefix `001` |
| `ESMX_Trade_Partner_Account__c` | → | `ipsa_account`.id | prefix `001` |

### imax_contract_header

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `ESMX_Account__c` | → | `imax_account`.id | prefix `001` |
| `ESMX_Account__c` | → | `ipsa_account`.id | prefix `001` |
| `ESMX_Bill_To__c` | → | `imax_account`.id | prefix `001` |
| `ESMX_Bill_To__c` | → | `ipsa_account`.id | prefix `001` |
| `ESMX_Payer__c` | → | `imax_account`.id | prefix `001` |
| `ESMX_Payer__c` | → | `ipsa_account`.id | prefix `001` |
| `ESMX_Ship_To_Account__c` | → | `imax_account`.id | prefix `001` |
| `ESMX_Ship_To_Account__c` | → | `ipsa_account`.id | prefix `001` |
| `NewHeader__c` | → | `imax_contract_header`.id | prefix `a4D` |

### imax_installed_product_c

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `ESMX_Auto_Created_From__c` | → | `imax_service_order_line`.id | prefix `a3c` |
| `ESMX_Bill_To__c` | → | `imax_account`.id | prefix `001` |
| `ESMX_Bill_To__c` | → | `ipsa_account`.id | prefix `001` |
| `ESMX_End_User_Account__c` | → | `imax_account`.id | prefix `001` |
| `ESMX_End_User_Account__c` | → | `ipsa_account`.id | prefix `001` |
| `ESMX_Hardware_Installed_Product_Lookup__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `ESMX_Location_Account_Name__c` | → | `imax_account`.id | prefix `001` |
| `ESMX_Location_Account_Name__c` | → | `ipsa_account`.id | prefix `001` |
| `ESMX_PM_Contact__c` | → | `imax_contact`.id | prefix `003` |
| `ESMX_PM_Contact__c` | → | `ipsa_contact`.id | prefix `003` |
| `ESMX_Payor__c` | → | `imax_account`.id | prefix `001` |
| `ESMX_Payor__c` | → | `ipsa_account`.id | prefix `001` |
| `ESMX_Primary_Technician_ID__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `ESMX_Primary_Technician_ID__c` | → | `ipsa_project_task`.id | prefix `a3V` |
| `ESMX_Secondary_FSE_Technician__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `ESMX_Secondary_FSE_Technician__c` | → | `ipsa_project_task`.id | prefix `a3V` |
| `ESMX_Secondary_Technician_ID__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `ESMX_Secondary_Technician_ID__c` | → | `ipsa_project_task`.id | prefix `a3V` |
| `ESMX_Service_Provider_Account__c` | → | `imax_account`.id | prefix `001` |
| `ESMX_Service_Provider_Account__c` | → | `ipsa_account`.id | prefix `001` |
| `ESMX_Tertiary_FSE_Technician__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `ESMX_Tertiary_FSE_Technician__c` | → | `ipsa_project_task`.id | prefix `a3V` |
| `ESMX_Tertiary_Technician_ID__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `ESMX_Tertiary_Technician_ID__c` | → | `ipsa_project_task`.id | prefix `a3V` |
| `SVMXC__Company__c` | → | `imax_account`.id | prefix `001` |
| `SVMXC__Company__c` | → | `ipsa_account`.id | prefix `001` |
| `SVMXC__Parent__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `SVMXC__Preferred_Technician__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `SVMXC__Preferred_Technician__c` | → | `ipsa_project_task`.id | prefix `a3V` |
| `SVMXC__Product__c` | → | `imax_product2`.id | prefix `01t` |
| `SVMXC__Product__c` | → | `v_products__aa`.id | prefix `01t` |
| `SVMXC__Top_Level__c` | → | `imax_installed_product_c`.id | prefix `a2W` |

### imax_installed_product_c_all

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `ESMX_Auto_Created_From__c` | → | `imax_service_order_line`.id | prefix `a3c` |
| `ESMX_Bill_To__c` | → | `imax_account`.id | prefix `001` |
| `ESMX_Bill_To__c` | → | `ipsa_account`.id | prefix `001` |
| `ESMX_End_User_Account__c` | → | `imax_account`.id | prefix `001` |
| `ESMX_End_User_Account__c` | → | `ipsa_account`.id | prefix `001` |
| `ESMX_Hardware_Installed_Product_Lookup__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `ESMX_Location_Account_Name__c` | → | `imax_account`.id | prefix `001` |
| `ESMX_Location_Account_Name__c` | → | `ipsa_account`.id | prefix `001` |
| `ESMX_PM_Contact__c` | → | `imax_contact`.id | prefix `003` |
| `ESMX_PM_Contact__c` | → | `ipsa_contact`.id | prefix `003` |
| `ESMX_Payor__c` | → | `imax_account`.id | prefix `001` |
| `ESMX_Payor__c` | → | `ipsa_account`.id | prefix `001` |
| `ESMX_Primary_Technician_ID__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `ESMX_Primary_Technician_ID__c` | → | `ipsa_project_task`.id | prefix `a3V` |
| `ESMX_Secondary_FSE_Technician__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `ESMX_Secondary_FSE_Technician__c` | → | `ipsa_project_task`.id | prefix `a3V` |
| `ESMX_Secondary_Technician_ID__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `ESMX_Secondary_Technician_ID__c` | → | `ipsa_project_task`.id | prefix `a3V` |
| `ESMX_Service_Provider_Account__c` | → | `imax_account`.id | prefix `001` |
| `ESMX_Service_Provider_Account__c` | → | `ipsa_account`.id | prefix `001` |
| `ESMX_Tertiary_FSE_Technician__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `ESMX_Tertiary_FSE_Technician__c` | → | `ipsa_project_task`.id | prefix `a3V` |
| `ESMX_Tertiary_Technician_ID__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `ESMX_Tertiary_Technician_ID__c` | → | `ipsa_project_task`.id | prefix `a3V` |
| `SVMXC__Company__c` | → | `imax_account`.id | prefix `001` |
| `SVMXC__Company__c` | → | `ipsa_account`.id | prefix `001` |
| `SVMXC__Parent__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `SVMXC__Preferred_Technician__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `SVMXC__Preferred_Technician__c` | → | `ipsa_project_task`.id | prefix `a3V` |
| `SVMXC__Product__c` | → | `imax_product2`.id | prefix `01t` |
| `SVMXC__Product__c` | → | `v_products__aa`.id | prefix `01t` |
| `SVMXC__Top_Level__c` | → | `imax_installed_product_c`.id | prefix `a2W` |

### imax_product2

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `SLCP_Upgrade_Base_Product__c` | → | `imax_product2`.id | prefix `01t` |
| `SLCP_Upgrade_Base_Product__c` | → | `v_products__aa`.id | prefix `01t` |

### imax_service_contract

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `ESMX_Bill_To__c` | → | `imax_account`.id | prefix `001` |
| `ESMX_Bill_To__c` | → | `ipsa_account`.id | prefix `001` |
| `ESMX_Contract_Header__c` | → | `imax_contract_header`.id | prefix `a4D` |
| `ESMX_Payer__c` | → | `imax_account`.id | prefix `001` |
| `ESMX_Payer__c` | → | `ipsa_account`.id | prefix `001` |
| `SVMXC__Canceled_By__c` | → | `imax_user`.id | prefix `005` |
| `SVMXC__Canceled_By__c` | → | `ipsa_user`.id | prefix `005` |
| `SVMXC__Company__c` | → | `imax_account`.id | prefix `001` |
| `SVMXC__Company__c` | → | `ipsa_account`.id | prefix `001` |
| `SVMXC__Contact__c` | → | `imax_contact`.id | prefix `003` |
| `SVMXC__Contact__c` | → | `ipsa_contact`.id | prefix `003` |
| `SVMXC__Renewed_From__c` | → | `imax_service_contract`.id | prefix `a3T` |
| `SVMXC__Sales_Rep__c` | → | `imax_user`.id | prefix `005` |
| `SVMXC__Sales_Rep__c` | → | `ipsa_user`.id | prefix `005` |

### imax_service_group_members

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `ESMX_Product__c` | → | `imax_product2`.id | prefix `01t` |
| `ESMX_Product__c` | → | `v_products__aa`.id | prefix `01t` |
| `ESMX_Service_Manager__c` | → | `imax_user`.id | prefix `005` |
| `ESMX_Service_Manager__c` | → | `ipsa_user`.id | prefix `005` |
| `ESMX_Tool_Owner__c` | → | `imax_user`.id | prefix `005` |
| `ESMX_Tool_Owner__c` | → | `ipsa_user`.id | prefix `005` |
| `ESMX_User_ID__c` | → | `imax_user`.id | prefix `005` |
| `ESMX_User_ID__c` | → | `ipsa_user`.id | prefix `005` |
| `SVMXC__Salesforce_User__c` | → | `imax_user`.id | prefix `005` |
| `SVMXC__Salesforce_User__c` | → | `ipsa_user`.id | prefix `005` |

### imax_service_group_skills

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `ESMX_Salesforce_User__c` | → | `imax_user`.id | prefix `005` |
| `ESMX_Salesforce_User__c` | → | `ipsa_user`.id | prefix `005` |
| `SVMXC__Group_Member__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `SVMXC__Group_Member__c` | → | `ipsa_project_task`.id | prefix `a3V` |

### imax_service_order_c

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `ESMX_CSR_Activity_RQ__c` | → | `imax_activity`.id | prefix `a1x` |
| `ESMX_Collaborator__c` | → | `imax_user`.id | prefix `005` |
| `ESMX_Collaborator__c` | → | `ipsa_user`.id | prefix `005` |
| `ESMX_Follow_Up_Contact__c` | → | `imax_contact`.id | prefix `003` |
| `ESMX_Follow_Up_Contact__c` | → | `ipsa_contact`.id | prefix `003` |
| `ESMX_Logged_in_User__c` | → | `imax_user`.id | prefix `005` |
| `ESMX_Logged_in_User__c` | → | `ipsa_user`.id | prefix `005` |
| `ESMX_Q_R_Contact__c` | → | `imax_contact`.id | prefix `003` |
| `ESMX_Q_R_Contact__c` | → | `ipsa_contact`.id | prefix `003` |
| `ESMX_Recommended_Service_Engineer__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `ESMX_Recommended_Service_Engineer__c` | → | `ipsa_project_task`.id | prefix `a3V` |
| `ESMX_Reference_IP_Product__c` | → | `imax_product2`.id | prefix `01t` |
| `ESMX_Reference_IP_Product__c` | → | `v_products__aa`.id | prefix `01t` |
| `ESMX_Reference_Installed_Product__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `ESMX_SWO_Location_Id__c` | → | `imax_service_contract`.id | prefix `a3T` |
| `ESMX_Service_Manager__c` | → | `imax_user`.id | prefix `005` |
| `ESMX_Service_Manager__c` | → | `ipsa_user`.id | prefix `005` |
| `ESMX_Technician_Id__c` | → | `imax_user`.id | prefix `005` |
| `ESMX_Technician_Id__c` | → | `ipsa_user`.id | prefix `005` |
| `ESMX_Work_Activity__c` | → | `imax_activity`.id | prefix `a1x` |
| `SVMXC__Case__c` | → | `imax_case`.id | prefix `500` |
| `SVMXC__Closed_By__c` | → | `imax_user`.id | prefix `005` |
| `SVMXC__Closed_By__c` | → | `ipsa_user`.id | prefix `005` |
| `SVMXC__Company__c` | → | `imax_account`.id | prefix `001` |
| `SVMXC__Company__c` | → | `ipsa_account`.id | prefix `001` |
| `SVMXC__Component__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `SVMXC__Contact__c` | → | `imax_contact`.id | prefix `003` |
| `SVMXC__Contact__c` | → | `ipsa_contact`.id | prefix `003` |
| `SVMXC__Group_Member__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `SVMXC__Group_Member__c` | → | `ipsa_project_task`.id | prefix `a3V` |
| `SVMXC__PM_SC__c` | → | `imax_service_contract`.id | prefix `a3T` |
| `SVMXC__Partner_Account__c` | → | `imax_account`.id | prefix `001` |
| `SVMXC__Partner_Account__c` | → | `ipsa_account`.id | prefix `001` |
| `SVMXC__Partner_Contact__c` | → | `imax_contact`.id | prefix `003` |
| `SVMXC__Partner_Contact__c` | → | `ipsa_contact`.id | prefix `003` |
| `SVMXC__Preferred_Technician__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `SVMXC__Preferred_Technician__c` | → | `ipsa_project_task`.id | prefix `a3V` |
| `SVMXC__Product__c` | → | `imax_product2`.id | prefix `01t` |
| `SVMXC__Product__c` | → | `v_products__aa`.id | prefix `01t` |
| `SVMXC__Related_Work_Order__c` | → | `imax_service_order_c`.id | prefix `a3d` |
| `SVMXC__Service_Contract__c` | → | `imax_service_contract`.id | prefix `a3T` |
| `SVMXC__Top_Level__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `Technician_Formula__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `Technician_Formula__c` | → | `ipsa_project_task`.id | prefix `a3V` |

### imax_service_order_line

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `ESMX_Account__c` | → | `imax_account`.id | prefix `001` |
| `ESMX_Account__c` | → | `ipsa_account`.id | prefix `001` |
| `ESMX_Case_Line__c` | → | `imax_case_line`.id | prefix `a2J` |
| `ESMX_Case_Line__c` | → | `vsmax_nar_cl_install`.id | prefix `a2J` |
| `ESMX_Case__c` | → | `imax_case`.id | prefix `500` |
| `ESMX_Consumed_From_Part__c` | → | `imax_service_order_line`.id | prefix `a3c` |
| `ESMX_Defective_Installed_Product__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `ESMX_Defective_Part__c` | → | `imax_product2`.id | prefix `01t` |
| `ESMX_Defective_Part__c` | → | `v_products__aa`.id | prefix `01t` |
| `ESMX_IB_External_Key__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `ESMX_Installed_Product_WD__c` | → | `imax_service_order_line`.id | prefix `a3c` |
| `ESMX_Installed_Product__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `ESMX_Parent_FCO_Kit__c` | → | `imax_service_order_line`.id | prefix `a3c` |
| `ESMX_Parent_IP_Sub_block__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `ESMX_Parent_IP__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `ESMX_Related_Work_Order__c` | → | `imax_service_order_c`.id | prefix `a3d` |
| `PF_Technician_User_ID__c` | → | `imax_user`.id | prefix `005` |
| `PF_Technician_User_ID__c` | → | `ipsa_user`.id | prefix `005` |
| `PF_Work_Detail_Id__c` | → | `imax_service_order_line`.id | prefix `a3c` |
| `SVMXC__Canceled_By__c` | → | `imax_user`.id | prefix `005` |
| `SVMXC__Canceled_By__c` | → | `ipsa_user`.id | prefix `005` |
| `SVMXC__Closed_By__c` | → | `imax_user`.id | prefix `005` |
| `SVMXC__Closed_By__c` | → | `ipsa_user`.id | prefix `005` |
| `SVMXC__Group_Member__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `SVMXC__Group_Member__c` | → | `ipsa_project_task`.id | prefix `a3V` |
| `SVMXC__Product__c` | → | `imax_product2`.id | prefix `01t` |
| `SVMXC__Product__c` | → | `v_products__aa`.id | prefix `01t` |
| `SVMXC__Serial_Number__c` | → | `imax_installed_product_c`.id | prefix `a2W` |
| `SVMXC__Service_Maintenance_Contract__c` | → | `imax_service_contract`.id | prefix `a3T` |
| `SVMXC__Service_Order__c` | → | `imax_service_order_c`.id | prefix `a3d` |
| `SVMXC__Work_Detail__c` | → | `imax_service_order_line`.id | prefix `a3c` |
| `SVMX_Return_Part__c` | → | `imax_product2`.id | prefix `01t` |
| `SVMX_Return_Part__c` | → | `v_products__aa`.id | prefix `01t` |

### imax_user

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `ESMX_Technician__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `ESMX_Technician__c` | → | `ipsa_project_task`.id | prefix `a3V` |

### ipsa_account

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `Account_Internal_ID__c` | → | `imax_account`.id | prefix `001` |
| `Account_Internal_ID__c` | → | `ipsa_account`.id | prefix `001` |
| `Associated_IDN__c` | → | `imax_account`.id | prefix `001` |
| `Associated_IDN__c` | → | `ipsa_account`.id | prefix `001` |
| `Destination_Account_Name__c` | → | `imax_account`.id | prefix `001` |
| `Destination_Account_Name__c` | → | `ipsa_account`.id | prefix `001` |
| `EHR_Vendor__c` | → | `imax_account`.id | prefix `001` |
| `EHR_Vendor__c` | → | `ipsa_account`.id | prefix `001` |
| `IHN__c` | → | `imax_account`.id | prefix `001` |
| `IHN__c` | → | `ipsa_account`.id | prefix `001` |
| `Level_01_Parent_Id__c` | → | `imax_account`.id | prefix `001` |
| `Level_01_Parent_Id__c` | → | `ipsa_account`.id | prefix `001` |
| `Level_02_Parent_Id__c` | → | `imax_account`.id | prefix `001` |
| `Level_02_Parent_Id__c` | → | `ipsa_account`.id | prefix `001` |
| `Level_03_Parent_Id__c` | → | `imax_account`.id | prefix `001` |
| `Level_03_Parent_Id__c` | → | `ipsa_account`.id | prefix `001` |
| `Level_04_Parent_Id__c` | → | `imax_account`.id | prefix `001` |
| `Level_04_Parent_Id__c` | → | `ipsa_account`.id | prefix `001` |
| `Level_05_Parent_Id__c` | → | `imax_account`.id | prefix `001` |
| `Level_05_Parent_Id__c` | → | `ipsa_account`.id | prefix `001` |
| `Level_06_Parent_Id__c` | → | `imax_account`.id | prefix `001` |
| `Level_06_Parent_Id__c` | → | `ipsa_account`.id | prefix `001` |
| `Level_1_Parent__c` | → | `imax_account`.id | prefix `001` |
| `Level_1_Parent__c` | → | `ipsa_account`.id | prefix `001` |
| `Level_5_Parent__c` | → | `imax_account`.id | prefix `001` |
| `Level_5_Parent__c` | → | `ipsa_account`.id | prefix `001` |
| `Level_6_Parent__c` | → | `imax_account`.id | prefix `001` |
| `Level_6_Parent__c` | → | `ipsa_account`.id | prefix `001` |
| `Parent_IDN_of_Associated_IDN__c` | → | `imax_account`.id | prefix `001` |
| `Parent_IDN_of_Associated_IDN__c` | → | `ipsa_account`.id | prefix `001` |
| `Region__c` | → | `ipsa_region`.id | prefix `a0o` |
| `Region_global__c` | → | `ipsa_region`.id | prefix `a0o` |
| `RelatedApexAccount__c` | → | `imax_account`.id | prefix `001` |
| `RelatedApexAccount__c` | → | `ipsa_account`.id | prefix `001` |
| `RelatedCoreAccount__c` | → | `imax_account`.id | prefix `001` |
| `RelatedCoreAccount__c` | → | `ipsa_account`.id | prefix `001` |
| `Strategic_Account_Manager__c` | → | `imax_user`.id | prefix `005` |
| `Strategic_Account_Manager__c` | → | `ipsa_user`.id | prefix `005` |

### ipsa_assignment__c

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `PSA_Delivery_Contact__c` | → | `ipsa_project_contacts__c`.id | prefix `a9C` |
| `pse__Milestone__c` | → | `ipsa_pse_milestone_c`.id | prefix `a3C` |
| `pse__Project__c` | → | `ipsa_proj_c`.id | prefix `a3L` |
| `pse__Project__c` | → | `nar_hpm_psa_projects`.id | prefix `a3L` |
| `pse__Project__c` | → | `vproject_milestone_dates`.id | prefix `a3L` |
| `pse__Resource_Request__c` | → | `ipsa_resource_request_c`.id | prefix `a3f` |
| `pse__Resource__c` | → | `imax_contact`.id | prefix `003` |
| `pse__Resource__c` | → | `ipsa_contact`.id | prefix `003` |

### ipsa_contact

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `CPM_Manager_User__c` | → | `imax_user`.id | prefix `005` |
| `CPM_Manager_User__c` | → | `ipsa_user`.id | prefix `005` |
| `Director__c` | → | `imax_contact`.id | prefix `003` |
| `Director__c` | → | `ipsa_contact`.id | prefix `003` |
| `Manager__c` | → | `imax_contact`.id | prefix `003` |
| `Manager__c` | → | `ipsa_contact`.id | prefix `003` |
| `Order_Manager__c` | → | `imax_contact`.id | prefix `003` |
| `Order_Manager__c` | → | `ipsa_contact`.id | prefix `003` |
| `PSA_Business_Group__c` | → | `ipsa_practice_c`.id | prefix `a3K` |
| `PSA_Country__c` | → | `imax_service_group_skills`.id | prefix `a3Y` |
| `PSA_Country__c` | → | `ipsa_pse_region_c`.id | prefix `a3Y` |
| `PSA_Territory__c` | → | `imax_service_group_skills`.id | prefix `a3Y` |
| `PSA_Territory__c` | → | `ipsa_pse_region_c`.id | prefix `a3Y` |
| `Region__c` | → | `ipsa_region`.id | prefix `a0o` |
| `pse__Practice__c` | → | `ipsa_practice_c`.id | prefix `a3K` |
| `pse__Region__c` | → | `imax_service_group_skills`.id | prefix `a3Y` |
| `pse__Region__c` | → | `ipsa_pse_region_c`.id | prefix `a3Y` |
| `pse__Salesforce_User__c` | → | `imax_user`.id | prefix `005` |
| `pse__Salesforce_User__c` | → | `ipsa_user`.id | prefix `005` |
| `pse__Work_Calendar__c` | → | `ipsa_work_calendar_c`.id | prefix `a48` |

### ipsa_missing_timecard__c

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `pse__Resource__c` | → | `imax_contact`.id | prefix `003` |
| `pse__Resource__c` | → | `ipsa_contact`.id | prefix `003` |

### ipsa_opportunity

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `Affiliated_IDN__c` | → | `imax_account`.id | prefix `001` |
| `Affiliated_IDN__c` | → | `ipsa_account`.id | prefix `001` |
| `Apex_Account_Id__c` | → | `imax_account`.id | prefix `001` |
| `Apex_Account_Id__c` | → | `ipsa_account`.id | prefix `001` |
| `CaseSafeOpptyID__c` | → | `ipsa_opportunity`.id | prefix `006` |
| `CaseSafeOpptyID__c` | → | `xplenty_staging_365363`.id | prefix `006` |
| `Chief_Technologist__c` | → | `imax_contact`.id | prefix `003` |
| `Chief_Technologist__c` | → | `ipsa_contact`.id | prefix `003` |
| `Competitor_Name__c` | → | `imax_account`.id | prefix `001` |
| `Competitor_Name__c` | → | `ipsa_account`.id | prefix `001` |
| `Key_Contact__c` | → | `imax_contact`.id | prefix `003` |
| `Key_Contact__c` | → | `ipsa_contact`.id | prefix `003` |
| `Opportunity_Hierarchy_Link__c` | → | `ipsa_opportunity`.id | prefix `006` |
| `Opportunity_Hierarchy_Link__c` | → | `xplenty_staging_365363`.id | prefix `006` |
| `PM__c` | → | `imax_contact`.id | prefix `003` |
| `PM__c` | → | `ipsa_contact`.id | prefix `003` |
| `Phone_Book_Account__c` | → | `imax_account`.id | prefix `001` |
| `Phone_Book_Account__c` | → | `ipsa_account`.id | prefix `001` |
| `Primary_Rep__c` | → | `imax_user`.id | prefix `005` |
| `Primary_Rep__c` | → | `ipsa_user`.id | prefix `005` |
| `RDD__c` | → | `imax_contact`.id | prefix `003` |
| `RDD__c` | → | `ipsa_contact`.id | prefix `003` |
| `Radiologist_Doctor__c` | → | `imax_contact`.id | prefix `003` |
| `Radiologist_Doctor__c` | → | `ipsa_contact`.id | prefix `003` |
| `Radiology_or_Dept_Admin__c` | → | `imax_contact`.id | prefix `003` |
| `Radiology_or_Dept_Admin__c` | → | `ipsa_contact`.id | prefix `003` |
| `Region__c` | → | `ipsa_region`.id | prefix `a0o` |
| `Regional_Svc_Mgr__c` | → | `imax_contact`.id | prefix `003` |
| `Regional_Svc_Mgr__c` | → | `ipsa_contact`.id | prefix `003` |
| `Secondary_Rep__c` | → | `imax_user`.id | prefix `005` |
| `Secondary_Rep__c` | → | `ipsa_user`.id | prefix `005` |
| `Spiff_Referred_By__c` | → | `imax_user`.id | prefix `005` |
| `Spiff_Referred_By__c` | → | `ipsa_user`.id | prefix `005` |
| `Working_Rep__c` | → | `imax_user`.id | prefix `005` |
| `Working_Rep__c` | → | `ipsa_user`.id | prefix `005` |

### ipsa_practice_c

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `pse__Actuals_Last_Updated_By__c` | → | `imax_user`.id | prefix `005` |
| `pse__Actuals_Last_Updated_By__c` | → | `ipsa_user`.id | prefix `005` |
| `pse__Backlog_Last_Updated_By__c` | → | `imax_user`.id | prefix `005` |
| `pse__Backlog_Last_Updated_By__c` | → | `ipsa_user`.id | prefix `005` |
| `pse__Global_Practice__c` | → | `ipsa_practice_c`.id | prefix `a3K` |
| `pse__Parent_Practice__c` | → | `ipsa_practice_c`.id | prefix `a3K` |
| `pse__Plan_Last_Updated_By__c` | → | `imax_user`.id | prefix `005` |
| `pse__Plan_Last_Updated_By__c` | → | `ipsa_user`.id | prefix `005` |
| `pse__Practice_Head__c` | → | `imax_contact`.id | prefix `003` |
| `pse__Practice_Head__c` | → | `ipsa_contact`.id | prefix `003` |
| `pse__Utilization_Last_Updated_By__c` | → | `imax_user`.id | prefix `005` |
| `pse__Utilization_Last_Updated_By__c` | → | `ipsa_user`.id | prefix `005` |

### ipsa_proj_c

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `Clinical_Co_Lead__c` | → | `imax_contact`.id | prefix `003` |
| `Clinical_Co_Lead__c` | → | `ipsa_contact`.id | prefix `003` |
| `Clinical_Lead__c` | → | `imax_contact`.id | prefix `003` |
| `Clinical_Lead__c` | → | `ipsa_contact`.id | prefix `003` |
| `District_Manager_SCS_Zone_Mgr__c` | → | `imax_contact`.id | prefix `003` |
| `District_Manager_SCS_Zone_Mgr__c` | → | `ipsa_contact`.id | prefix `003` |
| `ECR_Specialist__c` | → | `imax_contact`.id | prefix `003` |
| `ECR_Specialist__c` | → | `ipsa_contact`.id | prefix `003` |
| `Fetal_Specialist__c` | → | `imax_contact`.id | prefix `003` |
| `Fetal_Specialist__c` | → | `ipsa_contact`.id | prefix `003` |
| `Guardian_Specialist__c` | → | `imax_contact`.id | prefix `003` |
| `Guardian_Specialist__c` | → | `ipsa_contact`.id | prefix `003` |
| `IEM_CareEvent_Specialist__c` | → | `imax_contact`.id | prefix `003` |
| `IEM_CareEvent_Specialist__c` | → | `ipsa_contact`.id | prefix `003` |
| `Id__c` | → | `ipsa_proj_c`.id | prefix `a3L` |
| `Id__c` | → | `nar_hpm_psa_projects`.id | prefix `a3L` |
| `Id__c` | → | `vproject_milestone_dates`.id | prefix `a3L` |
| `Lead_Sales_Agent__c` | → | `imax_contact`.id | prefix `003` |
| `Lead_Sales_Agent__c` | → | `ipsa_contact`.id | prefix `003` |
| `PSA_Parent_Program__c` | → | `ipsa_proj_c`.id | prefix `a3L` |
| `PSA_Parent_Program__c` | → | `nar_hpm_psa_projects`.id | prefix `a3L` |
| `PSA_Parent_Program__c` | → | `vproject_milestone_dates`.id | prefix `a3L` |
| `PSA_Territory__c` | → | `imax_service_group_skills`.id | prefix `a3Y` |
| `PSA_Territory__c` | → | `ipsa_pse_region_c`.id | prefix `a3Y` |
| `PSA_proj_Country__c` | → | `imax_service_group_skills`.id | prefix `a3Y` |
| `PSA_proj_Country__c` | → | `ipsa_pse_region_c`.id | prefix `a3Y` |
| `Previous_PM__c` | → | `imax_contact`.id | prefix `003` |
| `Previous_PM__c` | → | `ipsa_contact`.id | prefix `003` |
| `SCS_Senior_Director_SCS_Sr_Dir_Mgr__c` | → | `imax_contact`.id | prefix `003` |
| `SCS_Senior_Director_SCS_Sr_Dir_Mgr__c` | → | `ipsa_contact`.id | prefix `003` |
| `pse__Account__c` | → | `imax_account`.id | prefix `001` |
| `pse__Account__c` | → | `ipsa_account`.id | prefix `001` |
| `pse__Actuals_Last_Updated_By__c` | → | `imax_user`.id | prefix `005` |
| `pse__Actuals_Last_Updated_By__c` | → | `ipsa_user`.id | prefix `005` |
| `pse__Backlog_Last_Updated_By__c` | → | `imax_user`.id | prefix `005` |
| `pse__Backlog_Last_Updated_By__c` | → | `ipsa_user`.id | prefix `005` |
| `pse__Email_Alert_Recipient__c` | → | `imax_contact`.id | prefix `003` |
| `pse__Email_Alert_Recipient__c` | → | `ipsa_contact`.id | prefix `003` |
| `pse__Master_Project__c` | → | `ipsa_proj_c`.id | prefix `a3L` |
| `pse__Master_Project__c` | → | `nar_hpm_psa_projects`.id | prefix `a3L` |
| `pse__Master_Project__c` | → | `vproject_milestone_dates`.id | prefix `a3L` |
| `pse__Opportunity_Owner__c` | → | `imax_user`.id | prefix `005` |
| `pse__Opportunity_Owner__c` | → | `ipsa_user`.id | prefix `005` |
| `pse__Opportunity__c` | → | `ipsa_opportunity`.id | prefix `006` |
| `pse__Opportunity__c` | → | `xplenty_staging_365363`.id | prefix `006` |
| `pse__Parent_Project__c` | → | `ipsa_proj_c`.id | prefix `a3L` |
| `pse__Parent_Project__c` | → | `nar_hpm_psa_projects`.id | prefix `a3L` |
| `pse__Parent_Project__c` | → | `vproject_milestone_dates`.id | prefix `a3L` |
| `pse__Practice__c` | → | `ipsa_practice_c`.id | prefix `a3K` |
| `pse__Project_ID_Chain__c` | → | `ipsa_proj_c`.id | prefix `a3L` |
| `pse__Project_ID_Chain__c` | → | `nar_hpm_psa_projects`.id | prefix `a3L` |
| `pse__Project_ID_Chain__c` | → | `vproject_milestone_dates`.id | prefix `a3L` |
| `pse__Project_Manager__c` | → | `imax_contact`.id | prefix `003` |
| `pse__Project_Manager__c` | → | `ipsa_contact`.id | prefix `003` |
| `pse__Region__c` | → | `imax_service_group_skills`.id | prefix `a3Y` |
| `pse__Region__c` | → | `ipsa_pse_region_c`.id | prefix `a3Y` |
| `pse__Work_Calendar__c` | → | `ipsa_work_calendar_c`.id | prefix `a48` |

### ipsa_project_change__c

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `Change_Requestor__c` | → | `imax_contact`.id | prefix `003` |
| `Change_Requestor__c` | → | `ipsa_contact`.id | prefix `003` |
| `Changes_Approved_By_1__c` | → | `imax_contact`.id | prefix `003` |
| `Changes_Approved_By_1__c` | → | `ipsa_contact`.id | prefix `003` |
| `Changes_Approved_By_2__c` | → | `imax_contact`.id | prefix `003` |
| `Changes_Approved_By_2__c` | → | `ipsa_contact`.id | prefix `003` |
| `Changes_Approved_By_3__c` | → | `imax_contact`.id | prefix `003` |
| `Changes_Approved_By_3__c` | → | `ipsa_contact`.id | prefix `003` |
| `Changes_Approved_By_4__c` | → | `imax_contact`.id | prefix `003` |
| `Changes_Approved_By_4__c` | → | `ipsa_contact`.id | prefix `003` |
| `PSA_Approver__c` | → | `imax_user`.id | prefix `005` |
| `PSA_Approver__c` | → | `ipsa_user`.id | prefix `005` |
| `PSA_Request_Evaluated_by__c` | → | `imax_contact`.id | prefix `003` |
| `PSA_Request_Evaluated_by__c` | → | `ipsa_contact`.id | prefix `003` |
| `Project__c` | → | `ipsa_proj_c`.id | prefix `a3L` |
| `Project__c` | → | `nar_hpm_psa_projects`.id | prefix `a3L` |
| `Project__c` | → | `vproject_milestone_dates`.id | prefix `a3L` |

### ipsa_project_contacts__c

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `Clinical_Technical_Resource__c` | → | `imax_contact`.id | prefix `003` |
| `Clinical_Technical_Resource__c` | → | `ipsa_contact`.id | prefix `003` |
| `Current_Contact_Name__c` | → | `imax_contact`.id | prefix `003` |
| `Current_Contact_Name__c` | → | `ipsa_contact`.id | prefix `003` |
| `Name__c` | → | `imax_contact`.id | prefix `003` |
| `Name__c` | → | `ipsa_contact`.id | prefix `003` |
| `PSA_Business_Group__c` | → | `ipsa_practice_c`.id | prefix `a3K` |
| `PSA_Project_Survey__c` | → | `ipsa_proj_c`.id | prefix `a3L` |
| `PSA_Project_Survey__c` | → | `nar_hpm_psa_projects`.id | prefix `a3L` |
| `PSA_Project_Survey__c` | → | `vproject_milestone_dates`.id | prefix `a3L` |
| `Prior_Contact__c` | → | `imax_contact`.id | prefix `003` |
| `Prior_Contact__c` | → | `ipsa_contact`.id | prefix `003` |
| `Project_Sales_Order__c` | → | `ipsa_project_order_link__c`.id | prefix `aLX` |
| `Project_Sales_Order__c` | → | `vpsa_nar_ol`.id | prefix `aLX` |
| `Project__c` | → | `ipsa_proj_c`.id | prefix `a3L` |
| `Project__c` | → | `nar_hpm_psa_projects`.id | prefix `a3L` |
| `Project__c` | → | `vproject_milestone_dates`.id | prefix `a3L` |

### ipsa_project_order_link__c

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `IQ_Contact__c` | → | `imax_contact`.id | prefix `003` |
| `IQ_Contact__c` | → | `ipsa_contact`.id | prefix `003` |
| `Project__c` | → | `ipsa_proj_c`.id | prefix `a3L` |
| `Project__c` | → | `nar_hpm_psa_projects`.id | prefix `a3L` |
| `Project__c` | → | `vproject_milestone_dates`.id | prefix `a3L` |

### ipsa_project_task

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `PSA_Opportunity__c` | → | `ipsa_opportunity`.id | prefix `006` |
| `PSA_Opportunity__c` | → | `xplenty_staging_365363`.id | prefix `006` |
| `PSA_Project__c` | → | `ipsa_proj_c`.id | prefix `a3L` |
| `PSA_Project__c` | → | `nar_hpm_psa_projects`.id | prefix `a3L` |
| `PSA_Project__c` | → | `vproject_milestone_dates`.id | prefix `a3L` |
| `pse__Milestone__c` | → | `ipsa_pse_milestone_c`.id | prefix `a3C` |
| `pse__Parent_Task__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `pse__Parent_Task__c` | → | `ipsa_project_task`.id | prefix `a3V` |
| `pse__Project__c` | → | `ipsa_proj_c`.id | prefix `a3L` |
| `pse__Project__c` | → | `nar_hpm_psa_projects`.id | prefix `a3L` |
| `pse__Project__c` | → | `vproject_milestone_dates`.id | prefix `a3L` |
| `pse__Top_level_Parent_Task__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `pse__Top_level_Parent_Task__c` | → | `ipsa_project_task`.id | prefix `a3V` |

### ipsa_pse__task_time__c

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `pse__Project_Task__c` | → | `imax_service_group_members`.id | prefix `a3V` |
| `pse__Project_Task__c` | → | `ipsa_project_task`.id | prefix `a3V` |
| `pse__Timecard__c` | → | `ipsa_timecard_header_c`.id | prefix `a3x` |

### ipsa_pse_milestone_c

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `CPM_Project_Order_Link__c` | → | `ipsa_project_order_link__c`.id | prefix `aLX` |
| `CPM_Project_Order_Link__c` | → | `vpsa_nar_ol`.id | prefix `aLX` |
| `PSA_Parent_Deliverable_Name__c` | → | `ipsa_pse_milestone_c`.id | prefix `a3C` |
| `Project_Record_Id__c` | → | `ipsa_proj_c`.id | prefix `a3L` |
| `Project_Record_Id__c` | → | `nar_hpm_psa_projects`.id | prefix `a3L` |
| `Project_Record_Id__c` | → | `vproject_milestone_dates`.id | prefix `a3L` |
| `pse__Approver__c` | → | `imax_user`.id | prefix `005` |
| `pse__Approver__c` | → | `ipsa_user`.id | prefix `005` |
| `pse__Project__c` | → | `ipsa_proj_c`.id | prefix `a3L` |
| `pse__Project__c` | → | `nar_hpm_psa_projects`.id | prefix `a3L` |
| `pse__Project__c` | → | `vproject_milestone_dates`.id | prefix `a3L` |
| `pse__Vendor_Account__c` | → | `imax_account`.id | prefix `001` |
| `pse__Vendor_Account__c` | → | `ipsa_account`.id | prefix `001` |

### ipsa_pse_region_c

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `pse__Actuals_Last_Updated_By__c` | → | `imax_user`.id | prefix `005` |
| `pse__Actuals_Last_Updated_By__c` | → | `ipsa_user`.id | prefix `005` |
| `pse__Backlog_Last_Updated_By__c` | → | `imax_user`.id | prefix `005` |
| `pse__Backlog_Last_Updated_By__c` | → | `ipsa_user`.id | prefix `005` |
| `pse__Headquarters_Region__c` | → | `imax_service_group_skills`.id | prefix `a3Y` |
| `pse__Headquarters_Region__c` | → | `ipsa_pse_region_c`.id | prefix `a3Y` |
| `pse__Parent_Region__c` | → | `imax_service_group_skills`.id | prefix `a3Y` |
| `pse__Parent_Region__c` | → | `ipsa_pse_region_c`.id | prefix `a3Y` |
| `pse__Plan_Last_Updated_By__c` | → | `imax_user`.id | prefix `005` |
| `pse__Plan_Last_Updated_By__c` | → | `ipsa_user`.id | prefix `005` |
| `pse__Utilization_Last_Updated_By__c` | → | `imax_user`.id | prefix `005` |
| `pse__Utilization_Last_Updated_By__c` | → | `ipsa_user`.id | prefix `005` |

### ipsa_resource_request_c

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `Escalated_By__c` | → | `imax_contact`.id | prefix `003` |
| `Escalated_By__c` | → | `ipsa_contact`.id | prefix `003` |
| `PSA_Delivery_Contact__c` | → | `ipsa_project_contacts__c`.id | prefix `a9C` |
| `PSA_Hospital_Clinical_Contact__c` | → | `ipsa_project_contacts__c`.id | prefix `a9C` |
| `PSA_Modality__c` | → | `ipsa_practice_c`.id | prefix `a3K` |
| `PSA_Parent_RR_No__c` | → | `ipsa_resource_request_c`.id | prefix `a3f` |
| `PSA_Project_Order_Link__c` | → | `ipsa_project_order_link__c`.id | prefix `aLX` |
| `PSA_Project_Order_Link__c` | → | `vpsa_nar_ol`.id | prefix `aLX` |
| `Regional_Service_Manager__c` | → | `imax_contact`.id | prefix `003` |
| `Regional_Service_Manager__c` | → | `ipsa_contact`.id | prefix `003` |
| `Request_Approver__c` | → | `imax_contact`.id | prefix `003` |
| `Request_Approver__c` | → | `ipsa_contact`.id | prefix `003` |
| `pse__AccountId__c` | → | `imax_account`.id | prefix `001` |
| `pse__AccountId__c` | → | `ipsa_account`.id | prefix `001` |
| `pse__Assignment__c` | → | `ipsa_assignment__c`.id | prefix `a2g` |
| `pse__Milestone__c` | → | `ipsa_pse_milestone_c`.id | prefix `a3C` |
| `pse__Opportunity__c` | → | `ipsa_opportunity`.id | prefix `006` |
| `pse__Opportunity__c` | → | `xplenty_staging_365363`.id | prefix `006` |
| `pse__Practice__c` | → | `ipsa_practice_c`.id | prefix `a3K` |
| `pse__Project__c` | → | `ipsa_proj_c`.id | prefix `a3L` |
| `pse__Project__c` | → | `nar_hpm_psa_projects`.id | prefix `a3L` |
| `pse__Project__c` | → | `vproject_milestone_dates`.id | prefix `a3L` |
| `pse__Region__c` | → | `imax_service_group_skills`.id | prefix `a3Y` |
| `pse__Region__c` | → | `ipsa_pse_region_c`.id | prefix `a3Y` |
| `pse__Resource__c` | → | `imax_contact`.id | prefix `003` |
| `pse__Resource__c` | → | `ipsa_contact`.id | prefix `003` |
| `pse__Staffer_Resource__c` | → | `imax_contact`.id | prefix `003` |
| `pse__Staffer_Resource__c` | → | `ipsa_contact`.id | prefix `003` |

### ipsa_sales_order_line_item

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `Milestone_ID__c` | → | `ipsa_pse_milestone_c`.id | prefix `a3C` |
| `OpportunityRecordType__c` | → | `imax_recordtype`.id | prefix `012` |
| `OpportunityRecordType__c` | → | `ipsa_recordtype`.id | prefix `012` |
| `Project__c` | → | `ipsa_proj_c`.id | prefix `a3L` |
| `Project__c` | → | `nar_hpm_psa_projects`.id | prefix `a3L` |
| `Project__c` | → | `vproject_milestone_dates`.id | prefix `a3L` |

### ipsa_timecard_c

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `pse__Assignment__c` | → | `ipsa_assignment__c`.id | prefix `a2g` |
| `pse__Milestone__c` | → | `ipsa_pse_milestone_c`.id | prefix `a3C` |
| `pse__Project__c` | → | `ipsa_proj_c`.id | prefix `a3L` |
| `pse__Project__c` | → | `nar_hpm_psa_projects`.id | prefix `a3L` |
| `pse__Project__c` | → | `vproject_milestone_dates`.id | prefix `a3L` |
| `pse__Resource__c` | → | `imax_contact`.id | prefix `003` |
| `pse__Resource__c` | → | `ipsa_contact`.id | prefix `003` |
| `pse__Timecard_Header__c` | → | `ipsa_timecard_header_c`.id | prefix `a3x` |

### ipsa_timecard_header_c

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `PSA_Approver_Manager__c` | → | `imax_user`.id | prefix `005` |
| `PSA_Approver_Manager__c` | → | `ipsa_user`.id | prefix `005` |
| `PSA_Resource_Manager__c` | → | `imax_user`.id | prefix `005` |
| `PSA_Resource_Manager__c` | → | `ipsa_user`.id | prefix `005` |
| `pse__Approver__c` | → | `imax_user`.id | prefix `005` |
| `pse__Approver__c` | → | `ipsa_user`.id | prefix `005` |
| `pse__Assignment__c` | → | `ipsa_assignment__c`.id | prefix `a2g` |
| `pse__Milestone__c` | → | `ipsa_pse_milestone_c`.id | prefix `a3C` |
| `pse__Project__c` | → | `ipsa_proj_c`.id | prefix `a3L` |
| `pse__Project__c` | → | `nar_hpm_psa_projects`.id | prefix `a3L` |
| `pse__Project__c` | → | `vproject_milestone_dates`.id | prefix `a3L` |
| `pse__Resource__c` | → | `imax_contact`.id | prefix `003` |
| `pse__Resource__c` | → | `ipsa_contact`.id | prefix `003` |

### ipsa_user

| Column | → | Target Table | Confidence |
|--------|---|--------------|------------|
| `DAR_User_Type__c` | → | `imax_user`.id | prefix `005` |
| `DAR_User_Type__c` | → | `ipsa_user`.id | prefix `005` |
| `SFDC_User_ID__c` | → | `imax_user`.id | prefix `005` |
| `SFDC_User_ID__c` | → | `ipsa_user`.id | prefix `005` |

## Notes

- These are **inferred** relationships based on ID prefix matching
- Some may be false positives if IDs happen to match patterns
- Review and validate before using in production queries
