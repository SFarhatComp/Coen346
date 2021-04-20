#Sami Farhat et Amine Bouras 

import sys
import concurrent.futures

count = 1  
count2 = 1


def main():
    sys.stdout = open("output.txt", "w")  # in order to ouput
    array = [3304, 8221, 26849, 14038, 1509, 6367, 7856, 21362] # array we created with the values given
    global count 
    with concurrent.futures.ThreadPoolExecutor() as executor:       #Executor that will help to create threads
        f1 = executor.submit(mergesort, array)  # thread calling the function
        if f1.running():    #output a message when the thread start
            print(f'thread {count2:b} started ')
        if concurrent.futures.as_completed(f1): #output a message when the thread finishes
            print(f'thread {count:b} finished: {f1.result()}\n')
    sys.stdout.close()  #closes the output file


def mergesort(array): #merge sort definition
    global count
    global count2  
    if len(array) <= 1:
        return array  #if the array has less or equal than 1 value, return the array as it is already sorted
    m = int(len(array) / 2) #find a midpoint that separates the array in 2

    with concurrent.futures.ThreadPoolExecutor() as executor: # recursive call of a function that will recursively separate the right half and the left half of the array
        r = executor.submit(mergesort, array[:m]) # right half, from the midpoint to the end
        l = executor.submit(mergesort, array[m:]) # left half, from the begingin to the midpoint

    if concurrent.futures.as_completed(r):
        count += 1
        count2 += 1                                 #thread counter for the right half
        print(f'thread {count2:b} started')   #thread counter for the right half
        print(f'thread {count:b} finished: {r.result()}')  #thread counter for the right half
    if concurrent.futures.as_completed(l): #thread counter for the LEFT half
        count2 += 1  
        count += 1
        print(f'thread {count2:b} started')
        print(f'thread {count:b} finished: {l.result()}')

    return merge(l.result(), r.result()) #returning the result and inputing it in the merge function


def merge(l, r):  # defining the sort function
    result = []
    indexl = 0
    indexr = 0

    while indexl < len(l) and indexr < len(r):    #as long as their is still a value in the array. When Index1 = len(l) it means we have reached the end of the array

        if l[indexl] < r[indexr]:
            result.append(l[indexl])
            indexl += 1          # sorting algorythm. If the present value at left is samller than the present value on the right, add it to the result array then increment the left index by 1  ex: [2,4][9,1] compare 2 to 9 , put 2 in the result and increment. Next step will compare 4 to 9
        else:
            result.append(r[indexr]) # same as previous explenation but for the right side
            indexr += 1

    result.extend(l[indexl:])
    result.extend(r[indexr:]) # if any values are left in the aray, they are appended to the result array

    return result


if __name__ == "__main__":   #call the main function 
    main()
