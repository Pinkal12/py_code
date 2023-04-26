print("Printing the equilateral triangle pattern with characters ")  
s = 6 
# Number of rows is defined as value more than 6 shall result in printing of special characters
ASCII_value = 65  
t = (2 * s) - 2  
for i in range(0, s):  
    for j in range(0, t):  
        print(end=" ")  
# After each iteration, we are decreasing the value of t
    t = t - 1  
    for j in range(0, i + 1):  
        toprint_Alphabet = chr(ASCII_value)  
        print(toprint_Alphabet, end=' ')  
# Now, after each iteration, we increase the ASCII number  
        ASCII_value = ASCII_value + 1  
    print()  