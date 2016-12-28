'''
@author: Xin Wen
'''
import re
from functools import reduce
sumup=0
file=open("D:\\LearningPy\\regex_sum_298911.txt","r")#open the file
print("sumup is:",reduce(lambda x,y:x+y,map(int,re.findall('[0-9]+',file.read()))))