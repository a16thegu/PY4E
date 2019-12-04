# Write a program to read through the mbox-short.txt and figure out who has sent
# the greatest number of mail messages. The program looks for 'From ' lines and
# takes the second word of those lines as the person who sent the mail. The
# program creates a Python dictionary that maps the sender's mail address to a
# count of the number of times they appear in the file. After the dictionary is
# produced, the program reads through the dictionary using a maximum loop to find
# the most prolific committer.

# Reference: https://www.py4e.com/html3/09-dictionaries

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

mailDict = dict()
for line in handle:
    words = line.split()
    for word in words:
        if word == "From":
            addressIndex = line.index("From") + 1

            uniqueMail = True
            for mail in mailDict:
                if words[addressIndex] == mail:
                    uniqueMail = False
                    break

            if uniqueMail is True:
                mailDict[words[addressIndex]] = 1
            else:
                mailDict[words[addressIndex]] += 1
                continue
        else:
            continue

largest = None
mailLargestSend = ""
for mail in mailDict:
    if largest is None or mailDict[mail] > largest :
        largest = mailDict[mail]
        mailLargestSend = mail

print(mailLargestSend, largest)
