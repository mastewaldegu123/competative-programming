
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    array=[]
    for i in range(len(grades)):
        if grades[i] >= 38:
            if grades[i]%5 ==3:
                grades[i] +=2
                array.append(grades[i])
            elif grades[i]%5 ==4:
                grades[i] +=1
                array.append(grades[i])
            else:
                array.append(grades[i])
        else:
            array.append(grades[i])
    return array
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
