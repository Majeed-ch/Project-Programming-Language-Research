# CST8333-S23-Projects
This repo includes all the projects and assignemnt for the course Programming Language Research CST8333.

## practical project part 1
*due date May 21st 2023.*

- Create a project, in your language of study that meets the following requirements:
  - Create a record object (also known as entity object, data-transfer object) that uses the column names from the dataset as part of the source code, e.g. variable names, accessors/mutators names, or constants.
  - Use File-IO on startup to open and read the dataset, initializing a few record objects with data parsed from the first few records in the csv file. The record objects should be stored in a simple data structure (array or a list), use exception handling in case the file is missing or not available.
  - Loop over the data structure, and output the record data on screen.
  - Displays your full name on screen so it remains visible at all times.
- Take a separate screen shot of your program performing each task above, ensuring your full name is within each screen shot.
- Comment your source code file using documentation comments (docstrings in Python, XML-document in C# or VB.Net, JSDoc for server-side JavaScript etc.)
- Your program should use the following programming concepts: variables, methods, a loop structure, File-IO reading from the dataset, exception handling, use of an API library, an array (or similar data structure).

## practical project part 2
*due date June 18 2023.*

- Project has a layered design and implementation e.g. Presentation, Business, and Persistence with record-objects.
- Use a record object (DTO), that uses the column names from the provided dataset as part of the source code, e.g. variable names, accessors/mutators names, or constants.
- Use File-IO on startup to open and read the dataset, initializing one hundred record objects with data parsed from the first one hundred records in the csv file. The record objects should be stored in a simple data structure (array or a list), use proper exception handling.
- Displays your full name on screen so it remains visible at all times, or after each user interaction.
- Provide the user the interactive options and functionality to:
	- Reload the data from the dataset, replacing the in-memory data.
	- Persist the data from memory to the disk as a comma-separated file, writing to a new file.
	- Select and display either one record, or display multiple records from the in-memory data.
	- Create a new record and store it in the simple data structure in memory.
	- Select and edit a record held in the simple data structure in memory.
	- Select and delete a record from the simple data structure in memory.
