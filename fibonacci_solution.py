num_digits = int(input("Enter the number of digits u want in the fibonacci series:  ")) #number of elements to be outputted from the fibonacci series which we want to manually eneter
fibonacci_lst = [0,1] # the first two digits of the fibonacci series and this is where we will append all digits one by one
i = 0 #a loop varibale used to represent index num zero of the fibnocci_lst
v = 1 #another loop varibale used to represent index num one of the fibnocci_lst
# now the main loop and the maths stuff go brrrr
while len(fibonacci_lst) < num_digits : #we take length of the fib list so that we get the number of digits that we entered
    sum_fibonacci_digit = fibonacci_lst[i] + fibonacci_lst[v] #we add the first two index numbers
    fibonacci_lst.append(sum_fibonacci_digit) # then we append the sum
    i += 1 #here we increase v and i by 1 so that in the next interation it will add the next two index numbers
    v += 1
# the loop runs till it appends the required num of digits in the fib series and then we simply print it out or we can make a for loop to loop around and print it out seperatley
print(fibonacci_lst)



# #factorial calculator
# imput = input("Enter a number whose factorial u want: ")
# input_num = int(imput) #recieves input
# factorial_ans = 1 #we add the factorial to it after the for loop
# do_not_execute = False
# if input_num <= 1:
#     do_not_execute = True
#     print("You should enter a number higher than 1 pls try again")
# if do_not_execute == False:
#     for i in range(2,input_num + 1): # for loop which loops until we get the answer
#         factorial_ans = factorial_ans * i  #for 1st iteration it is 1 x 2 which gives 2 and next iteration it is 2 x 3 which is six then next iteration 6 x 4 and so on..
# if do_not_execute == False:
#     print("The Factorial is: " , factorial_ans)