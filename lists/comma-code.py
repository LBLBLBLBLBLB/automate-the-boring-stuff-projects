def comma_code(spam):
    string = ''
    if len(spam) == 0:
        return 'list is empty'
    elif len(spam) == 1:
        return spam[0]

    for i in range(0,len(spam)):
        if i == len(spam)-1:
            string += f'and {spam[i]}'
        else:
            string += f'{spam[i]}, '
    return string


def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    result = comma_code(spam)
    print(result)

    empty_list_result = comma_code([])
    print(empty_list_result)

    single_element_result = comma_code(['apples'])
    print(single_element_result)


if __name__ == "__main__":
    main()
