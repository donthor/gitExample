def doubler(number):
    result = number * 2
    return result
get_number = float(input("Type a number: "))
print('Getting your answer')
answer = doubler(get_number)
print(f'Your answer is: {answer}')
