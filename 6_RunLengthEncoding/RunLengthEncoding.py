
# Python code for run length encoding
from collections import OrderedDict
def runLengthEncoding(input):
  
    dict = {x:0 for x in input}

    for ch in input:
        dict[ch] +=1

    output = ''
    
    for key,value in dict.items():
         output = output + key + str(value)
    
    return output
   

if __name__ == "__main__":
    input="aaabbbccc"
    print (runLengthEncoding(input))