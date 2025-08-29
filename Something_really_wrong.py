string = input("Enter string: ")
lenth = len(string)
max_lenght = 0
max_sub = ""
sub = ""
len_sub = 0
for i in range(lenth):
    if(string[i] in "aeiou" or string[i] in "AEIOU"):
        if(len_sub > max_lenght):
            max_sub = sub
            max_lenght = len_sub
            sub = ""
            len_sub = 0
    else:
        sub+=string[i]
        len_sub = len(sub)
        i += 1
print("maximum lenth consonant substring is: ", max_sub,end =" ")
print("with",max_lenght,"characters")
# akhil is a pro gamer and he is not fry cry by