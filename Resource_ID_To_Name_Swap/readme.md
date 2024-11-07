# Swap tag names for their IDs

This script takes two CSVs for input. One is a Tags export that can be pulled via the Tag Export plug-in which contains the public ID of tag objects. 

The second csv would contain tags where they are only identified by name. 

The goal here is to replace the name of a tag with it's public API ID. Please note the column's used will need to be adjusted based on the CSV you are using. 
Could also adjust this to work with different resources. 

Script will out two CSVs. One that has run the swap between name and public API ID, and another where the name did not match any public API IDs in the tag export file.