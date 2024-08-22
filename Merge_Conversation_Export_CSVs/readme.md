# Merge Conversation Export CSVs

These scripts can be used to merge a full data/conversation export into one singular CSV. It will traverse the export folder structure, pull out each individual message CSV from each Conversation folder
and then merge those messages into a single CSV. The script adds a new column called Conversation Folder which is just the Conversation ID for which that message belongs to.

Super useful for customers that want all their messages in a single CSV file.

Included is a secondary merge_filtered.py file that allows for filtering of specific rows in the CSV. In the current code it's checking for any mention of the string LEED in From, To, Subject, and Text columns. I believe the customer wanted to check for any mention of the word LEED in these fields. Adjust if needed. 