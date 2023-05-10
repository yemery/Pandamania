#Excel to CSV Converter and Column Exporter
This is a Python script that converts an Excel file to a CSV file and exports specified columns. The script uses the Pandas library to read and manipulate Excel and CSV files, and the sys module to accept input and output file names and column names from the command line.

###Requirements
-Python 3.6 or higher
-Pandas library
-sys module

###Installation
-Clone the repository to your local machine.
-Install Python 3.6 or higher if it is not already installed.
-Install the Pandas library by running pip install pandas in your terminal or command prompt.
-The sys module is included in the Python standard library and does not need to be installed separately.

###Excel to CSV Converter
The excel_to_csv.py script converts an Excel file to a CSV file. To use the script, run the following command in your terminal or command prompt:
```python excel_to_csv.py input_file output_file```
Replace input_file with the name of the Excel file you want to convert, and replace output_file with the name you want to save the CSV file as.
The script will convert the Excel file to a CSV file and save it to the output file.

###Column Exporter
The column_exporter.py script exports specified columns from an Excel file to a CSV file. To use the script, run the following command in your terminal or command prompt:
```python column_exporter.py input_file output_file column1 column2 ...```
Replace input_file with the name of the Excel file you want to export columns from, replace output_file with the name you want to save the CSV file as, and replace column1, column2, etc. with the names of the columns you want to export.
The script will export the specified columns from the Excel file to a CSV file and save it to the output file.
