# Check CSV Upload for correct formatting

This script can be ran to check if a contacts csv file for upload has phone and email in the correct format. Can probably be extended to the custom fields as well later.

Will output a CSV that lists what rows are incorrect and what column is incorrect for that row. 

Note: The script currently only considers US phone numbers so the regex being matched on will need to be updated if you need to check for additional country code and number formats.
The script can also take a Front Accounts export as an input file to check against the customer's provided CSV. THis will detect any differences in account names across the their existing accounts and the provided contacts.csv. It's important to note Front's uploader will fail if an accountName is provided in the import file that doesn't exist. 