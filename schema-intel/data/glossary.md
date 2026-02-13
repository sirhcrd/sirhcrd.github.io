# Glossary

Business terms mapped to technical table/column names.

| Term | Technical | Description |
|------|-----------|-------------|
| Deliverable | `pse__milestone__c` | A milestone record representing a customer deliverable |
| DRI | `pse_deliverable_related_info__c` | Bridge table linking deliverables to assignments and materials |
| Assignment | `pse__assignment__c` | Who is doing the work — links resources to projects |
| Resource | `contact` | Employee/technician doing the work |
| Case | `imax_case` | Service case/ticket in iMax system |
| Service Order | `imax_service_order_c` | Work order created from a case |
| Installed Product | `imax_installed_product_c` | Equipment/asset at customer site |
| Bench Tracker | `imax_bench_status_tracker__c` | Tracks bench repair lifecycle |
| Zone | `zone_mapping` | Geographic region (DI or IGT zone) |
| Modality | various `*_Modality__c` columns | Product type (CT, MR, X-ray, etc.) |

## System Prefixes

| Prefix | System | Examples |
|--------|--------|----------|
| `pse__` | Salesforce PSA (FinancialForce) | `pse__milestone__c`, `pse__assignment__c` |
| `SVMXC__` | ServiceMax | `SVMXC__Product_Family__c` |
| `ESMX__` | Extended ServiceMax | `ESMX_Case__c` |
| `CPL__` | Custom Philips | `CPL_Product_Modality__c` |
| `PSA_` | PSA custom fields | `PSA_Material_Number__c` |
| `mp1_` | SAP ERP | `mp1_material`, `mp1.mbew` |
