# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math 

# def print_stat():
#     grade_list = []
#     # Get the inputs from the user
#     n_student = 5
#     for _ in range(0, n_student):
#         grade_list.append(int(input('Enter a number: ')))

#     # Calculate the mean and standard deviation of the grades
#     sum_of_grades = 0 # Do you think 'sum' is a good var name? Run pylint to figure out!
#     for grade in grade_list:
#         sum_of_grades = sum_of_grades + grade
#     mean = sum / len(grade_list)
#     sd = 0 # standard deviation
#     sum_of_sqrs = 0
#     for grade in grade_list:
#         sum_of_sqrs += (grade - mean) ** 2
#     sd = math.sqrt(sum_of_sqrs / len(grade_list))
#     # print out the mean and standard deviation in a nice format.
#     print('****** Grade Statistics ******')
#     print("The grades's mean is:", mean)
#     print('The population standard deviation of grades is: ', round(sd, 3))
#     print('****** END ******')

# print_stat()

def enter_grades():
    grade_list = []
    # Get the inputs from the user
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    
    return grade_list
        
def gather_sum(grade_list):
    sum_of_grades = 0 # Do you think 'sum' is a good var name? Run pylint to figure out!
    for grade in grade_list:
        sum_of_grades = sum_of_grades + grade
    
    return sum_of_grades

def standard_deviation(grade_list):
    sum_of_grades = gather_sum(grade_list)
    
    mean = sum_of_grades / len(grade_list)
    sd = 0 # standard deviation
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))
    
    return sd
    
def print_results():
    grade_list = enter_grades()
    sum_of_grades = gather_sum(grade_list)
    sd = standard_deviation(grade_list)
    
    return f"the sum is {sum_of_grades} and the standard deviation is {sd}"
    
print(print_results())
    
    
