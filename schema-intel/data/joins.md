# Join Definitions

This document defines all known relationships between tables. Used by build_db.py to populate the `joins` table.

---

## Backlog Report Joins

### pse__milestone__c → pse_deliverable_related_info__c
- **Join column:** Id = pse__Milestone__c
- **Type:** LEFT JOIN
- **Cardinality:** one-to-many (milestone has many DRI rows)
- **Notes:** DRI is the bridge table; milestone is the central entity

### pse_deliverable_related_info__c → pse__assignment__c
- **Join column:** PSA_Assignment__c = Id
- **Type:** LEFT JOIN
- **Cardinality:** many-to-one
- **Notes:** Links deliverable to who is doing the work

### pse__assignment__c → pse__proj__c
- **Join column:** pse__Project__c = Id
- **Type:** LEFT JOIN
- **Cardinality:** many-to-one
- **Notes:** Links assignment to its parent project

### pse__assignment__c → contact
- **Join column:** pse__Resource__c = Id
- **Type:** LEFT JOIN
- **Cardinality:** many-to-one
- **Notes:** Links assignment to resource (employee) doing the work

### pse_deliverable_related_info__c → mp1_material
- **Join column:** PSA_Material_Number__c = materialnumber
- **Type:** LEFT JOIN
- **Cardinality:** many-to-one
- **Notes:** Material number must be zero-padded to 18 chars (LPAD) for join

### mp1_material → mp1_mbew
- **Join column:** materialnumber + plant = MATNR + BWKEY
- **Type:** LEFT JOIN
- **Cardinality:** one-to-one (per plant)
- **Notes:** Composite key join; mbew has pricing data

### pse__proj__c → zone_mapping
- **Join column:** state = state
- **Type:** LEFT JOIN
- **Cardinality:** many-to-one
- **Notes:** Use COALESCE(proj.state, mile.state) for fallback

### pse__milestone__c → zone_mapping
- **Join column:** PSA_State_Province__c = state
- **Type:** LEFT JOIN
- **Cardinality:** many-to-one
- **Notes:** Fallback when project state is null

---

## Timecard Report Joins

### project_timecard → pse__timecard__c
- **Join column:** Timecard_Name = Name
- **Type:** LEFT JOIN
- **Cardinality:** one-to-one
- **Notes:** project_timecard (xt) is denormalized starting point

### pse__timecard__c → pse__task_time__c
- **Join column:** Id = pse__Timecard__c
- **Type:** LEFT JOIN
- **Cardinality:** one-to-many
- **Notes:** Only for Regular Work; Time Off has no task_time rows

### pse__task_time__c → pse__project_task__c
- **Join column:** pse__Project_Task__c = Id
- **Type:** LEFT JOIN
- **Cardinality:** many-to-one
- **Notes:** Links time entry to specific project task

### project_timecard → contact
- **Join column:** Resource_Name = Name
- **Type:** LEFT JOIN
- **Cardinality:** many-to-one
- **Notes:** Resource lookup by name

### pse__assignment__c → user
- **Join column:** pse__Manager__c = Id
- **Type:** LEFT JOIN
- **Cardinality:** many-to-one
- **Notes:** Manager lookup; NULL for time-off (use window function)

---

## Bench Tracker Joins

### imax_bench_status_tracker__c → imax_case
- **Join column:** ESMX_Case__c = Id
- **Type:** INNER JOIN or LEFT JOIN
- **Cardinality:** many-to-one
- **Notes:** Core join for bench repair data

### imax_case → imax_account
- **Join column:** Account_Number__c = AccountNumber
- **Type:** INNER JOIN
- **Cardinality:** many-to-one
- **Notes:** Account/customer information

### imax_case → imax_installed_product_c
- **Join column:** ESMX_Reference_Installed_Product__c = Id
- **Type:** LEFT JOIN (optional)
- **Cardinality:** many-to-one
- **Notes:** Equipment details

---

## iMax Table Relationships

### imax_case → imax_case_line
- **Join column:** Id = (case reference column)
- **Type:** LEFT JOIN
- **Cardinality:** one-to-many
- **Notes:** Case line items

### imax_case → imax_service_order_c
- **Join column:** Id = (case reference column)
- **Type:** LEFT JOIN
- **Cardinality:** one-to-many
- **Notes:** Service orders for a case

### imax_service_order_c → imax_service_order_line__c
- **Join column:** Id = (service order reference)
- **Type:** LEFT JOIN
- **Cardinality:** one-to-many
- **Notes:** Line items on service order

---

## Reference Table Joins

### zone_mapping
- **Standalone reference table**
- **Join on:** state (full state name)
- **Provides:** di_zone, igt_zone for regional grouping
- **Location:** qa_wb.nam_data_science.zone_mapping
