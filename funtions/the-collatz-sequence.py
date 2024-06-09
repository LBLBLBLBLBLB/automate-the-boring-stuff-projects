def collatz(number):
    if number % 2 == 0:
        num = number // 2
        print(num)
        return num
    else:
        num = 3 * number + 1
        print(num)
        return num


def main():
    try:
        n = int(input("enter an integer: "))
        while n != 1:
            n = collatz(n)
            print(n)
    except ValueError:
        print('please enter a valid integer')


if __name__ == "__main__":
    main()
