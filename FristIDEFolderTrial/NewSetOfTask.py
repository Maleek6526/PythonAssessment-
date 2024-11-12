def list_of_integers(num):
    for index in range(1, 16):
        num.append(index)
    return num


def duplicateElements(num):

    duplicates = []

    for index in range(len(num)):
        duplicates.append(num[index])
    count = 0
    for counter in range(len(duplicates)):
        duplicates.append(num[count])
        count+=1
    return duplicates

def eliminate_duplicates_values(num):
    duplicates_elimination = []
    counter = 1
    for index in range(len(num)):
        for count in range(len(num)):
            if num[count] == num[index]:
                counter+=1
                if counter == 2:
                    duplicates_elimination.append(num[index])
    print(duplicates_elimination)
    return duplicates_elimination


def addition_of_every_third_elements(num):
    addition = 0
    for count in range(0, len(num), 2):
        addition += num[count]
    return addition


elements = [1, 2, 3, 4, 5, 6, 7, 8]
addition_of_every_third_elements(elements)


def sum_of_first_middle_and_last(num):
    for index in range(len(num)):
        element = num[0]
        element_two = num[len(num) -1]
        if len(num) % 2 == 0:
                
        elif len(num) % 2 == 1:

    addition = element+element_two+third_element
    print(addition)
    return addition


numb = [1,2,3,4,5,6]

sum_of_first_middle_and_last(numb)



list = []
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list_of_integers(list)
duplicateElements(list)
eliminate_duplicates_values(numbers)