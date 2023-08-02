# CST8333-S23-Project
This repo includes the practical projects for the course Programming Language Research CST8333.
The language used is Python with SQLite database.

### Dependencies
For the project to run, you'll need to install its dependencies. 
- From the project root folder "CST8333_S23", open the terminal or CMD
- Run the following command `pip install -r requirements.txt`
- This should download and install the required dependencies.

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

## practical project part 3
*due date July 23 2023.*

Augment your project, developed via Practical Project Part 2, by utilizing one advanced language feature from the list below, using the examples as a guide.
<br/>[List of the advanced features]

The selected advanced feature is Database Connectivity.
- Database Connectivity
	- Create a database table with fields named after the column names, and use a database driver, to connect your program to a database. This can replace the reliance on the File-IO of the dataset. Your Create, Read, Update, and Delete options would then manipulate the database rather than the CSV file.
	- Populate the database table with all the data from the dataset, using field names in the database table

## practical project part 4
*due date August 06 2023.*

Modify your project to add additional functionality by utilizing the data set data to offer a new project feature to the user, Choose one of
- Horizontal Bar Chart
- Vertical Bar Chart
- Pie Chart
- Search records based on multiple columns at same time
- Sort records based on multiple columns at same time, in a selected order (*Selected)

The user must be able to interact with the program at run time to customize the output, for example what parts of the data to chart or perform a search or sort on.


