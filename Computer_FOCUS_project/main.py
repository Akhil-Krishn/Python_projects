import database_creator
import mysql.connector as mc
import data_cs
import data_commerce
import data_humantities
import customtkinter as ctk
import tkinter as tk
import json
import matplotlib.pyplot as plt
import anim
con = mc.connect(host = "localhost" , user = "root" , password = "password", database = database_creator.name)
cur = con.cursor()
if(database_creator.first_time == True):
    cur.execute('''create table Computer_science
    (Courses varchar(100) primary key)''')
    cur.execute('''create table Bio_maths
    (Courses varchar(100) primary key)''')
    cur.execute('''create table Commerce
    (Courses varchar(100) primary key)''')
    cur.execute('''create table Humanities
    (Courses varchar(100) primary key)''')
    cur.execute('''create table Job_opportunity
    (Name_of_job varchar(100) primary key not null,
    Salary integer not null,
    Description text)''')
    cur.execute('''create table Colleges
    (College Varchar(100) primary key not null,
    State varchar(20),
    Entrance varchar(20),
    Courses text)''')
    cur.execute('''create table Courses
    (Courses varchar(100) primary key not null,
    Job_opportunities text(10000) not null,
    Description text,
    Average_duration integer,
    Colleges text)''')
    print("created tables succesfully")
    def insert_CS(course_list):
        for i in course_list:
            cur.execute("insert into Computer_science values('{}')".format(str(i)))
    def insert_Bio(course_list):
        for i in course_list:
            cur.execute("insert into Bio_maths values('{}')".format(str(i)))
    def insert_commerce(course_list):
        for i in course_list:
            cur.execute("insert into Commerce values('{}')".format(str(i)))
    def insert_humanities(course_list):
        for i in course_list:
            cur.execute("insert into Humanities values('{}')".format(str(i)))
    def insert_Job_opps(Jobs_dict):
        for i in Jobs_dict:
            cur.execute("insert into Job_opportunity values('{job_name}',{salary},'{desc}')".format(job_name = i, salary = str(Jobs_dict[i][0]), desc = Jobs_dict[i][1]))
    def insert_colleges(college_dict):
        for i in college_dict:
            cur.execute("insert into Colleges values('{collage_name}','{state}','{entrance}','{courses}')".format(collage_name = i, state = college_dict[i][0], entrance = college_dict[i][1], courses = str(college_dict[i][2])))
    def insert_courses(course_dict):
        for i in course_dict:
            cur.execute("insert into Courses values('{course_name}','{job_opps}','{desc}',{duration},'{colleges}')".format(course_name = i, job_opps = str(course_dict[i][0]), desc = course_dict[i][1], duration = course_dict[i][2], colleges = str(course_dict[i][3])))
    insert_commerce(data_commerce.course_list_Commerce)
    insert_Job_opps(data_commerce.Jobs_dict_Commerce)
    insert_colleges(data_commerce.college_dict_Commerce)
    insert_CS(data_cs.course_list_cs)
    insert_Job_opps(data_cs.Jobs_dict_cs)
    insert_colleges(data_cs.college_dict_cs)
    insert_courses(data_cs.course_dict_cs)
    insert_courses(data_commerce.course_dict_Commerce)
    insert_humanities(data_humantities.course_list_humantities)
    insert_Job_opps(data_humantities.Jobs_dict_humantities)
    insert_colleges(data_humantities.college_dict_humantities)
    insert_courses(data_humantities.course_dict_humantitse)
    con.commit()
