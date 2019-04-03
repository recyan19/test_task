import operator
import re
from pprint import pprint

def handle_numbers(num1, num2, num3):
    """This function takes three integers and returns the count of 
    integers that are divisible by num3 in range [num1, num2]"""

    result = (1 for i in range(num1, num2+1) if i % num3 == 0)

    return sum(result)

def handle_string(value):
    """This function takes one string parameter and returns
    tuple with number of letters and digits in string"""
    digits = re.findall('\d', value)
    letters = re.findall('[a-zA-Z]', value)
    result = 'Letters - %d\nDigits - %d'
    return result % (len(letters), len(digits))

def handle_list_of_tuples(list_of_tup):
    """Function that takes list of tuples and sorts it by name / age / height / weight """
    list_of_tup.sort(key = operator.itemgetter(0, 1, 2, 3))
    return list_of_tup



if __name__ == "__main__":
    print("Task 1:")
    print(handle_numbers(1, 10, 2))
    print("Task 2")
    print(handle_string("Hello world! 123!"))
    print("Task 3")
    l = [
        ("Tom", "19", "167", "54"), 
        ("Jony", "24", "180", "69"),
        ("Json", "21", "185", "75"),
        ("John", "27", "190", "87"), 
        ("Jony", "24", "191", "98"), 
    ]
    pprint(handle_list_of_tuples(l))
