import pandas as pd
import argparse


def collector_extractor(input_file,output_file):
    df = pd.read_excel(input_file)

    unique_values = {}

    for index, row in df.iterrows():
        row_tuple = tuple(row)
        if any(row_tuple):
            unique_values[row_tuple] = list(set(row_tuple) - {None})

    df_unique = pd.DataFrame.from_dict(unique_values, orient='index')

    df_unique.to_excel(output_file, index=False, header=list(df.columns))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract unique values from non-empty rows of an Excel file')
    parser.add_argument('input_file', type=str, help='Input Excel file name')
    parser.add_argument('output_file', type=str, help='Output Excel file name')
    args = parser.parse_args()

    collector_extractor(args.input_file, args.output_file)