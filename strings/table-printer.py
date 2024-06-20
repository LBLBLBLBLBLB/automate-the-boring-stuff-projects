def table_printer(lst_str):
    col_widths = [0] * len(lst_str)
    
    for i in range(0, len(lst_str)):
        max_width = 0
        for word in lst_str[i]:
            if len(word) > max_width:
                max_width = len(word)   
        col_widths[i] = max_width

    num_rows = len(lst_str[0])
    formatted_table = ''

    for row in range(num_rows):
        row_str = ''
        for col in range(len(lst_str)):
            row_str += lst_str[col][row].rjust(col_widths[col]) + ' '
        formatted_table += row_str.rstrip() + '\n'   

    return formatted_table

if __name__ == "__main__":
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
    print(table_printer(table_data))
