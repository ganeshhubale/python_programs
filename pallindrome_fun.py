def pallindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    s = input("Enter string: ")
    if pallindrome(s):
        print("Pallindrome string!")
    else:
        print("Not Pallindrome string!")
