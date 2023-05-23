def is_automorphic(num):
    square = num ** 2
    str_num = str(num)
    str_square = str(square)

    if str_square.endswith(str_num):
        return True
    else:
        return False

number = int(input())

if is_automorphic(number):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
