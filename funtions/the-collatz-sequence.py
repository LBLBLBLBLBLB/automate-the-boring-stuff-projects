def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1

def main():
    try:
        num = int(input('enter number: \n'))
        while num != 1:
            num = collatz(num)
            print(num)
    except ValueError:
        print("Please enter integer")

if __name__ == "__main__":
    main()
