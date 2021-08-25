def create_digits(n):
    digit_list = []
    for num in str(n):
        digit_list.append(num)
    print(digit_list)
    return digit_list
def sum_of_digits(list):
    suma=0
    for digits in list:
        suma=suma + int(digits)
    return suma
def lengt_of_list(number):
    lenght=len(str(number))
    return lenght

def digital_root(n):
    lenght = lengt_of_list(n)
    while lenght>1:
        digits = create_digits(n)
        n = sum_of_digits(digits)
        lenght = lengt_of_list(n)
    return n