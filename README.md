# SEProjectTool
Description:
	A tool that translates MySQL queries into NoSQL queries. The tool will be a web page with a text box to type queries to be converted. Users can also upload files that they want to convert from MySQL to NoSQL.

Existing Works:
	There are some existing tools that work only for simple SQL commands. They will not give correct results for nested queries or special operations like UNION, TABLE JOIN or even little complicated select statements.

How is our tool different from the existing ones:
	We will try to make our tool to be able to convert some of the special operations and nested queries correctly with appropriate code/comment padding in some certain language (like python or JS) that describes the unsupported operations.

# Running The Tool
To run the tool locally on your system:
1. clone the repository using git clone command
2. cd into 'SQLToNoSQLConverter' and then run 'python3 manage.py runserver <opt_port_number>'
	eg : python3 manage.py runserver
3. Now go to http://localhost:8000/converter/home to go to the tool interface
4. Here you can upload/type in the SQL command (in CAPITAL formatted version only -- for current release) and click on convert.
5. Output can be seen in the right side box
