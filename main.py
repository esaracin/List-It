#
#
# Eli Saracino (esaracin@bu.edu)
# 4/9/2022
#
#

import sys

def clean_list(column_lst, char_to_remove='', char_to_add=''):
    """
    Takes a list of strings representing the input column, and cleans the data.
    Cleaning include removal of empty/newline rows, removal of any specified characters
    from around the values, and addition of any new characters around the values.
    """

    clean_data = []

    for data_elem in column_lst:
        # Ignore any blank elements
        if not (data_elem == '' or data_elem == ' ' or data_elem == '\n'):
            # Remove any unwanted characters
            data_elem = data_elem.replace(char_to_remove, '')

            # Addition of new characters
            data_elem = char_to_add + data_elem + char_to_add
            clean_data.append(data_elem)


    return clean_data

def delimit_data(column_str, delimiter=',', char_to_remove='', char_to_add=''):
    """
    Takes a string of columnized data, and a delimiter. Returns a string of
    the columnized data as a single line, delimited by the passed delimiter.
    """
    column_data_lst = column_str.split('\n')
    if column_data_lst[-1] == '' or column_data_lst[-1] == ' ':
        column_data_lst = column_data_lst[:-1]

    column_data_lst = clean_list(column_data_lst, char_to_add=char_to_add, char_to_remove=char_to_remove)

    return delimiter.join(column_data_lst)

def main():
    f = open('test_inputs/input01_std.txt', 'r')
    column_string1 = f.read()
    f.close()


    f = open('test_inputs/input02_blank_lines.txt', 'r')
    column_string2 = f.read()
    f.close()


    f = open('test_inputs/input03_char_removal.txt', 'r')
    column_string3 = f.read()
    f.close()

    print(delimit_data(column_string1, char_to_add='"'))
    print(delimit_data(column_string2, char_to_add='"'))
    print(delimit_data(column_string3, char_to_add='"', char_to_remove="'"))

if __name__ == '__main__':
    main()
