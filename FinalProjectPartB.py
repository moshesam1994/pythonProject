from functools import reduce



# q9

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# Example usage
num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}")


# q10


concatenate = lambda strings: reduce(lambda x, y: x + ' ' + y, strings)

# Example usage
string_list = ["Hello", "world", "this", "is", "a", "test"]
result = concatenate(string_list)
print(result)


# q11

# The outermost lambda expression applies map to the input list lst.
# The second lambda expression inside map applies to each sublist of the input list.
# The third lambda expression inside the inner map applies to each sub-sublist of the sublist.
# The fourth lambda expression applies to each number in the sub-sublist, squaring it only if it's even.
# The sum function calculates the cumulative sum of the squared even numbers in the sub-sublist.

def cumulative_sum_of_squares_of_even(lst):
    return list(map(
        lambda sublist: list(map(
            lambda subsublist: sum(
                map(
                    lambda num: num ** 2 if num % 2 == 0 else 0,
                    subsublist
                )
            ),
            [sublist]
        )),
        lst
    ))

# Example usage
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = cumulative_sum_of_squares_of_even(list_of_lists)
print(result)



# q12
nums = [1, 2, 3, 4, 5, 6]
sum_squared = reduce(lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(sum_squared)



# q13


count_palindromes = lambda lst: list(map(lambda sublist: reduce(lambda x, y: x + (1 if y == y[::-1] else 0), sublist, 0), lst))

# Example usage:
list_of_lists = [['level', 'hlalh', 'ar'], ['python', 'madam', 'racecar']]
result = count_palindromes(list_of_lists)
print(result)  # Output: [2, 2]



