def reverse(number) :
""" This function reverses the digits of number """
    reverse_number = 0
    n = number

    while n > 0 :
        reverse_number *= 10
        reverse_number += n % 10
        n //= 10

    return reverse_number
