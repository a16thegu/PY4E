# Open the file romeo.txt and read it line by line. For each line, split the line
# into a list of words using the split() method. The program should build a list
# of words. For each word on each line check to see if the word is already in the
# list and if not append it to the list. When the program completes, sort and
# print the resulting words in alphabetical order.

# You can download the sample data at http://www.py4e.com/code3/romeo.txt
# Reference: https://www.py4e.com/html3/08-lists

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
#print(len(lst))
for line in fh:
    text = line.split()
    for word in text:
        if len(lst) is 0:
            lst.append(word)
        else:
            #print(len(lst))
            uniqueWord = True
            for lstWord in lst:
                #print(lstWord)
                if word == lstWord:
                    uniqueWord = False
                    break
                #print(word, lstWord, uniqueWord)
            if uniqueWord is True:
                lst.append(word)
            else:
                continue
lst.sort()
print(lst)
