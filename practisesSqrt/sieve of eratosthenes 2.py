'''
Find all prime numbers less than n 
'''

def sieve(end):
    prime_list = []
    sieve_list = list(range(end+1))
    for each_number in range(2,end+1):
        if sieve_list[each_number]:
            prime_list.append(each_number)
            for every_multiple_of_the_prime in range(each_number*2, end+1, each_number):
                sieve_list[every_multiple_of_the_prime] = 0
    return prime_list

print (sieve(10))

