# Processing notes

### Downloaded Rangeland Administration System data reports from BLM website
Ran reports for each state office (AZ, CA, CO, ID, MT, NM, NV, OR, UT, WY) for each table (operators, allotments, permits). Downloads came in xlsx format.

### Convert to CSV, load each state file into a SQL database.

### Merge permit-specific data from allotments table into permits table

First create a field that has a unique allotment ID using state and allotment ID (allotment IDs are unique within states):

      alter table permits
      add column new_allotment_id varchar(20)

      update permits
      set new_allotment_id = concat(substring(off_cd, 3, 2), allotment_number)

Then make the join using authorization number (unique to operator) and new allotment number (unique to allotment):

      select permits.*, allotments.new_allotment_id, allotments.auth_no, allotments.permitted_aums, allotments.suspended_aums, allotments.susp_use_temp
      from permits
      left outer join allotments on  permits.auth_no = allotments.auth_no and permits.new_allotment_id = allotments.new_allotment_id
      order by suspended_aums desc


### Select only distinct allotments to avoid over-counting public acreage
