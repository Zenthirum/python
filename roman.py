symbols = [('M', 1000), ('CM', 900), ('D', 500),
    ('CD', 400), ('C', 100), ('XC', 90), ('L', 50),
    ('XL', 40), ('X', 10), ('IX', 9), ('V', 5),
    ('IV', 4), ('I', 1)]

def romannumeral(number):
    output_string = ""
    while number > 0:
        for symbol, value in symbols:
            if number - value >= 0:
                output_string = output_string + symbol
                number = number - value
                break
    return output_string
            
if __name__ == '__main__':
    number_in = input("Enter a number: ")
    romannumeral(int(number_in))