window = ctk.CTk()
window.geometry("1000x800")
window.title("FOCUS")
ctk.set_default_color_theme("green")
notebook = ctk.CTkTabview(window)
custom_font = ctk.CTkFont("<Times New Roman",20)
notebook._segmented_button.configure(font=custom_font)
Focus_tab = notebook.add("Focus")
Aptitude_tab = notebook.add("Aptitude Test")
Credits_tab = notebook.add("Credits")
def focus():
    def start_button_remove():
        start_button.place_forget()
        start_label.place_forget()
        def remove_buttons():
            cs_button.place_forget()
            bio_button.place_forget()
            com_button.place_forget()
            hum_button.place_forget()
            heading.place_forget()
        def cs_pressed():
            remove_buttons()
            def remove_buttons_cs():
                canvas_cs_press.pack_forget()
                scrollbar_cs_press.place_forget()
            def job_pressed(text):
                remove_buttons_cs()
                def remove_buttons_job():
                    job_slary_title.place_forget()
                    job_slary_content.place_forget()
                    job_desc_content.place_forget()
                    job_title.place_forget()
                    job_desc_content.place_forget()
                    check_courses_button.place_forget()
                def check_courses_pressed():
                    remove_buttons_job()
                    def remove_buttons_checkcourse():
                        canvas_cous_press.pack_forget()
                        scrollbar_cous_press.place_forget()
                    def course_pressed(name_course):
                        remove_buttons_checkcourse()
                        def remove_buttons_course_detail():
                            canvas_cous_detail.pack_forget()
                            scrollbar_cous_detail.place_forget()
                        def collage_pressed(name_collage):
                            remove_buttons_course_detail()
                            def home_pressed():
                                collage_title.place_forget()
                                collage_entrance_title.place_forget()
                                collage_location_title.place_forget()
                                collage_course_list_title.place_forget()
                                collage_course_list_stuff.place_forget()
                                back_button.place_forget()
                                focus()
                            cur.execute("Select * from Colleges")
                            collage_data_list = cur.fetchall()
                            for i in collage_data_list:
                                if(i[0] == name_collage):
                                    collage_data_act = list(i)
                            collage_state = collage_data_act[1]
                            collage_entrance = collage_data_act[2]
                            collage_course_list = json.loads(collage_data_act[3])
                            collage_course_list_content = ""
                            for i in collage_course_list:
                                collage_course_list_content = collage_course_list_content + i +", "
                            collage_course_list_content_act = ''
                            line_var = 0
                            for j in range(len(collage_course_list_content)-2):
                                line_var +=1
                                if( line_var > 70 and collage_course_list_content[j] == " "):
                                    collage_course_list_content_act += '\n'
                                    line_var = 0
                                collage_course_list_content_act += collage_course_list_content[j]
                            collage_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text=name_collage+" Details:",font = ("<Times New Roman",30))
                            collage_entrance_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="Entrance exam: "+collage_entrance,font = ("<Times New Roman",25))
                            collage_location_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="College location: "+collage_state,font = ("<Times New Roman",25))
                            collage_course_list_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="Other available courses:",font = ("<Times New Roman",25))
                            collage_course_list_stuff = ctk.CTkLabel(Focus_tab,corner_radius=10,text=collage_course_list_content_act,font = ("<Times New Roman",20))
                            back_button = ctk.CTkButton(Focus_tab,corner_radius=10,text="Home",font = ("<Times New Roman",25),command=home_pressed)
                            collage_title.place(relx = 0.5, rely= 0.1, relwidth = 1,anchor = 'center')
                            collage_entrance_title.place(relx = 0.5, rely = 0.3, relwidth = 0.9,anchor = 'center')
                            collage_location_title.place(relx = 0.5, rely = 0.45, relwidth = 0.9,anchor = 'center')
                            collage_course_list_title.place(relx = 0.5, rely = 0.6, relwidth = 0.9,anchor = 'center')
                            collage_course_list_stuff.place(relx = 0.5, rely = 0.69,relwidth = 0.9,anchor='center')
                            back_button.place(relx=0.5,rely = 0.9,relwidth=0.3,anchor="center")
                        class collage_boottuns:
                            def __init__(self,txt):
                                self.txt = txt
                                self.collage_button_act = ctk.CTkButton(Focus_tab,corner_radius=10,text=self.txt, font = ("<Times New Roman",20),width=70,height=50,command=lambda:collage_pressed(self.txt))
                        for i in courses_full_data_lst:
                            if i[0] == name_course:
                                course_desc = ''
                                line_var = 0
                                for j in range(len(str(i[2]))):
                                    line_var += 1
                                    if( line_var > 70 and str(i[2])[j] == " " ):
                                        course_desc += '\n'
                                        line_var = 0
                                    course_desc += str(i[2])[j]
                                course_duration = int(i[3])
                                course_collage_list = json.loads(i[4])
                        canvas_cous_detail = tk.Canvas(Focus_tab,scrollregion=(0,0,2000,5000),bg="#2a2b2a")
                        canvas_cous_detail.create_rectangle(0,0,canvas_cous_detail.winfo_width(),canvas_cous_detail.winfo_height(),fill='#2a2b2a')
                        canvas_cous_detail.pack(fill='both',expand=True)
                        scrollbar_cous_detail = tk.Scrollbar(Focus_tab,orient='vertical',command=canvas_cous_detail.yview,bg="#2a2b2a")
                        scrollbar_cous_detail.place(relx=1,rely=0,relheight=1,anchor='ne')
                        canvas_cous_detail.configure(yscrollcommand= scrollbar_cous_detail.set)
                        course_name_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text=name_course+":",font = ("<Times New Roman",30))
                        course_desc_content = ctk.CTkLabel(Focus_tab,corner_radius=10,text=course_desc,font = ("<Times New Roman",20))
                        course_duration_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="Duration of "+name_course+": "+str(course_duration)+" years",font = ("<Times New Roman",25))
                        collage_list_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="Suitable Collages:",font = ("<Times New Roman",30))
                        canvas_cous_detail.create_window((550,100),window=course_name_title)
                        canvas_cous_detail.create_window((550,200),window=course_desc_content)
                        canvas_cous_detail.create_window((550,300),window=course_duration_title)
                        canvas_cous_detail.create_window((550,400),window=collage_list_title)
                        x=550
                        y=500
                        for i in course_collage_list:
                            collage_button = collage_boottuns(str(i))
                            canvas_cous_detail.create_window((x,y),window=collage_button.collage_button_act)
                            y+=150
                    class course_boottuns:
                        def __init__(self,txt):
                            self.txt = txt
                            self.course_button_act = ctk.CTkButton(Focus_tab,corner_radius=10,text=self.txt, font = ("<Times New Roman",25),width=100,height=50,command=lambda:course_pressed(self.txt))
                    canvas_cous_press = tk.Canvas(Focus_tab,scrollregion=(0,0,2000,5000),bg="#2a2b2a")
                    canvas_cous_press.create_rectangle(0,0,canvas_cous_press.winfo_width(),canvas_cous_press.winfo_height(),fill='#2a2b2a')
                    canvas_cous_press.pack(fill='both',expand=True)
                    scrollbar_cous_press = tk.Scrollbar(Focus_tab,orient='vertical',command=canvas_cous_press.yview,bg="#2a2b2a")
                    scrollbar_cous_press.place(relx=1,rely=0,relheight=1,anchor='ne')
                    canvas_cous_press.configure(yscrollcommand= scrollbar_cous_press.set)
                    course_title = ctk.CTkLabel(Focus_tab,text = "The courses most suitable\nfor "+name_job+" are:",font = ("<Times New Roman",30),corner_radius=10)
                    canvas_cous_press.create_window((550,100),window=course_title)
                    cur.execute("Select * from Courses")
                    data_job_press = cur.fetchall()
                    courses_full_data_lst = []
                    for i in data_job_press:
                        if name_job in json.loads(i[1]):
                            courses_full_data_lst.append(i)
                    x=550
                    y=250
                    for i in courses_full_data_lst:
                        j = i[0]
                        course_button = course_boottuns(str(j))
                        canvas_cous_press.create_window((x,y),window=course_button.course_button_act)
                        y+=150
                cur.execute("select * from Job_opportunity")
                jobs_data = cur.fetchall()
                for i in jobs_data:
                    if(i[0] == text):
                        name_job = i[0]
                        avg_salary = i[1]
                        job_desc = ''
                        line_var = 0
                        for j in range(len(i[2])):
                            line_var += 1
                            if(line_var > 70 and i[2][j] == " "):
                                job_desc += '\n'
                                line_var = 0
                            job_desc += i[2][j]

                job_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text=name_job+":",font = ("<Times New Roman",30))
                job_slary_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="Average Salary:",font = ("<Times New Roman",30))
                job_slary_content = ctk.CTkLabel(Focus_tab,corner_radius=10,text=str(avg_salary),font = ("<Times New Roman",25))
                job_desc_content = ctk.CTkLabel(Focus_tab,corner_radius=10,text=job_desc,font = ("<Times New Roman",25))
                check_courses_button = ctk.CTkButton(Focus_tab,corner_radius=10,text="Check related courses",font = ("<Times New Roman",30),command = check_courses_pressed)
                job_title.place(relx = 0.0, rely= 0.1, relwidth = 0.5,anchor = 'w')
                job_desc_content.place(relx = 0.0, rely = 0.25, relwidth = 1,anchor = 'w')
                job_slary_title.place(relx = 0.0, rely = 0.5, relwidth = 0.5,anchor = 'w')
                job_slary_content.place(relx = 0.0, rely = 0.6, relwidth = 0.5,anchor = 'w')
                check_courses_button.place(relx = 0.5, rely = 0.85,relwidth = 0.6,anchor='center')
            class job_boottuns:
                def __init__(self,txt):
                    self.txt = txt
                    self.job_button_act = ctk.CTkButton(Focus_tab,corner_radius=10,text=self.txt, font = ("<Times New Roman",20),width=100,height=50,command=lambda:job_pressed(self.txt))
            canvas_cs_press = tk.Canvas(Focus_tab,scrollregion=(0,0,2000,5000),bg="#2a2b2a")
            canvas_cs_press.create_rectangle(0,0,canvas_cs_press.winfo_width(),canvas_cs_press.winfo_height(),fill='#2a2b2a')
            canvas_cs_press.pack(fill='both',expand=True)
            scrollbar_cs_press = tk.Scrollbar(Focus_tab,orient='vertical',command=canvas_cs_press.yview,bg="#2a2b2a")
            scrollbar_cs_press.place(relx=1,rely=0,relheight=1,anchor='ne')
            canvas_cs_press.configure(yscrollcommand= scrollbar_cs_press.set)
            heading_cs_press = ctk.CTkLabel(Focus_tab,corner_radius=10,text="These are the best possible\njobs after Computer science",font = ("<Times New Roman",30))
            canvas_cs_press.create_window((550,100),window=heading_cs_press)
            cur.execute("select * from Computer_science")
            course_list_cs_raw = cur.fetchall()
            course_list_cs = []
            for i in course_list_cs_raw:
                course_list_cs.append(i[0])
            cur.execute("select * from Courses")
            course_list_data = cur.fetchall()
            jobs_list_cs_raw = []
            jobs_list_cs = []
            for i in course_list_data:
                if(i[0] in course_list_cs):
                    jobs_list_cs_raw.append(i[1])
            for i in jobs_list_cs_raw:
                jobs_list_cs.extend(json.loads(i))
            x=550
            y=250
            for i in jobs_list_cs:
                job_button = job_boottuns(str(i))
                canvas_cs_press.create_window((x,y),window=job_button.job_button_act)
                y+=150
        def bio_pressed():
            remove_buttons()
            def remove_buttons_cs():
                canvas_cs_press.pack_forget()
                scrollbar_cs_press.place_forget()
            def job_pressed(text):
                remove_buttons_cs()
                def remove_buttons_job():
                    job_slary_title.place_forget()
                    job_slary_content.place_forget()
                    job_desc_content.place_forget()
                    job_title.place_forget()
                    job_desc_content.place_forget()
                    check_courses_button.place_forget()
                def check_courses_pressed():
                    remove_buttons_job()
                    def remove_buttons_checkcourse():
                        canvas_cous_press.pack_forget()
                        scrollbar_cous_press.place_forget()
                    def course_pressed(name_course):
                        remove_buttons_checkcourse()
                        def remove_buttons_course_detail():
                            canvas_cous_detail.pack_forget()
                            scrollbar_cous_detail.place_forget()
                        def collage_pressed(name_collage):
                            remove_buttons_course_detail()
                            def home_pressed():
                                collage_title.place_forget()
                                collage_entrance_title.place_forget()
                                collage_location_title.place_forget()
                                collage_course_list_title.place_forget()
                                collage_course_list_stuff.place_forget()
                                back_button.place_forget()
                                focus()
                            cur.execute("Select * from Colleges")
                            collage_data_list = cur.fetchall()
                            for i in collage_data_list:
                                if(i[0] == name_collage):
                                    collage_data_act = list(i)
                            collage_state = collage_data_act[1]
                            collage_entrance = collage_data_act[2]
                            collage_course_list = json.loads(collage_data_act[3])
                            collage_course_list_content = ""
                            for i in collage_course_list:
                                collage_course_list_content = collage_course_list_content + i +", "
                            collage_course_list_content_act = ''
                            line_var = 0
                            for j in range(len(collage_course_list_content)-2):
                                line_var +=1
                                if( line_var > 70 and collage_course_list_content[j] == " "):
                                    collage_course_list_content_act += '\n'
                                    line_var = 0
                                collage_course_list_content_act += collage_course_list_content[j]
                            collage_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text=name_collage+" Details:",font = ("<Times New Roman",30))
                            collage_entrance_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="Entrance exam: "+collage_entrance,font = ("<Times New Roman",25))
                            collage_location_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="College location: "+collage_state,font = ("<Times New Roman",25))
                            collage_course_list_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="Other available courses:",font = ("<Times New Roman",25))
                            collage_course_list_stuff = ctk.CTkLabel(Focus_tab,corner_radius=10,text=collage_course_list_content_act,font = ("<Times New Roman",20))
                            back_button = ctk.CTkButton(Focus_tab,corner_radius=10,text="Home",font = ("<Times New Roman",25),command=home_pressed)
                            collage_title.place(relx = 0.5, rely= 0.1, relwidth = 1,anchor = 'center')
                            collage_entrance_title.place(relx = 0.5, rely = 0.3, relwidth = 0.9,anchor = 'center')
                            collage_location_title.place(relx = 0.5, rely = 0.45, relwidth = 0.9,anchor = 'center')
                            collage_course_list_title.place(relx = 0.5, rely = 0.6, relwidth = 0.9,anchor = 'center')
                            collage_course_list_stuff.place(relx = 0.5, rely = 0.69,relwidth = 0.9,anchor='center')
                            back_button.place(relx=0.5,rely = 0.9,relwidth=0.3,anchor="center")
                        class collage_boottuns:
                            def __init__(self,txt):
                                self.txt = txt
                                self.collage_button_act = ctk.CTkButton(Focus_tab,corner_radius=10,text=self.txt, font = ("<Times New Roman",20),width=70,height=50,command=lambda:collage_pressed(self.txt))
                        for i in courses_full_data_lst:
                            if i[0] == name_course:
                                course_desc = ''
                                line_var = 0
                                for j in range(len(str(i[2]))):
                                    line_var += 1
                                    if( line_var > 70 and str(i[2])[j] == " " ):
                                        course_desc += '\n'
                                        line_var = 0
                                    course_desc += str(i[2])[j]
                                course_duration = int(i[3])
                                course_collage_list = json.loads(i[4])
                        canvas_cous_detail = tk.Canvas(Focus_tab,scrollregion=(0,0,2000,5000),bg="#2a2b2a")
                        canvas_cous_detail.create_rectangle(0,0,canvas_cous_detail.winfo_width(),canvas_cous_detail.winfo_height(),fill='#2a2b2a')
                        canvas_cous_detail.pack(fill='both',expand=True)
                        scrollbar_cous_detail = tk.Scrollbar(Focus_tab,orient='vertical',command=canvas_cous_detail.yview,bg="#2a2b2a")
                        scrollbar_cous_detail.place(relx=1,rely=0,relheight=1,anchor='ne')
                        canvas_cous_detail.configure(yscrollcommand= scrollbar_cous_detail.set)
                        course_name_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text=name_course+":",font = ("<Times New Roman",30))
                        course_desc_content = ctk.CTkLabel(Focus_tab,corner_radius=10,text=course_desc,font = ("<Times New Roman",20))
                        course_duration_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="Duration of "+name_course+": "+str(course_duration)+" years",font = ("<Times New Roman",25))
                        collage_list_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="Suitable Collages:",font = ("<Times New Roman",30))
                        canvas_cous_detail.create_window((550,100),window=course_name_title)
                        canvas_cous_detail.create_window((550,200),window=course_desc_content)
                        canvas_cous_detail.create_window((550,300),window=course_duration_title)
                        canvas_cous_detail.create_window((550,400),window=collage_list_title)
                        x=550
                        y=500
                        for i in course_collage_list:
                            collage_button = collage_boottuns(str(i))
                            canvas_cous_detail.create_window((x,y),window=collage_button.collage_button_act)
                            y+=150
                    class course_boottuns:
                        def __init__(self,txt):
                            self.txt = txt
                            self.course_button_act = ctk.CTkButton(Focus_tab,corner_radius=10,text=self.txt, font = ("<Times New Roman",25),width=100,height=50,command=lambda:course_pressed(self.txt))
                    canvas_cous_press = tk.Canvas(Focus_tab,scrollregion=(0,0,2000,5000),bg="#2a2b2a")
                    canvas_cous_press.create_rectangle(0,0,canvas_cous_press.winfo_width(),canvas_cous_press.winfo_height(),fill='#2a2b2a')
                    canvas_cous_press.pack(fill='both',expand=True)
                    scrollbar_cous_press = tk.Scrollbar(Focus_tab,orient='vertical',command=canvas_cous_press.yview,bg="#2a2b2a")
                    scrollbar_cous_press.place(relx=1,rely=0,relheight=1,anchor='ne')
                    canvas_cous_press.configure(yscrollcommand= scrollbar_cous_press.set)
                    course_title = ctk.CTkLabel(Focus_tab,text = "The courses most suitable\nfor "+name_job+" are:",font = ("<Times New Roman",30),corner_radius=10)
                    canvas_cous_press.create_window((550,100),window=course_title)
                    cur.execute("Select * from Courses")
                    data_job_press = cur.fetchall()
                    courses_full_data_lst = []
                    for i in data_job_press:
                        if name_job in json.loads(i[1]):
                            courses_full_data_lst.append(i)
                    x=550
                    y=250
                    for i in courses_full_data_lst:
                        j = i[0]
                        course_button = course_boottuns(str(j))
                        canvas_cous_press.create_window((x,y),window=course_button.course_button_act)
                        y+=150
                cur.execute("select * from Job_opportunity")
                jobs_data = cur.fetchall()
                for i in jobs_data:
                    if(i[0] == text):
                        name_job = i[0]
                        avg_salary = i[1]
                        job_desc = ''
                        line_var = 0
                        for j in range(len(i[2])):
                            line_var += 1
                            if(line_var > 70 and i[2][j] == " "):
                                job_desc += '\n'
                                line_var = 0
                            job_desc += i[2][j]
                job_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text=name_job+":",font = ("<Times New Roman",30))
                job_slary_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="Average Salary:",font = ("<Times New Roman",30))
                job_slary_content = ctk.CTkLabel(Focus_tab,corner_radius=10,text=str(avg_salary),font = ("<Times New Roman",25))
                job_desc_content = ctk.CTkLabel(Focus_tab,corner_radius=10,text=job_desc,font = ("<Times New Roman",25))
                check_courses_button = ctk.CTkButton(Focus_tab,corner_radius=10,text="Check related courses",font = ("<Times New Roman",30),command = check_courses_pressed)
                job_title.place(relx = 0.0, rely= 0.1, relwidth = 0.5,anchor = 'w')
                job_desc_content.place(relx = 0.0, rely = 0.25, relwidth = 1,anchor = 'w')
                job_slary_title.place(relx = 0.0, rely = 0.5, relwidth = 0.5,anchor = 'w')
                job_slary_content.place(relx = 0.0, rely = 0.6, relwidth = 0.5,anchor = 'w')
                check_courses_button.place(relx = 0.5, rely = 0.85,relwidth = 0.6,anchor='center')
            class job_boottuns:
                def __init__(self,txt):
                    self.txt = txt
                    self.job_button_act = ctk.CTkButton(Focus_tab,corner_radius=10,text=self.txt, font = ("<Times New Roman",20),width=100,height=50,command=lambda:job_pressed(self.txt))
            canvas_cs_press = tk.Canvas(Focus_tab,scrollregion=(0,0,2000,5000),bg="#2a2b2a")
            canvas_cs_press.create_rectangle(0,0,canvas_cs_press.winfo_width(),canvas_cs_press.winfo_height(),fill='#2a2b2a')
            canvas_cs_press.pack(fill='both',expand=True)
            scrollbar_cs_press = tk.Scrollbar(Focus_tab,orient='vertical',command=canvas_cs_press.yview,bg="#2a2b2a")
            scrollbar_cs_press.place(relx=1,rely=0,relheight=1,anchor='ne')
            canvas_cs_press.configure(yscrollcommand= scrollbar_cs_press.set)
            heading_cs_press = ctk.CTkLabel(Focus_tab,corner_radius=10,text="These are the best possible\njobs after Bio Maths",font = ("<Times New Roman",30))
            canvas_cs_press.create_window((550,100),window=heading_cs_press)
            cur.execute("select * from Computer_science")
            course_list_cs_raw = cur.fetchall()
            course_list_cs = []
            for i in course_list_cs_raw:
                course_list_cs.append(i[0])
            cur.execute("select * from Courses")
            course_list_data = cur.fetchall()
            jobs_list_cs_raw = []
            jobs_list_cs = []
            for i in course_list_data:
                if(i[0] in course_list_cs):
                    jobs_list_cs_raw.append(i[1])
            for i in jobs_list_cs_raw:
                jobs_list_cs.extend(json.loads(i))
            x=550
            y=250
            for i in jobs_list_cs:
                job_button = job_boottuns(str(i))
                canvas_cs_press.create_window((x,y),window=job_button.job_button_act)
                y+=150
        def com_pressed():
            remove_buttons()
            def remove_buttons_cs():
                canvas_cs_press.pack_forget()
                scrollbar_cs_press.place_forget()
            def job_pressed(text):
                remove_buttons_cs()
                def remove_buttons_job():
                    job_slary_title.place_forget()
                    job_slary_content.place_forget()
                    job_desc_content.place_forget()
                    job_title.place_forget()
                    job_desc_content.place_forget()
                    check_courses_button.place_forget()
                def check_courses_pressed():
                    remove_buttons_job()
                    def remove_buttons_checkcourse():
                        canvas_cous_press.pack_forget()
                        scrollbar_cous_press.place_forget()
                    def course_pressed(name_course):
                        remove_buttons_checkcourse()
                        def remove_buttons_course_detail():
                            canvas_cous_detail.pack_forget()
                            scrollbar_cous_detail.place_forget()
                        def collage_pressed(name_collage):
                            remove_buttons_course_detail()
                            def home_pressed():
                                collage_title.place_forget()
                                collage_entrance_title.place_forget()
                                collage_location_title.place_forget()
                                collage_course_list_title.place_forget()
                                collage_course_list_stuff.place_forget()
                                back_button.place_forget()
                                focus()
                            cur.execute("Select * from Colleges")
                            collage_data_list = cur.fetchall()
                            for i in collage_data_list:
                                if(i[0] == name_collage):
                                    collage_data_act = list(i)
                            collage_state = collage_data_act[1]
                            collage_entrance = collage_data_act[2]
                            collage_course_list = json.loads(collage_data_act[3])
                            collage_course_list_content = ""
                            for i in collage_course_list:
                                collage_course_list_content = collage_course_list_content + i +", "
                            collage_course_list_content_act = ''
                            line_var = 0
                            for j in range(len(collage_course_list_content)-2):
                                line_var +=1
                                if( line_var > 70 and collage_course_list_content[j] == " "):
                                    collage_course_list_content_act += '\n'
                                    line_var = 0
                                collage_course_list_content_act += collage_course_list_content[j]
                            collage_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text=name_collage+" Details:",font = ("<Times New Roman",30))
                            collage_entrance_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="Entrance exam: "+collage_entrance,font = ("<Times New Roman",25))
                            collage_location_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="College location: "+collage_state,font = ("<Times New Roman",25))
                            collage_course_list_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="Other available courses:",font = ("<Times New Roman",25))
                            collage_course_list_stuff = ctk.CTkLabel(Focus_tab,corner_radius=10,text=collage_course_list_content_act,font = ("<Times New Roman",20))
                            back_button = ctk.CTkButton(Focus_tab,corner_radius=10,text="Home",font = ("<Times New Roman",25),command=home_pressed)
                            collage_title.place(relx = 0.5, rely= 0.1, relwidth = 1,anchor = 'center')
                            collage_entrance_title.place(relx = 0.5, rely = 0.3, relwidth = 0.9,anchor = 'center')
                            collage_location_title.place(relx = 0.5, rely = 0.45, relwidth = 0.9,anchor = 'center')
                            collage_course_list_title.place(relx = 0.5, rely = 0.6, relwidth = 0.9,anchor = 'center')
                            collage_course_list_stuff.place(relx = 0.5, rely = 0.69,relwidth = 0.9,anchor='center')
                            back_button.place(relx=0.5,rely = 0.9,relwidth=0.3,anchor="center")
                        class collage_boottuns:
                            def __init__(self,txt):
                                self.txt = txt
                                self.collage_button_act = ctk.CTkButton(Focus_tab,corner_radius=10,text=self.txt, font = ("<Times New Roman",20),width=70,height=50,command=lambda:collage_pressed(self.txt))
                        for i in courses_full_data_lst:
                            if i[0] == name_course:
                                course_desc = ''
                                line_var = 0
                                for j in range(len(str(i[2]))):
                                    line_var += 1
                                    if( line_var > 70 and str(i[2])[j] == " " ):
                                        course_desc += '\n'
                                        line_var = 0
                                    course_desc += str(i[2])[j]
                                course_duration = int(i[3])
                                course_collage_list = json.loads(i[4])
                        canvas_cous_detail = tk.Canvas(Focus_tab,scrollregion=(0,0,2000,5000),bg="#2a2b2a")
                        canvas_cous_detail.create_rectangle(0,0,canvas_cous_detail.winfo_width(),canvas_cous_detail.winfo_height(),fill='#2a2b2a')
                        canvas_cous_detail.pack(fill='both',expand=True)
                        scrollbar_cous_detail = tk.Scrollbar(Focus_tab,orient='vertical',command=canvas_cous_detail.yview,bg="#2a2b2a")
                        scrollbar_cous_detail.place(relx=1,rely=0,relheight=1,anchor='ne')
                        canvas_cous_detail.configure(yscrollcommand= scrollbar_cous_detail.set)
                        course_name_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text=name_course+":",font = ("<Times New Roman",30))
                        course_desc_content = ctk.CTkLabel(Focus_tab,corner_radius=10,text=course_desc,font = ("<Times New Roman",20))
                        course_duration_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="Duration of "+name_course+": "+str(course_duration)+" years",font = ("<Times New Roman",25))
                        collage_list_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="Suitable Collages:",font = ("<Times New Roman",30))
                        canvas_cous_detail.create_window((550,100),window=course_name_title)
                        canvas_cous_detail.create_window((550,200),window=course_desc_content)
                        canvas_cous_detail.create_window((550,300),window=course_duration_title)
                        canvas_cous_detail.create_window((550,400),window=collage_list_title)
                        x=550
                        y=500
                        for i in course_collage_list:
                            collage_button = collage_boottuns(str(i))
                            canvas_cous_detail.create_window((x,y),window=collage_button.collage_button_act)
                            y+=150
                    class course_boottuns:
                        def __init__(self,txt):
                            self.txt = txt
                            self.course_button_act = ctk.CTkButton(Focus_tab,corner_radius=10,text=self.txt, font = ("<Times New Roman",25),width=100,height=50,command=lambda:course_pressed(self.txt))
                    canvas_cous_press = tk.Canvas(Focus_tab,scrollregion=(0,0,2000,5000),bg="#2a2b2a")
                    canvas_cous_press.create_rectangle(0,0,canvas_cous_press.winfo_width(),canvas_cous_press.winfo_height(),fill='#2a2b2a')
                    canvas_cous_press.pack(fill='both',expand=True)
                    scrollbar_cous_press = tk.Scrollbar(Focus_tab,orient='vertical',command=canvas_cous_press.yview,bg="#2a2b2a")
                    scrollbar_cous_press.place(relx=1,rely=0,relheight=1,anchor='ne')
                    canvas_cous_press.configure(yscrollcommand= scrollbar_cous_press.set)
                    course_title = ctk.CTkLabel(Focus_tab,text = "The courses most suitable\nfor "+name_job+" are:",font = ("<Times New Roman",30),corner_radius=10)
                    canvas_cous_press.create_window((550,100),window=course_title)
                    cur.execute("Select * from Courses")
                    data_job_press = cur.fetchall()
                    courses_full_data_lst = []
                    for i in data_job_press:
                        if name_job in json.loads(i[1]):
                            courses_full_data_lst.append(i)
                    x=550
                    y=250
                    for i in courses_full_data_lst:
                        j = i[0]
                        course_button = course_boottuns(str(j))
                        canvas_cous_press.create_window((x,y),window=course_button.course_button_act)
                        y+=150
                cur.execute("select * from Job_opportunity")
                jobs_data = cur.fetchall()
                for i in jobs_data:
                    if(i[0] == text):
                        name_job = i[0]
                        avg_salary = i[1]
                        job_desc = ''
                        line_var = 0
                        for j in range(len(i[2])):
                            line_var += 1
                            if(line_var > 70 and i[2][j] == " "):
                                job_desc += '\n'
                                line_var = 0
                            job_desc += i[2][j]
                job_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text=name_job+":",font = ("<Times New Roman",30))
                job_slary_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="Average Salary:",font = ("<Times New Roman",30))
                job_slary_content = ctk.CTkLabel(Focus_tab,corner_radius=10,text=str(avg_salary),font = ("<Times New Roman",25))
                job_desc_content = ctk.CTkLabel(Focus_tab,corner_radius=10,text=job_desc,font = ("<Times New Roman",25))
                check_courses_button = ctk.CTkButton(Focus_tab,corner_radius=10,text="Check related courses",font = ("<Times New Roman",30),command = check_courses_pressed)
                job_title.place(relx = 0.0, rely= 0.1, relwidth = 0.5,anchor = 'w')
                job_desc_content.place(relx = 0.0, rely = 0.25, relwidth = 1,anchor = 'w')
                job_slary_title.place(relx = 0.0, rely = 0.5, relwidth = 0.5,anchor = 'w')
                job_slary_content.place(relx = 0.0, rely = 0.6, relwidth = 0.5,anchor = 'w')
                check_courses_button.place(relx = 0.5, rely = 0.85,relwidth = 0.6,anchor='center')
            class job_boottuns:
                def __init__(self,txt):
                    self.txt = txt
                    self.job_button_act = ctk.CTkButton(Focus_tab,corner_radius=10,text=self.txt, font = ("<Times New Roman",20),width=100,height=50,command=lambda:job_pressed(self.txt))
            canvas_cs_press = tk.Canvas(Focus_tab,scrollregion=(0,0,2000,5000),bg="#2a2b2a")
            canvas_cs_press.create_rectangle(0,0,canvas_cs_press.winfo_width(),canvas_cs_press.winfo_height(),fill='#2a2b2a')
            canvas_cs_press.pack(fill='both',expand=True)
            scrollbar_cs_press = tk.Scrollbar(Focus_tab,orient='vertical',command=canvas_cs_press.yview,bg="#2a2b2a")
            scrollbar_cs_press.place(relx=1,rely=0,relheight=1,anchor='ne')
            canvas_cs_press.configure(yscrollcommand= scrollbar_cs_press.set)
            heading_cs_press = ctk.CTkLabel(Focus_tab,corner_radius=10,text="These are the best possible\njobs after Commerce",font = ("<Times New Roman",30))
            canvas_cs_press.create_window((550,100),window=heading_cs_press)
            cur.execute("select * from Commerce")
            course_list_cs_raw = cur.fetchall()
            course_list_cs = []
            for i in course_list_cs_raw:
                course_list_cs.append(i[0])
            cur.execute("select * from Courses")
            course_list_data = cur.fetchall()
            jobs_list_cs_raw = []
            jobs_list_cs = []
            for i in course_list_data:
                if(i[0] in course_list_cs):
                    jobs_list_cs_raw.append(i[1])
            for i in jobs_list_cs_raw:
                jobs_list_cs.extend(json.loads(i))
            x=550
            y=250
            for i in jobs_list_cs:
                job_button = job_boottuns(str(i))
                canvas_cs_press.create_window((x,y),window=job_button.job_button_act)
                y+=150
        def hum_pressed():
            remove_buttons()
            def remove_buttons_cs():
                canvas_cs_press.pack_forget()
                scrollbar_cs_press.place_forget()
            def job_pressed(text):
                remove_buttons_cs()
                def remove_buttons_job():
                    job_slary_title.place_forget()
                    job_slary_content.place_forget()
                    job_desc_content.place_forget()
                    job_title.place_forget()
                    job_desc_content.place_forget()
                    check_courses_button.place_forget()
                def check_courses_pressed():
                    remove_buttons_job()
                    def remove_buttons_checkcourse():
                        canvas_cous_press.pack_forget()
                        scrollbar_cous_press.place_forget()
                    def course_pressed(name_course):
                        remove_buttons_checkcourse()
                        def remove_buttons_course_detail():
                            canvas_cous_detail.pack_forget()
                            scrollbar_cous_detail.place_forget()
                        def collage_pressed(name_collage):
                            remove_buttons_course_detail()
                            def home_pressed():
                                collage_title.place_forget()
                                collage_entrance_title.place_forget()
                                collage_location_title.place_forget()
                                collage_course_list_title.place_forget()
                                collage_course_list_stuff.place_forget()
                                back_button.place_forget()
                                focus()
                            cur.execute("Select * from Colleges")
                            collage_data_list = cur.fetchall()
                            for i in collage_data_list:
                                if(i[0] == name_collage):
                                    collage_data_act = list(i)
                            collage_state = collage_data_act[1]
                            collage_entrance = collage_data_act[2]
                            collage_course_list = json.loads(collage_data_act[3])
                            collage_course_list_content = ""
                            for i in collage_course_list:
                                collage_course_list_content = collage_course_list_content + i +", "
                            collage_course_list_content_act = ''
                            line_var = 0
                            for j in range(len(collage_course_list_content)-2):
                                line_var +=1
                                if( line_var > 70 and collage_course_list_content[j] == " "):
                                    collage_course_list_content_act += '\n'
                                    line_var = 0
                                collage_course_list_content_act += collage_course_list_content[j]
                            collage_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text=name_collage+" Details:",font = ("<Times New Roman",30))
                            collage_entrance_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="Entrance exam: "+collage_entrance,font = ("<Times New Roman",25))
                            collage_location_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="College location: "+collage_state,font = ("<Times New Roman",25))
                            collage_course_list_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="Other available courses:",font = ("<Times New Roman",25))
                            collage_course_list_stuff = ctk.CTkLabel(Focus_tab,corner_radius=10,text=collage_course_list_content_act,font = ("<Times New Roman",20))
                            back_button = ctk.CTkButton(Focus_tab,corner_radius=10,text="Home",font = ("<Times New Roman",25),command=home_pressed)
                            collage_title.place(relx = 0.5, rely= 0.1, relwidth = 1,anchor = 'center')
                            collage_entrance_title.place(relx = 0.5, rely = 0.3, relwidth = 0.9,anchor = 'center')
                            collage_location_title.place(relx = 0.5, rely = 0.45, relwidth = 0.9,anchor = 'center')
                            collage_course_list_title.place(relx = 0.5, rely = 0.6, relwidth = 0.9,anchor = 'center')
                            collage_course_list_stuff.place(relx = 0.5, rely = 0.69,relwidth = 0.9,anchor='center')
                            back_button.place(relx=0.5,rely = 0.9,relwidth=0.3,anchor="center")
                        class collage_boottuns:
                            def __init__(self,txt):
                                self.txt = txt
                                self.collage_button_act = ctk.CTkButton(Focus_tab,corner_radius=10,text=self.txt, font = ("<Times New Roman",20),width=70,height=50,command=lambda:collage_pressed(self.txt))
                        for i in courses_full_data_lst:
                            if i[0] == name_course:
                                course_desc = ''
                                line_var = 0
                                for j in range(len(str(i[2]))):
                                    line_var += 1
                                    if( line_var > 70 and str(i[2])[j] == " " ):
                                        course_desc += '\n'
                                        line_var = 0
                                    course_desc += str(i[2])[j]
                                course_duration = int(i[3])
                                course_collage_list = json.loads(i[4])
                        canvas_cous_detail = tk.Canvas(Focus_tab,scrollregion=(0,0,2000,5000),bg="#2a2b2a")
                        canvas_cous_detail.create_rectangle(0,0,canvas_cous_detail.winfo_width(),canvas_cous_detail.winfo_height(),fill='#2a2b2a')
                        canvas_cous_detail.pack(fill='both',expand=True)
                        scrollbar_cous_detail = tk.Scrollbar(Focus_tab,orient='vertical',command=canvas_cous_detail.yview,bg="#2a2b2a")
                        scrollbar_cous_detail.place(relx=1,rely=0,relheight=1,anchor='ne')
                        canvas_cous_detail.configure(yscrollcommand= scrollbar_cous_detail.set)
                        course_name_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text=name_course+":",font = ("<Times New Roman",30))
                        course_desc_content = ctk.CTkLabel(Focus_tab,corner_radius=10,text=course_desc,font = ("<Times New Roman",20))
                        course_duration_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="Duration of "+name_course+": "+str(course_duration)+" years",font = ("<Times New Roman",25))
                        collage_list_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="Suitable Collages:",font = ("<Times New Roman",30))
                        canvas_cous_detail.create_window((550,100),window=course_name_title)
                        canvas_cous_detail.create_window((550,200),window=course_desc_content)
                        canvas_cous_detail.create_window((550,300),window=course_duration_title)
                        canvas_cous_detail.create_window((550,400),window=collage_list_title)
                        x=550
                        y=500
                        for i in course_collage_list:
                            collage_button = collage_boottuns(str(i))
                            canvas_cous_detail.create_window((x,y),window=collage_button.collage_button_act)
                            y+=150
                    class course_boottuns:
                        def __init__(self,txt):
                            self.txt = txt
                            self.course_button_act = ctk.CTkButton(Focus_tab,corner_radius=10,text=self.txt, font = ("<Times New Roman",25),width=100,height=50,command=lambda:course_pressed(self.txt))
                    canvas_cous_press = tk.Canvas(Focus_tab,scrollregion=(0,0,2000,5000),bg="#2a2b2a")
                    canvas_cous_press.create_rectangle(0,0,canvas_cous_press.winfo_width(),canvas_cous_press.winfo_height(),fill='#2a2b2a')
                    canvas_cous_press.pack(fill='both',expand=True)
                    scrollbar_cous_press = tk.Scrollbar(Focus_tab,orient='vertical',command=canvas_cous_press.yview,bg="#2a2b2a")
                    scrollbar_cous_press.place(relx=1,rely=0,relheight=1,anchor='ne')
                    canvas_cous_press.configure(yscrollcommand= scrollbar_cous_press.set)
                    course_title = ctk.CTkLabel(Focus_tab,text = "The courses most suitable\nfor "+name_job+" are:",font = ("<Times New Roman",30),corner_radius=10)
                    canvas_cous_press.create_window((550,100),window=course_title)
                    cur.execute("Select * from Courses")
                    data_job_press = cur.fetchall()
                    courses_full_data_lst = []
                    for i in data_job_press:
                        if name_job in json.loads(i[1]):
                            courses_full_data_lst.append(i)
                    x=550
                    y=250
                    for i in courses_full_data_lst:
                        j = i[0]
                        course_button = course_boottuns(str(j))
                        canvas_cous_press.create_window((x,y),window=course_button.course_button_act)
                        y+=150
                cur.execute("select * from Job_opportunity")
                jobs_data = cur.fetchall()
                for i in jobs_data:
                    if(i[0] == text):
                        name_job = i[0]
                        avg_salary = i[1]
                        job_desc = ''
                        line_var = 0
                        for j in range(len(i[2])):
                            line_var += 1
                            if(line_var > 70 and i[2][j] == " "):
                                job_desc += '\n'
                                line_var = 0
                            job_desc += i[2][j]
                job_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text=name_job+":",font = ("<Times New Roman",30))
                job_slary_title = ctk.CTkLabel(Focus_tab,corner_radius=10,text="Average Salary:",font = ("<Times New Roman",30))
                job_slary_content = ctk.CTkLabel(Focus_tab,corner_radius=10,text=str(avg_salary),font = ("<Times New Roman",25))
                job_desc_content = ctk.CTkLabel(Focus_tab,corner_radius=10,text=job_desc,font = ("<Times New Roman",25))
                check_courses_button = ctk.CTkButton(Focus_tab,corner_radius=10,text="Check related courses",font = ("<Times New Roman",30),command = check_courses_pressed)
                job_title.place(relx = 0.0, rely= 0.1, relwidth = 0.5,anchor = 'w')
                job_desc_content.place(relx = 0.0, rely = 0.25, relwidth = 1,anchor = 'w')
                job_slary_title.place(relx = 0.0, rely = 0.5, relwidth = 0.5,anchor = 'w')
                job_slary_content.place(relx = 0.0, rely = 0.6, relwidth = 0.5,anchor = 'w')
                check_courses_button.place(relx = 0.5, rely = 0.85,relwidth = 0.6,anchor='center')
            class job_boottuns:
                def __init__(self,txt):
                    self.txt = txt
                    self.job_button_act = ctk.CTkButton(Focus_tab,corner_radius=10,text=self.txt, font = ("<Times New Roman",20),width=100,height=50,command=lambda:job_pressed(self.txt))
            canvas_cs_press = tk.Canvas(Focus_tab,scrollregion=(0,0,2000,5000),bg="#2a2b2a")
            canvas_cs_press.create_rectangle(0,0,canvas_cs_press.winfo_width(),canvas_cs_press.winfo_height(),fill='#2a2b2a')
            canvas_cs_press.pack(fill='both',expand=True)
            scrollbar_cs_press = tk.Scrollbar(Focus_tab,orient='vertical',command=canvas_cs_press.yview,bg="#2a2b2a")
            scrollbar_cs_press.place(relx=1,rely=0,relheight=1,anchor='ne')
            canvas_cs_press.configure(yscrollcommand= scrollbar_cs_press.set)
            heading_cs_press = ctk.CTkLabel(Focus_tab,corner_radius=10,text="These are the best possible\njobs after Humanities",font = ("<Times New Roman",30))
            canvas_cs_press.create_window((550,100),window=heading_cs_press)
            cur.execute("select * from Humanities")
            course_list_cs_raw = cur.fetchall()
            course_list_cs = []
            for i in course_list_cs_raw:
                course_list_cs.append(i[0])
            cur.execute("select * from Courses")
            course_list_data = cur.fetchall()
            jobs_list_cs_raw = []
            jobs_list_cs = []
            for i in course_list_data:
                if(i[0] in course_list_cs):
                    jobs_list_cs_raw.append(i[1])
            for i in jobs_list_cs_raw:
                jobs_list_cs.extend(json.loads(i))
            x=550
            y=250
            for i in jobs_list_cs:
                job_button = job_boottuns(str(i))
                canvas_cs_press.create_window((x,y),window=job_button.job_button_act)
                y+=150
        cs_button = ctk.CTkButton(Focus_tab,corner_radius=10,text="Computer\nScience", font = ("<Times New Roman",30),command=cs_pressed)
        bio_button = ctk.CTkButton(Focus_tab,corner_radius=10,text="Bio\nMaths", font = ("<Times New Roman",30),command=bio_pressed)
        com_button = ctk.CTkButton(Focus_tab,corner_radius=10,text="Commerce", font = ("<Times New Roman",30),command=com_pressed)
        hum_button = ctk.CTkButton(Focus_tab,corner_radius=10,text="Humanities", font = ("<Times New Roman",30),command=hum_pressed)
        heading = ctk.CTkLabel(Focus_tab,corner_radius=10,text="Select Your Stream", font = ("<Times New Roman",30))
        heading.place(relx = 0.5,rely = 0.1 ,relwidth = 0.9,anchor = "center")
        cs_button.place(relx = 0.25,rely = 0.35,relheight = 0.3,relwidth = 0.3,anchor = "center")
        bio_button.place(relx = 0.75,rely = 0.35,relheight = 0.3,relwidth = 0.3,anchor = "center")
        com_button.place(relx = 0.25,rely = 0.75,relheight = 0.3,relwidth = 0.3,anchor = "center")
        hum_button.place(relx = 0.75,rely = 0.75,relheight = 0.3,relwidth = 0.3,anchor = "center")
    start_label = ctk.CTkLabel(Focus_tab,corner_radius = 20,text="Explore your career options\nafter 12th with FOCUS...", font = ("<Times New Roman",35))
    start_button = ctk.CTkButton(Focus_tab,corner_radius = 25,text="Get Started",command=start_button_remove, font = ("<Times New Roman",35))
    start_button.place(relx = 0.5,rely = 0.6,anchor = "center")
    start_label.place(relx = 0.5, rely = 0.3, anchor = "center")
