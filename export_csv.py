import pandas as pd
import csv
import sys

def export_to_csv(input_file, output_file, columns):
    df = pd.read_excel(input_file)
    
    df = df[columns]

    df.to_csv(output_file, index=False, quoting=csv.QUOTE_NONNUMERIC)

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    columns = sys.argv[3:]

    export_to_csv(input_file, output_file, columns)
