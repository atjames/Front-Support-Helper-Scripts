# Check CSV Upload for correct formatting

This script can be ran to check if a provided contacts csv has phone/email in the correct format. 

Will output a txt file that gives information on what fields are incorrect and which row they are contained. 

Note: The script currently only considers US phone numbers so the regex being matched on will need to be updated if you need to check for additional country code and number formats.
The script can also take a Front Accounts export as an input file to check against the customer's provided CSV. THis will detect any differences in account names across the their existing accounts and the provided contacts.csv. It's important to note Front's uploader will fail if an accountName is provided in the import file that doesn't exist. 