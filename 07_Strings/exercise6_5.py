# Write code using find() and string slicing (see section 6.10) to extract the
# number at the end of the line below. Convert the extracted value to a
# floating point number and print it out.

# Reference: https://www.py4e.com/html3/06-strings

text = "X-DSPAM-Confidence:    0.8475";
index = text.find("0")
str = text[index:]
num = float(str)

print(num)
