# Remove a field from a JSON that's inside a CSV Column

This script allows you to remove a field from within a JSON when it's inside a CSV column. 

Super useful for when you need to remove data from a JSON object so it can be shared with a customer. 

Example use case would be the JSON that's generated when a application webhook recieves an unexpected/error status. The error JSON we create in logs contains important information for the customer but also private Front data. So it's important to remove the private data so we can share the error details with the customer :D 