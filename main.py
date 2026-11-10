def duplicate(sring):

    if len(string) == 0:
        return True

    if len(string) % 2 != 0:
        return False

    middle = len(string) // 2

    if string[:middle] == string[middle:]:
        return True
    else:
        return False


string = input("Enter string: ")

if duplicate(string):
    print("Duplicate")
else:
    print("Not Duplicate")
