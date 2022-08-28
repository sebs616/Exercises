import random

#Find the missing number in the array
# A function that takes an unordered list of consecutive numbers with a missing value and returns the missing value.
# The missing number can be found by calculating   (the sum of values from 1 to n) - (the sum of vales in the list), where n= the biggest value in the list 
def missing_number(list):
    biggest = len(list)                             #The biggest number in the list is equals to the list length, because it is starting to count from 0.
    sum_should_be = int((biggest*(biggest+1))/2)    #calculate the sum of all consecutive numbers up to the biggest number in the list with a generic formula.
    actual_sum=0
    for item in list:                               #Calculate the sum of all the numbers in the list with a for structure, and save that sum in the variable actual_sum
        actual_sum=actual_sum + item
    return sum_should_be - actual_sum               #We return an integer equals to this difference by subtracting the theorical sum from the actual sum.




# TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST 
#create a test case, returns a list with two items; 
# [ [a shuffled range of values],  the missing value in the range]
def create_case():
    list = [*range(random.randint(3, 100))]
    removed_number = list.pop(random.randint(0, len(list)-2))
    random.shuffle(list)
    return [list, removed_number]

def validate_case(case):
    case_result = missing_number(case[0])
    if case_result == case[1]:
        return print("PASSED, value found is "+str(case_result) + " correct value is: " + str(case[1]))
    print("FAILED, value found is "+str(case_result) + " correct value is: " + str(case[1]))
    print(case[0])

#TEST THE FUNCTION 10 TIMES
validate_case(create_case())
validate_case(create_case())
validate_case(create_case())
validate_case(create_case())
validate_case(create_case())
validate_case(create_case())
validate_case(create_case())
validate_case(create_case())
validate_case(create_case())
validate_case(create_case())