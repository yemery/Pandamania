#Excel to CSV Converter and Column Exporter
<br/>
This is a Python script that converts an Excel file to a CSV file and exports specified columns. The script uses the Pandas library to read and manipulate Excel and CSV files, and the sys module to accept input and output file names and column names from the command line.
<br/>

###Requirements
<br/>
-Python 3.6 or higher
-Pandas library
-sys module
<br/>

###Installation
<br/>
-Clone the repository to your local machine.
-Install Python 3.6 or higher if it is not already installed.
-Install the Pandas library by running pip install pandas in your terminal or command prompt.
-The sys module is included in the Python standard library and does not need to be installed separately.
<br/>

###Excel to CSV Converter
<br/>

The excel_to_csv.py script converts an Excel file to a CSV file. To use the script, run the following command in your terminal or command prompt:
<br/>

```python excel_to_csv.py input_file output_file```
<br/>

Replace input_file with the name of the Excel file you want to convert, and replace output_file with the name you want to save the CSV file as.
The script will convert the Excel file to a CSV file and save it to the output file.
<br/>

###Column Exporter
<br/>

The column_exporter.py script exports specified columns from an Excel file to a CSV file. To use the script, run the following command in your terminal or command prompt:
<br/>
```python column_exporter.py input_file output_file column1 column2 ...```
<br/>

Replace input_file with the name of the Excel file you want to export columns from, replace output_file with the name you want to save the CSV file as, and replace column1, column2, etc. with the names of the columns you want to export.
The script will export the specified columns from the Excel file to a CSV file and save it to the output file.
