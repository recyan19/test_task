This module contains 3 functions:

1) handle_numbers(num1, num2, num3)

that takes as a parameters 3 integers.
Returns the count of integers that are divisible by num3 in range [num1, num2]
Example:
num1 = 1
num2 = 10
num3 = 2

Result: 
5, because 2, 4, 6, 8, 10 are divisible by 2

2) handle_string(value)

function that takes sentense as a parameter and returns number of letters and digits.
Example:
value = "Hello world! 123!"

Result:
Letters -  10
Digits -  3

3) handle_list_of_tuples(list_of_tup)

Function that takes list of tuples and sorts it by name / age / height / weight

Example:
list = [
    ("Tom", "19", "167", "54"), 
    ("Jony", "24", "180", "69"),
    ("Json", "21", "185", "75"), 
    ("John", "27", "190", "87"), 
    ("Jony", "24", "191", "98"), 
    ]

Result:
[
    ("John", "27", "190", "87"),
    ("Jony", "24", "180", "69"),
    ("Jony", "24", "191", "98"),
    ("Json", "21", "185", "75"),
    ("Tom", "19", "167", "54"),
]
