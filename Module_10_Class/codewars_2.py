# Write a function taking in a string like WOW this is REALLY          amazing and returning Wow this is really amazing. String should be capitalized and properly spaced. Using re and string is not allowed.

# Examples:

# filter_words('HELLO CAN YOU HEAR ME') #=> Hello can you hear me
# filter_words('now THIS is REALLY interesting') #=> Now this is really interesting
# filter_words('THAT was EXTRAORDINARY!') #=> That was extraordinary!
# 'Qklgkqe  lrncqsbvmkmnh  ijfoqzsyyuamkq  ockk  eweffevw' should equal 'Qklgkqe lrncqsbvmkmnh ijfoqzsyyuamkq ockk eweffevw'

def filter_words(st):
    st = ' '.join(st.split())
    return st.capitalize()


# filter_words('HELLO CAN YOU HEAR ME')  # => Hello can you hear me
# # => Now this is really interesting
# filter_words('now THIS                is REALLY interesting')
# # => That was extraordinary!
# filter_words('Qklgkqe  lrncqsbvmkmnh  ijfoqzsyyuamkq  ockk  eweffevw')

def reverse(st):
    return ' '.join(reversed(st.split()))


print(reverse('Hello World'))


def solution(number):
    sum = 0
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum


def summation(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum


# print(solution(10))
print(summation(8))


def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list


animals = ['dog', 'cat', 'elephant']
print(list_animals(animals))