def aptitude():
    apt_dict_phy_1 = {"question": "What is the SI unit of force?", "options": ["Newton", "Watt", "Joule", "Ohm"], "answer": "Newton","Physics":False}
    apt_dict_phy_2 = {"question": "What is the speed of light in a vacuum (approximately)?", "options": ["300,000 m/s", "200,000 m/s", "400,000 m/s", "500,000 m/s"], "answer": "300,000 m/s","Physics":False}
    apt_dict_chem_1 = {"question": "What is the chemical symbol for gold?", "options": ["Au", "Ag", "Hg", "Cu"], "answer": "Au","Chemistry":False}
    apt_dict_chem_2 = {"question": "What is the atomic number of carbon?", "options": ["6", "12", "14", "16"], "answer": "6","Chemistry":False}
    apt_dict_math_1 = {"question": "What is 69 x 42?", "options": ["2898", "2438", "2988", "2328"], "answer": "2898","Math":False}
    apt_dict_math_2 = {"question": "What is 5 to the power of 5?", "options": ["25", "625", "125", "3125"], "answer": "3125","Math":False}
    apt_dict_eng_1 = {"question": "A person who speaks less is called?", "options": ["Misogynist", "Hypocrite", "Reticent", "Obsolate"], "answer": "Reticent","English":False}
    apt_dict_eng_2 = {"question": "A person who collects coins is called?", "options": ["Oologist", "Numismatist", "Arctophile", "Notaphilist "], "answer": "Numismatist","English":False}
    apt_dict_gk_1 = {"question": "Which gas do plants absorb from the atmosphere?", "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Methane"], "answer": "Carbon Dioxide","GK":False}
    apt_dict_gk_2 = {"question": "What is the capital of Spain?", "options": ["Paris", "Vienna", "Berlin", "Madrid"], "answer": "Madrid","GK":False}
    def apt_completed():
        def home_pressed_apt():
            label_apt_comp.place_forget()
            home_button_apt.place_forget()
            graph_button_apt.place_forget()
            aptitude()
        def get_graph():
            plt.bar(subjects, scores)
            plt.xlabel("Subjects")
            plt.ylabel("Scores")
            plt.title("Subject-wise Scores")
            plt.show()
        subject_score_dict = {"Physics":0,"Chemistry":0,"English":0,"Math":0,"GK":0}
        if(apt_dict_phy_1["Physics"]):
            subject_score_dict["Physics"] += 1
        if(apt_dict_phy_2["Physics"]):
            subject_score_dict["Physics"] += 1
        if(apt_dict_chem_1["Chemistry"]):
            subject_score_dict["Chemistry"] += 1
        if(apt_dict_chem_2["Chemistry"]):
            subject_score_dict["Chemistry"] += 1
        if(apt_dict_math_1["Math"]):
            subject_score_dict["Math"] += 1
        if(apt_dict_math_2["Math"]):
            subject_score_dict["Math"] += 1
        if(apt_dict_eng_1["English"]):
            subject_score_dict["English"] += 1
        if(apt_dict_eng_2["English"]):
            subject_score_dict["English"] += 1
        if(apt_dict_gk_1["GK"]):
            subject_score_dict["GK"] += 1
        if(apt_dict_gk_2["GK"]):
            subject_score_dict["GK"] += 1
        subjects = list(subject_score_dict.keys())
        scores = list(subject_score_dict.values())
        label_apt_comp = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="Here is the graph of your\nperformance in the aptitude test", font = ("<Times New Roman",30))
        label_apt_comp.place(relx = 0.5, rely = 0.2,relwidth = 0.9,anchor = "center")
        home_button_apt = ctk.CTkButton(Aptitude_tab,corner_radius = 20,text="Home", font = ("<Times New Roman",30),command=home_pressed_apt)
        home_button_apt.place(relx = 0.5, rely = 0.7,relwidth = 0.4,anchor = "center")
        graph_button_apt = ctk.CTkButton(Aptitude_tab,corner_radius = 20,text="Show Graph", font = ("<Times New Roman",30),command=get_graph)
        graph_button_apt.place(relx = 0.5, rely = 0.45,relwidth = 0.4,anchor = "center")
    def start_press_apt():
        start_button_apt.place_forget()
        intro_apt_label.place_forget()
        def enter_phy1():
            def remove_button_phy1():
                ques_label_phy1.place_forget()
                option_label_phy1_1.place_forget()
                option_label_phy1_2.place_forget()
                option_label_phy1_3.place_forget()
                option_label_phy1_4.place_forget()
                answer_entry_phy1.place_forget()
                enter_button_phy1.place_forget()
            def cor_incor_phy1():
                remove_button_phy1()
                def enter_phy2():
                    def remove_button_phy2():
                        ques_label_phy2.place_forget()
                        option_label_phy2_1.place_forget()
                        option_label_phy2_2.place_forget()
                        option_label_phy2_3.place_forget()
                        option_label_phy2_4.place_forget()
                        answer_entry_phy2.place_forget()
                        enter_button_phy2.place_forget()
                    def cor_incor_phy2():
                        remove_button_phy2()
                        def enter_chem1():
                            def remove_button_chem1():
                                ques_label_chem1.place_forget()
                                option_label_chem1_1.place_forget()
                                option_label_chem1_2.place_forget()
                                option_label_chem1_3.place_forget()
                                option_label_chem1_4.place_forget()
                                answer_entry_chem1.place_forget()
                                enter_button_chem1.place_forget()
                            def cor_incor_chem1():
                                remove_button_chem1()
                                def enter_chem2():
                                    def remove_button_chem2():
                                        ques_label_chem2.place_forget()
                                        option_label_chem2_1.place_forget()
                                        option_label_chem2_2.place_forget()
                                        option_label_chem2_3.place_forget()
                                        option_label_chem2_4.place_forget()
                                        answer_entry_chem2.place_forget()
                                        enter_button_chem2.place_forget()
                                    def cor_incor_chem2():
                                        remove_button_chem2()
                                        def enter_math1():
                                            def remove_button_math1():
                                                ques_label_math1.place_forget()
                                                option_label_math1_1.place_forget()
                                                option_label_math1_2.place_forget()
                                                option_label_math1_3.place_forget()
                                                option_label_math1_4.place_forget()
                                                answer_entry_math1.place_forget()
                                                enter_button_math1.place_forget()
                                            def cor_incor_math1():
                                                remove_button_math1()
                                                def enter_math2():
                                                    def remove_button_math2():
                                                        ques_label_math2.place_forget()
                                                        option_label_math2_1.place_forget()
                                                        option_label_math2_2.place_forget()
                                                        option_label_math2_3.place_forget()
                                                        option_label_math2_4.place_forget()
                                                        answer_entry_math2.place_forget()
                                                        enter_button_math2.place_forget()
                                                    def cor_incor_math2():
                                                        remove_button_math2()
                                                        def enter_eng1():
                                                            def remove_button_eng1():
                                                                ques_label_eng1.place_forget()
                                                                option_label_eng1_1.place_forget()
                                                                option_label_eng1_2.place_forget()
                                                                option_label_eng1_3.place_forget()
                                                                option_label_eng1_4.place_forget()
                                                                answer_entry_eng1.place_forget()
                                                                enter_button_eng1.place_forget()
                                                            def cor_incor_eng1():
                                                                remove_button_eng1()
                                                                def enter_eng2():
                                                                    def remove_button_eng2():
                                                                        ques_label_eng2.place_forget()
                                                                        option_label_eng2_1.place_forget()
                                                                        option_label_eng2_2.place_forget()
                                                                        option_label_eng2_3.place_forget()
                                                                        option_label_eng2_4.place_forget()
                                                                        answer_entry_eng2.place_forget()
                                                                        enter_button_eng2.place_forget()
                                                                    def cor_incor_eng2():
                                                                        remove_button_eng2()
                                                                        def enter_gk1():
                                                                            def remove_button_gk1():
                                                                                ques_label_gk1.place_forget()
                                                                                option_label_gk1_1.place_forget()
                                                                                option_label_gk1_2.place_forget()
                                                                                option_label_gk1_3.place_forget()
                                                                                option_label_gk1_4.place_forget()
                                                                                answer_entry_gk1.place_forget()
                                                                                enter_button_gk1.place_forget()
                                                                            def cor_incor_gk1():
                                                                                remove_button_gk1()
                                                                                def enter_gk2():
                                                                                    def remove_button_gk2():
                                                                                        ques_label_gk2.place_forget()
                                                                                        option_label_gk2_1.place_forget()
                                                                                        option_label_gk2_2.place_forget()
                                                                                        option_label_gk2_3.place_forget()
                                                                                        option_label_gk2_4.place_forget()
                                                                                        answer_entry_gk2.place_forget()
                                                                                        enter_button_gk2.place_forget()
                                                                                    def cor_incor_gk2():
                                                                                        remove_button_gk2()
                                                                                        apt_completed()
                                                                                    entered_gk2 = entry_var_gk2.get()
                                                                                    if entered_gk2 == apt_dict_gk_2["answer"]:
                                                                                        apt_dict_gk_2["GK"] = True
                                                                                        cor_incor_gk2()
                                                                                    elif entered_gk2 in apt_dict_gk_2["options"]:
                                                                                        cor_incor_gk2()
                                                                                    else:
                                                                                        entry_var_gk2.set("Invalid. Try again")
                                                                                entry_var_gk2 =  tk.StringVar()
                                                                                ques_label_gk2 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text=apt_dict_gk_2["question"], font = ("<Times New Roman",25))
                                                                                option_label_gk2_1 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="1) "+apt_dict_gk_2["options"][0], font = ("<Times New Roman",25))
                                                                                option_label_gk2_1.place(relx = 0.5,rely = 0.2,relwidth = 0.5,anchor = "center")
                                                                                option_label_gk2_2 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="2) "+apt_dict_gk_2["options"][1], font = ("<Times New Roman",25))
                                                                                option_label_gk2_2.place(relx = 0.5,rely = 0.3,relwidth = 0.5,anchor = "center")
                                                                                option_label_gk2_3 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="3) "+apt_dict_gk_2["options"][2], font = ("<Times New Roman",25))
                                                                                option_label_gk2_3.place(relx = 0.5,rely = 0.4,relwidth = 0.5,anchor = "center")
                                                                                option_label_gk2_4 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="4) "+apt_dict_gk_2["options"][3], font = ("<Times New Roman",25))
                                                                                option_label_gk2_4.place(relx = 0.5,rely = 0.5,relwidth = 0.5,anchor = "center")
                                                                                answer_entry_gk2 = ctk.CTkEntry(Aptitude_tab,corner_radius= 20, font = ("<Times New Roman",25),textvariable=entry_var_gk2)
                                                                                entry_var_gk2.set("Enter the answer")
                                                                                enter_button_gk2 = ctk.CTkButton(Aptitude_tab,corner_radius = 20,text="Enter", font = ("<Times New Roman",25),command=enter_gk2)
                                                                                ques_label_gk2.place(relx = 0.5,rely = 0.1,relwidth = 0.9,anchor = "center")
                                                                                answer_entry_gk2.place(relx = 0.5,rely = 0.6,relwidth = 0.5,anchor = "center")
                                                                                enter_button_gk2.place(relx = 0.5,rely = 0.7,relwidth = 0.5,anchor = "center")
                                                                            entered_gk1 = entry_var_gk1.get()
                                                                            if entered_gk1 == apt_dict_gk_1["answer"]:
                                                                                apt_dict_gk_1["GK"] = True
                                                                                cor_incor_gk1()
                                                                            elif entered_gk1 in apt_dict_gk_1["options"]:
                                                                                cor_incor_gk1()
                                                                            else:
                                                                                entry_var_gk1.set("Invalid. Try again")
                                                                        entry_var_gk1 =  tk.StringVar()
                                                                        ques_label_gk1 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text=apt_dict_gk_1["question"], font = ("<Times New Roman",25))
                                                                        option_label_gk1_1 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="1) "+apt_dict_gk_1["options"][0], font = ("<Times New Roman",25))
                                                                        option_label_gk1_1.place(relx = 0.5,rely = 0.2,relwidth = 0.5,anchor = "center")
                                                                        option_label_gk1_2 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="2) "+apt_dict_gk_1["options"][1], font = ("<Times New Roman",25))
                                                                        option_label_gk1_2.place(relx = 0.5,rely = 0.3,relwidth = 0.5,anchor = "center")
                                                                        option_label_gk1_3 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="3) "+apt_dict_gk_1["options"][2], font = ("<Times New Roman",25))
                                                                        option_label_gk1_3.place(relx = 0.5,rely = 0.4,relwidth = 0.5,anchor = "center")
                                                                        option_label_gk1_4 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="4) "+apt_dict_gk_1["options"][3], font = ("<Times New Roman",25))
                                                                        option_label_gk1_4.place(relx = 0.5,rely = 0.5,relwidth = 0.5,anchor = "center")
                                                                        answer_entry_gk1 = ctk.CTkEntry(Aptitude_tab,corner_radius= 20, font = ("<Times New Roman",25),textvariable=entry_var_gk1)
                                                                        entry_var_gk1.set("Enter the answer")
                                                                        enter_button_gk1 = ctk.CTkButton(Aptitude_tab,corner_radius = 20,text="Enter", font = ("<Times New Roman",25),command=enter_gk1)
                                                                        ques_label_gk1.place(relx = 0.5,rely = 0.1,relwidth = 0.9,anchor = "center")
                                                                        answer_entry_gk1.place(relx = 0.5,rely = 0.6,relwidth = 0.5,anchor = "center")
                                                                        enter_button_gk1.place(relx = 0.5,rely = 0.7,relwidth = 0.5,anchor = "center")
                                                                    entered_eng2 = entry_var_eng2.get()
                                                                    if entered_eng2 == apt_dict_eng_2["answer"]:
                                                                        apt_dict_eng_2["English"] = True
                                                                        cor_incor_eng2()
                                                                    elif entered_eng2 in apt_dict_eng_2["options"]:
                                                                        cor_incor_eng2()
                                                                    else:
                                                                        entry_var_eng2.set("Invalid. Try again")
                                                                entry_var_eng2 =  tk.StringVar()
                                                                ques_label_eng2 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text=apt_dict_eng_2["question"], font = ("<Times New Roman",25))
                                                                option_label_eng2_1 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="1) "+apt_dict_eng_2["options"][0], font = ("<Times New Roman",25))
                                                                option_label_eng2_1.place(relx = 0.5,rely = 0.2,relwidth = 0.5,anchor = "center")
                                                                option_label_eng2_2 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="2) "+apt_dict_eng_2["options"][1], font = ("<Times New Roman",25))
                                                                option_label_eng2_2.place(relx = 0.5,rely = 0.3,relwidth = 0.5,anchor = "center")
                                                                option_label_eng2_3 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="3) "+apt_dict_eng_2["options"][2], font = ("<Times New Roman",25))
                                                                option_label_eng2_3.place(relx = 0.5,rely = 0.4,relwidth = 0.5,anchor = "center")
                                                                option_label_eng2_4 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="4) "+apt_dict_eng_2["options"][3], font = ("<Times New Roman",25))
                                                                option_label_eng2_4.place(relx = 0.5,rely = 0.5,relwidth = 0.5,anchor = "center")
                                                                answer_entry_eng2 = ctk.CTkEntry(Aptitude_tab,corner_radius= 20, font = ("<Times New Roman",25),textvariable=entry_var_eng2)
                                                                entry_var_eng2.set("Enter the answer")
                                                                enter_button_eng2 = ctk.CTkButton(Aptitude_tab,corner_radius = 20,text="Enter", font = ("<Times New Roman",25),command=enter_eng2)
                                                                ques_label_eng2.place(relx = 0.5,rely = 0.1,relwidth = 0.9,anchor = "center")
                                                                answer_entry_eng2.place(relx = 0.5,rely = 0.6,relwidth = 0.5,anchor = "center")
                                                                enter_button_eng2.place(relx = 0.5,rely = 0.7,relwidth = 0.5,anchor = "center")
                                                            entered_eng1 = entry_var_eng1.get()
                                                            if entered_eng1 == apt_dict_eng_1["answer"]:
                                                                apt_dict_eng_1["English"] = True
                                                                cor_incor_eng1()
                                                            elif entered_eng1 in apt_dict_eng_1["options"]:
                                                                cor_incor_eng1()
                                                            else:
                                                                entry_var_eng1.set("Invalid. Try again")
                                                        entry_var_eng1 =  tk.StringVar()
                                                        ques_label_eng1 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text=apt_dict_eng_1["question"], font = ("<Times New Roman",25))
                                                        option_label_eng1_1 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="1) "+apt_dict_eng_1["options"][0], font = ("<Times New Roman",25))
                                                        option_label_eng1_1.place(relx = 0.5,rely = 0.2,relwidth = 0.5,anchor = "center")
                                                        option_label_eng1_2 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="2) "+apt_dict_eng_1["options"][1], font = ("<Times New Roman",25))
                                                        option_label_eng1_2.place(relx = 0.5,rely = 0.3,relwidth = 0.5,anchor = "center")
                                                        option_label_eng1_3 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="3) "+apt_dict_eng_1["options"][2], font = ("<Times New Roman",25))
                                                        option_label_eng1_3.place(relx = 0.5,rely = 0.4,relwidth = 0.5,anchor = "center")
                                                        option_label_eng1_4 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="4) "+apt_dict_eng_1["options"][3], font = ("<Times New Roman",25))
                                                        option_label_eng1_4.place(relx = 0.5,rely = 0.5,relwidth = 0.5,anchor = "center")
                                                        answer_entry_eng1 = ctk.CTkEntry(Aptitude_tab,corner_radius= 20, font = ("<Times New Roman",25),textvariable=entry_var_eng1)
                                                        entry_var_eng1.set("Enter the answer")
                                                        enter_button_eng1 = ctk.CTkButton(Aptitude_tab,corner_radius = 20,text="Enter", font = ("<Times New Roman",25),command=enter_eng1)
                                                        ques_label_eng1.place(relx = 0.5,rely = 0.1,relwidth = 0.9,anchor = "center")
                                                        answer_entry_eng1.place(relx = 0.5,rely = 0.6,relwidth = 0.5,anchor = "center")
                                                        enter_button_eng1.place(relx = 0.5,rely = 0.7,relwidth = 0.5,anchor = "center")
                                                    entered_math2 = entry_var_math2.get()
                                                    if entered_math2 == apt_dict_math_2["answer"]:
                                                        apt_dict_math_2["Math"] = True
                                                        cor_incor_math2()
                                                    elif entered_math2 in apt_dict_math_2["options"]:
                                                        cor_incor_math2()
                                                    else:
                                                        entry_var_math2.set("Invalid. Try again")
                                                entry_var_math2 =  tk.StringVar()
                                                ques_label_math2 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text=apt_dict_math_2["question"], font = ("<Times New Roman",25))
                                                option_label_math2_1 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="1) "+apt_dict_math_2["options"][0], font = ("<Times New Roman",25))
                                                option_label_math2_1.place(relx = 0.5,rely = 0.2,relwidth = 0.5,anchor = "center")
                                                option_label_math2_2 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="2) "+apt_dict_math_2["options"][1], font = ("<Times New Roman",25))
                                                option_label_math2_2.place(relx = 0.5,rely = 0.3,relwidth = 0.5,anchor = "center")
                                                option_label_math2_3 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="3) "+apt_dict_math_2["options"][2], font = ("<Times New Roman",25))
                                                option_label_math2_3.place(relx = 0.5,rely = 0.4,relwidth = 0.5,anchor = "center")
                                                option_label_math2_4 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="4) "+apt_dict_math_2["options"][3], font = ("<Times New Roman",25))
                                                option_label_math2_4.place(relx = 0.5,rely = 0.5,relwidth = 0.5,anchor = "center")
                                                answer_entry_math2 = ctk.CTkEntry(Aptitude_tab,corner_radius= 20, font = ("<Times New Roman",25),textvariable=entry_var_math2)
                                                entry_var_math2.set("Enter the answer")
                                                enter_button_math2 = ctk.CTkButton(Aptitude_tab,corner_radius = 20,text="Enter", font = ("<Times New Roman",25),command=enter_math2)
                                                ques_label_math2.place(relx = 0.5,rely = 0.1,relwidth = 0.9,anchor = "center")
                                                answer_entry_math2.place(relx = 0.5,rely = 0.6,relwidth = 0.5,anchor = "center")
                                                enter_button_math2.place(relx = 0.5,rely = 0.7,relwidth = 0.5,anchor = "center")
                                            entered_math1 = entry_var_math1.get()
                                            if entered_math1 == apt_dict_math_1["answer"]:
                                                apt_dict_math_1["Math"] = True
                                                cor_incor_math1()
                                            elif entered_math1 in apt_dict_math_1["options"]:
                                                cor_incor_math1()
                                            else:
                                                entry_var_math1.set("Invalid. Try again")
                                        entry_var_math1 =  tk.StringVar()
                                        ques_label_math1 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text=apt_dict_math_1["question"], font = ("<Times New Roman",25))
                                        option_label_math1_1 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="1) "+apt_dict_math_1["options"][0], font = ("<Times New Roman",25))
                                        option_label_math1_1.place(relx = 0.5,rely = 0.2,relwidth = 0.5,anchor = "center")
                                        option_label_math1_2 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="2) "+apt_dict_math_1["options"][1], font = ("<Times New Roman",25))
                                        option_label_math1_2.place(relx = 0.5,rely = 0.3,relwidth = 0.5,anchor = "center")
                                        option_label_math1_3 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="3) "+apt_dict_math_1["options"][2], font = ("<Times New Roman",25))
                                        option_label_math1_3.place(relx = 0.5,rely = 0.4,relwidth = 0.5,anchor = "center")
                                        option_label_math1_4 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="4) "+apt_dict_math_1["options"][3], font = ("<Times New Roman",25))
                                        option_label_math1_4.place(relx = 0.5,rely = 0.5,relwidth = 0.5,anchor = "center")
                                        answer_entry_math1 = ctk.CTkEntry(Aptitude_tab,corner_radius= 20, font = ("<Times New Roman",25),textvariable=entry_var_math1)
                                        entry_var_math1.set("Enter the answer")
                                        enter_button_math1 = ctk.CTkButton(Aptitude_tab,corner_radius = 20,text="Enter", font = ("<Times New Roman",25),command=enter_math1)
                                        ques_label_math1.place(relx = 0.5,rely = 0.1,relwidth = 0.9,anchor = "center")
                                        answer_entry_math1.place(relx = 0.5,rely = 0.6,relwidth = 0.5,anchor = "center")
                                        enter_button_math1.place(relx = 0.5,rely = 0.7,relwidth = 0.5,anchor = "center")
                                    entered_chem2 = entry_var_chem2.get()
                                    if entered_chem2 == apt_dict_chem_2["answer"]:
                                        apt_dict_chem_2["Chemistry"] = True
                                        cor_incor_chem2()
                                    elif entered_chem2 in apt_dict_chem_2["options"]:
                                        cor_incor_chem2()
                                    else:
                                        entry_var_chem2.set("Invalid. Try again")
                                entry_var_chem2 =  tk.StringVar()
                                ques_label_chem2 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text=apt_dict_chem_2["question"], font = ("<Times New Roman",25))
                                option_label_chem2_1 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="1) "+apt_dict_chem_2["options"][0], font = ("<Times New Roman",25))
                                option_label_chem2_1.place(relx = 0.5,rely = 0.2,relwidth = 0.5,anchor = "center")
                                option_label_chem2_2 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="2) "+apt_dict_chem_2["options"][1], font = ("<Times New Roman",25))
                                option_label_chem2_2.place(relx = 0.5,rely = 0.3,relwidth = 0.5,anchor = "center")
                                option_label_chem2_3 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="3) "+apt_dict_chem_2["options"][2], font = ("<Times New Roman",25))
                                option_label_chem2_3.place(relx = 0.5,rely = 0.4,relwidth = 0.5,anchor = "center")
                                option_label_chem2_4 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="4) "+apt_dict_chem_2["options"][3], font = ("<Times New Roman",25))
                                option_label_chem2_4.place(relx = 0.5,rely = 0.5,relwidth = 0.5,anchor = "center")
                                answer_entry_chem2 = ctk.CTkEntry(Aptitude_tab,corner_radius= 20, font = ("<Times New Roman",25),textvariable=entry_var_chem2)
                                entry_var_chem2.set("Enter the answer")
                                enter_button_chem2 = ctk.CTkButton(Aptitude_tab,corner_radius = 20,text="Enter", font = ("<Times New Roman",25),command=enter_chem2)
                                ques_label_chem2.place(relx = 0.5,rely = 0.1,relwidth = 0.9,anchor = "center")
                                answer_entry_chem2.place(relx = 0.5,rely = 0.6,relwidth = 0.5,anchor = "center")
                                enter_button_chem2.place(relx = 0.5,rely = 0.7,relwidth = 0.5,anchor = "center")
                            entered_chem1 = entry_var_chem1.get()
                            if entered_chem1 == apt_dict_chem_1["answer"]:
                                apt_dict_chem_1["Chemistry"] = True
                                cor_incor_chem1()
                            elif entered_chem1 in apt_dict_chem_1["options"]:
                                cor_incor_chem1()
                            else:
                                entry_var_chem1.set("Invalid. Try again")
                        entry_var_chem1 =  tk.StringVar()
                        ques_label_chem1 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text=apt_dict_chem_1["question"], font = ("<Times New Roman",25))
                        option_label_chem1_1 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="1) "+apt_dict_chem_1["options"][0], font = ("<Times New Roman",25))
                        option_label_chem1_1.place(relx = 0.5,rely = 0.2,relwidth = 0.5,anchor = "center")
                        option_label_chem1_2 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="2) "+apt_dict_chem_1["options"][1], font = ("<Times New Roman",25))
                        option_label_chem1_2.place(relx = 0.5,rely = 0.3,relwidth = 0.5,anchor = "center")
                        option_label_chem1_3 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="3) "+apt_dict_chem_1["options"][2], font = ("<Times New Roman",25))
                        option_label_chem1_3.place(relx = 0.5,rely = 0.4,relwidth = 0.5,anchor = "center")
                        option_label_chem1_4 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="4) "+apt_dict_chem_1["options"][3], font = ("<Times New Roman",25))
                        option_label_chem1_4.place(relx = 0.5,rely = 0.5,relwidth = 0.5,anchor = "center")
                        answer_entry_chem1 = ctk.CTkEntry(Aptitude_tab,corner_radius= 20, font = ("<Times New Roman",25),textvariable=entry_var_chem1)
                        entry_var_chem1.set("Enter the answer")
                        enter_button_chem1 = ctk.CTkButton(Aptitude_tab,corner_radius = 20,text="Enter", font = ("<Times New Roman",25),command=enter_chem1)
                        ques_label_chem1.place(relx = 0.5,rely = 0.1,relwidth = 0.9,anchor = "center")
                        answer_entry_chem1.place(relx = 0.5,rely = 0.6,relwidth = 0.5,anchor = "center")
                        enter_button_chem1.place(relx = 0.5,rely = 0.7,relwidth = 0.5,anchor = "center")
                    entered_phy2 = entry_var_phy2.get()
                    if entered_phy2 == apt_dict_phy_2["answer"]:
                        apt_dict_phy_2["Physics"] = True
                        cor_incor_phy2()
                    elif entered_phy2 in apt_dict_phy_2["options"]:
                        cor_incor_phy2()
                    else:
                        entry_var_phy2.set("Invalid. Try again")
                entry_var_phy2 =  tk.StringVar()
                ques_label_phy2 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text=apt_dict_phy_2["question"], font = ("<Times New Roman",25))
                option_label_phy2_1 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="1) "+apt_dict_phy_2["options"][0], font = ("<Times New Roman",25))
                option_label_phy2_1.place(relx = 0.5,rely = 0.2,relwidth = 0.5,anchor = "center")
                option_label_phy2_2 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="2) "+apt_dict_phy_2["options"][1], font = ("<Times New Roman",25))
                option_label_phy2_2.place(relx = 0.5,rely = 0.3,relwidth = 0.5,anchor = "center")
                option_label_phy2_3 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="3) "+apt_dict_phy_2["options"][2], font = ("<Times New Roman",25))
                option_label_phy2_3.place(relx = 0.5,rely = 0.4,relwidth = 0.5,anchor = "center")
                option_label_phy2_4 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="4) "+apt_dict_phy_2["options"][3], font = ("<Times New Roman",25))
                option_label_phy2_4.place(relx = 0.5,rely = 0.5,relwidth = 0.5,anchor = "center")
                answer_entry_phy2 = ctk.CTkEntry(Aptitude_tab,corner_radius= 20, font = ("<Times New Roman",25),textvariable=entry_var_phy2)
                entry_var_phy2.set("Enter the answer")
                enter_button_phy2 = ctk.CTkButton(Aptitude_tab,corner_radius = 20,text="Enter", font = ("<Times New Roman",25),command=enter_phy2)
                ques_label_phy2.place(relx = 0.5,rely = 0.1,relwidth = 0.9,anchor = "center")
                answer_entry_phy2.place(relx = 0.5,rely = 0.6,relwidth = 0.5,anchor = "center")
                enter_button_phy2.place(relx = 0.5,rely = 0.7,relwidth = 0.5,anchor = "center")
            entered_phy1 = entry_var_phy1.get()
            if entered_phy1 == apt_dict_phy_1["answer"]:
                apt_dict_phy_1["Physics"] = True
                cor_incor_phy1()
            elif entered_phy1 in apt_dict_phy_1["options"]:
                cor_incor_phy1()
            else:
                entry_var_phy1.set("Invalid. Try again")
        entry_var_phy1 =  tk.StringVar()
        ques_label_phy1 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text=apt_dict_phy_1["question"], font = ("<Times New Roman",25))
        option_label_phy1_1 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="1) "+apt_dict_phy_1["options"][0], font = ("<Times New Roman",25))
        option_label_phy1_1.place(relx = 0.5,rely = 0.2,relwidth = 0.5,anchor = "center")
        option_label_phy1_2 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="2) "+apt_dict_phy_1["options"][1], font = ("<Times New Roman",25))
        option_label_phy1_2.place(relx = 0.5,rely = 0.3,relwidth = 0.5,anchor = "center")
        option_label_phy1_3 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="3) "+apt_dict_phy_1["options"][2], font = ("<Times New Roman",25))
        option_label_phy1_3.place(relx = 0.5,rely = 0.4,relwidth = 0.5,anchor = "center")
        option_label_phy1_4 = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="4) "+apt_dict_phy_1["options"][3], font = ("<Times New Roman",25))
        option_label_phy1_4.place(relx = 0.5,rely = 0.5,relwidth = 0.5,anchor = "center")
        answer_entry_phy1 = ctk.CTkEntry(Aptitude_tab,corner_radius= 20, font = ("<Times New Roman",25),textvariable=entry_var_phy1)
        entry_var_phy1.set("Enter the answer")
        enter_button_phy1 = ctk.CTkButton(Aptitude_tab,corner_radius = 20,text="Enter", font = ("<Times New Roman",25),command=enter_phy1)
        ques_label_phy1.place(relx = 0.5,rely = 0.1,relwidth = 0.9,anchor = "center")
        answer_entry_phy1.place(relx = 0.5,rely = 0.6,relwidth = 0.5,anchor = "center")
        enter_button_phy1.place(relx = 0.5,rely = 0.7,relwidth = 0.5,anchor = "center")
    intro_apt_label = ctk.CTkLabel(Aptitude_tab,corner_radius = 20,text="Take a quick aptitude test to\n gauge your strengths and weaknesses", font = ("<Times New Roman",30))
    intro_apt_label.place(relx = 0.5,rely = 0.25,relwidth = 0.9,anchor = "center")
    start_button_apt = ctk.CTkButton(Aptitude_tab,corner_radius = 20,text="Start Test", font = ("<Times New Roman",30),command=start_press_apt)
    start_button_apt.place(relx = 0.5,rely = 0.55,relwidth = 0.4,anchor = "center")
focus()
aptitude()
f = open("credits.txt","r")
credits_label = ctk.CTkLabel(Credits_tab,corner_radius = 10,text=f.read(), font = ("<Times New Roman",40))
f.close()
credits_label.place(relx = 0.5, rely = 0.5, anchor = "center")
notebook.place(relx = 0.5, y = 30,relheight = 0.9,relwidth = 0.9, anchor = 'n')
window.resizable(False,False)
window.mainloop()