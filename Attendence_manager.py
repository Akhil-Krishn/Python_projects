created = False
try:
    #after looping and saving attendence file, this executes
    from attendence import * #we get values in attendence(stud_dict)
    created = True

except:
    #when we execute for first time so no attendence file or names are ther so we create it
    main_dict = dict()
    def entering_names_und_nums(dic): # for creating a dict with roll nos and names
        n = int(input("Enter the number of students: "))
        for i in range(1,n+1):
            dic[i] = input("Enter name of roll number " + str(i) + ": ")

    def creat_att_save(dic): #for creating a file which stores names and roll nos we got earlier
        file = open("attendence.py","w")
        file_data = "stud_dict = " + str(dic)
        file.write(file_data)
        file.close()

    #calling the functions we defined......i guess there was no need for functions
    entering_names_und_nums(main_dict)
    creat_att_save(main_dict)
    created = False

#rember main_dict = stud_dict
# in the end we get presentence dict which contains which students are absent and which are present by roll numbers
def get_present(stud_dict): #same argumentt name as the variable name from file but ok
    #after getting stud dict with rool nos and names from attendence file
    presentence_dict = stud_dict # so that we can assign keys(here roll nos) values(true or false) depending on wheather they're present or not
    for i in stud_dict:
        while True: # so it loops till it gets correct input ie "y" or "n"
            presence = input("is " + str(stud_dict[i]) + " present? y/n : ")
            if(presence.lower() == "y"): # is present
                presentence_dict[i] = True
                break #get out of while
            elif(presence.lower() == "n"):
                presentence_dict[i] = False #not present
                break #still get out of while as we got approprite input
            else:
                print("wrong input, try again")
                #loops when user makes mistake
    return presentence_dict

#funtion for modifying files??
def mod_files(file_name,data_to_mod,data_for_value,line_number):
    file = open(file_name,"r")
    with open(file_name,"r") as file:
        data = file.readlines()

    data[line_number] = str(data_to_mod) + " = " + str(data_for_value)
  
    with open(file_name,"w") as file:
        file.writelines(data)

if(created):
    ph_x = get_present(stud_dict) #place holder?
    for i in ph_x:
        if ph_x[i] == True:
            roll_num_present[i] +=1
    
    #it just modifies the 2nd line i thnk
    mod_files("attendence.py","roll_num_present",roll_num_present,1)

elif(not created):
    ph_x = get_present(main_dict) #place holder?
    ph_keys = main_dict.keys()
    ph_value = 0
    ph_roll_num_present = dict.fromkeys(ph_keys,ph_value)#creates a dic like {1:0,2:0,3:0......etc}
    for i in ph_x:
        if ph_x[i] == True:
            ph_roll_num_present[i] +=1
    file = open("attendence.py","a")
    file_data = "\nroll_num_present = " + str(ph_roll_num_present)
    file.write(file_data)
    file.close()