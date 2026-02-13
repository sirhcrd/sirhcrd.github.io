---
type: id-prefixes
generated_date: 2026-02-12
prefix_count: 37
---

# Salesforce ID Prefix Decoder

Salesforce IDs use a 3-character prefix to identify the object type.
Use this reference to decode IDs and find their source tables.

## Prefix Reference

| Prefix | Table(s) | Example |
|--------|----------|---------|
| `001` | `imax_account`, `ipsa_account` | |
| `003` | `imax_contact`, `ipsa_contact` | |
| `005` | `imax_user`, `ipsa_user` | |
| `006` | `ipsa_opportunity`, `xplenty_staging_365363` | |
| `008` | `ipsa_opportunity_history` | |
| `00E` | `ipsa_userrole` | |
| `00G` | `ipsa_group` | |
| `00e` | `ipsa_profile` | |
| `012` | `imax_recordtype`, `ipsa_recordtype` | |
| `017` | `imax_managed_equipment_history`, `ipsa_contacthistory`, `ipsa_cpm_key_date_audit_trail_history`, `ipsa_project_change_history`, `ipsa_project_order_link_history`, `ipsa_pse_missing_timecard_history`, `ipsa_timecard_history` | |
| `01t` | `imax_product2`, `v_products__aa` | |
| `02c` | `ipsa_timecard_header_share` | |
| `500` | `imax_case` | |
| `a0o` | `ipsa_region` | |
| `a1E` | `ipsa_sales_order_line_item` | |
| `a1x` | `imax_activity` | |
| `a2J` | `imax_case_line`, `vsmax_nar_cl_install` | |
| `a2W` | `imax_installed_product_c` | |
| `a2g` | `ipsa_assignment__c` | |
| `a3C` | `ipsa_pse_milestone_c` | |
| `a3E` | `ipsa_missing_timecard__c` | |
| `a3K` | `ipsa_practice_c` | |
| `a3L` | `ipsa_proj_c`, `nar_hpm_psa_projects`, `vproject_milestone_dates` | |
| `a3T` | `imax_service_contract` | |
| `a3V` | `imax_service_group_members`, `ipsa_project_task` | |
| `a3Y` | `imax_service_group_skills`, `ipsa_pse_region_c` | |
| `a3c` | `imax_service_order_line` | |
| `a3d` | `imax_service_order_c` | |
| `a3f` | `ipsa_resource_request_c` | |
| `a3q` | `ipsa_pse__task_time__c` | |
| `a3x` | `ipsa_timecard_header_c` | |
| `a3y` | `ipsa_timecard_c` | |
| `a48` | `ipsa_work_calendar_c` | |
| `a4D` | `imax_contract_header` | |
| `a9C` | `ipsa_project_contacts__c` | |
| `aAC` | `ipsa_project_change__c` | |
| `aLX` | `ipsa_project_order_link__c`, `vpsa_nar_ol` | |

## How to Use

When you see a Salesforce ID like `001E000001XsEHhIAN`:
1. Take the first 3 characters: `001`
2. Look up in the table above → `imax_account`
3. Query that table with `WHERE id = '001E000001XsEHhIAN'`
