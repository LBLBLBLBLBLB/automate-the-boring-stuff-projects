def comma_code(spam):
    string = ''
    if len(spam) == 0:
        return 'list is empty'    
    elif len(spam) == 1:
        return spam[0]
    elif len(spam) > 1:
        for i in range(0,len(spam)-1):
            string += spam[i] + ','      
        string += f' and {spam[-1]}'
    return string


def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    result = comma_code(spam)
    print('multiple element result ')
    print(result, '\n')

    empty_list_result = comma_code([])
    print('empty list result ')
    print(empty_list_result, '\n')

    single_element_result = comma_code(['apples'])
    print('single element result ')
    print(single_element_result, '\n')


if __name__ == "__main__":
    main()
