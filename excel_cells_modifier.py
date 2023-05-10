import argparse
import pandas as pd

def modify_locality_column(input_file, output_file, locality_col, entity_col, search_string):
    df = pd.read_excel(input_file)
    # df.loc[df[locality_col].str.contains(search_string), locality_col] = df[entity_col]
    # df.loc[df[locality_col].str.contains(search_string), locality_col] = df[entity_col]
    df.loc[df[locality_col].str.contains(search_string), locality_col] = df.loc[df[locality_col].str.contains(search_string), entity_col]

    df.to_excel(output_file, index=False)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Modify the locality column in an Excel file.')
    parser.add_argument('input_file', help='the name of the input Excel file')
    parser.add_argument('output_file', help='the name of the output Excel file')
    parser.add_argument('locality_col', help='the name of the locality column')
    parser.add_argument('entity_col', help='the name of the entity column')
    parser.add_argument('search_string', help='the string to search for in the locality column')
    
    args = parser.parse_args()
    
    modify_locality_column(args.input_file, args.output_file, args.locality_col, args.entity_col, args.search_string)
