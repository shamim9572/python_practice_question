def main():
    n = int(input("Enter Input: "))
    
    if n < 1 or n % 2 == 1:
        return

    # Upper part of the pattern
    for i in range(n // 2):
        for j in range(n // 2):
            print(" ", end="")
        for j in range(i):
            print(" ", end="")
        for j in range(n - (2 * i)):
            print("@", end="")
        print()

    # Lower part of the pattern
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

if __name__ == "__main__":
    main()
