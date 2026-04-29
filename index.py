fonts=('Courier New',10,'bold')
from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter.ttk import Treeview


class Login:
    def __init__(self, root) -> None:
        self.root = root
        self.home()
    def home(self):
        self.choice = Frame(self.root, width=500, height=300)
        self.choice.place(x=100, y=50)
    #Student button
        original_image_student = PhotoImage(file='student.png')
        width_student, height_student = 100, 96
        resized_image_student = original_image_student.subsample(int(original_image_student.width() / width_student), int(original_image_student.height() / height_student))
        stu_label = Label(self.choice, image=resized_image_student)
        stu_label.image = resized_image_student
        stu_label.place(x=45, y=35)
        self.student = Button(self.choice, text="Student", bg='white',font=fonts, fg='dodgerblue', width=10, command=self.goto_login_student)
        self.student.place(x=57, y=150) 

        # Seller button
        original_image_seller = PhotoImage(file='sellar.png')
        width_seller, height_seller = 100, 96
        resized_image_seller = original_image_seller.subsample(int(original_image_seller.width() / width_seller), int(original_image_seller.height() / height_seller))
        sell_label = Label(self.choice, image=resized_image_seller)
        sell_label.image = resized_image_seller
        sell_label.place(x=305, y=30)
        self.seller = Button(self.choice, text="Seller", bg='white',font=fonts, fg='dodgerblue', width=10, command=self.goto_login_seller)
        self.seller.place(x=315, y=155)

    def goto_login_student(self):
        self.choice.destroy()
        self.login_window=Frame(self.root, width=500, height=300,bg= 'white',borderwidth=4)
        self.login_window.place(x=100, y=50)
        self.root.title("Student Login")
        self.user=""

        def check_login():
            entered_username = self.username_entry.get()
            self.user=self.username_entry.get()
            entered_password = self.password_entry.get()

            db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="***",
            database="trail")

            # Create a cursor object to interact with the database
            cursor = db_connection.cursor()

            try:
                # Execute a SELECT query to retrieve the user's details
                query = "SELECT * FROM student WHERE user_name = %s AND password = %s"
                cursor.execute(query, (entered_username, entered_password))

                # Fetch the result
                result = cursor.fetchone()

                if result:
                    # User exists, login successful
                    print("Login successful!")
                    self.login_window.destroy()
                    self.homestu()
                    # messagebox.showinfo('WELCOME', 'WELCOME USER')


                else:
                    # User not found or password incorrect
                    print("Invalid login credentials.")

            except mysql.connector.Error as err:
                print(f"Error: {err}")

            finally:
                # Close the cursor and connection
                cursor.close()
                db_connection.close()

        username_label=Label(self.login_window,text='UserName: ',font= ('Arial', 15),bg='white',fg='steel blue',width=15)
        username_label.place(x=60,y=80)
        self.username_entry=Entry(self.login_window,bg='white',fg='steel blue',font= ('Arial', 15),width=17)
        self.username_entry.place(x=200,y=80)

        password_label=Label(self.login_window,text='Password: ',font= ('Arial', 15),bg='white',fg='steel blue',width=15)
        password_label.place(x=60,y=150)
        self.password_entry=Entry(self.login_window,bg='white',fg='steel blue',font= ('Arial', 15),width=17,show='x')
        self.password_entry.place(x=200,y=150)

        login_button = Button(self.login_window, text="Login",font=('Arial', 11), command=check_login,bg='white',fg='steel blue')
        login_button.place(x=210, y=200)

        lable= Label(self.login_window,text="Not have an account..?",font=('Arial',10),fg='black',bg='white')
        lable.place(x=250,y=20)
        signup_button = Button(self.login_window, text="SignUp",font= ('Arial', 11), command=self.goto_signup_student,bg='white',fg='steel blue')
        signup_button.place(x=390, y=15)
        back_button=Button(self.login_window,text='< Back',font= ('Arial', 11),command=self.home,bg='white',fg='steelblue')
        back_button.place(x=30,y=20)


    def goto_login_seller(self, seller_name='default'):
        print("Seller button clicked")
        self.choice.destroy()
        self.login_window=Frame(self.root, width=500, height=300,bg= 'white',borderwidth=4)
        self.login_window.place(x=100, y=50)
        self.root.title("Seller Login")
        self.seller=''


        def check_login():
            entered_username = self.username_entry.get()
            entered_password = self.password_entry.get()
            self.seller=self.username_entry.get()

            db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="***",
            database="trail")

            # Create a cursor object to interact with the database
            cursor = db_connection.cursor()

            try:
                # Execute a SELECT query to retrieve the user's details
                query = "SELECT * FROM sellar WHERE username = %s AND password = %s"
                cursor.execute(query, (entered_username, entered_password))

                # Fetch the result
                result = cursor.fetchone()

                if result:
                    # User exists, login successful
                    print("Login successful!")
                    self.login_window.destroy()

                    # messagebox.showinfo('WELCOME', 'WELCOME USER')
                    self.home_sell()


                else:
                    # User not found or password incorrect
                    print("Invalid login credentials.")

            except mysql.connector.Error as err:
                print(f"Error: {err}")

            finally:
                # Close the cursor and connection
                cursor.close()
                db_connection.close()

                

        username_label=Label(self.login_window,text='UserName: ',font= ('Arial', 15),bg='white',fg='steel blue',width=15)
        username_label.place(x=60,y=80)
        self.username_entry=Entry(self.login_window,bg='white',fg='steel blue',font= ('Arial', 15),width=17)
        self.username_entry.place(x=200,y=80)

        password_label=Label(self.login_window,text='Password: ',font= ('Arial', 15),bg='white',fg='steel blue',width=15)
        password_label.place(x=60,y=150)
        self.password_entry=Entry(self.login_window,bg='white',fg='steel blue',font= ('Arial', 15),width=17,show='x')
        self.password_entry.place(x=200,y=150)

        login_button = Button(self.login_window, text="Login",font=('Arial', 11), command=check_login,bg='white',fg='steel blue')
        login_button.place(x=210, y=200)

        lable= Label(self.login_window,text="Not have an account..?",font=('Arial',10),fg='black',bg='white')
        lable.place(x=250,y=20)
        signup_button = Button(self.login_window, text="SignUp",font= ('Arial', 11), command=self.goto_signup_seller,bg='white',fg='steel blue')
        signup_button.place(x=390, y=15)
        back_button=Button(self.login_window,text='< Back',font= ('Arial', 11),command=self.home,bg='white',fg='steelblue')
        back_button.place(x=30,y=20)

    def goto_signup_student(self):
        print("student not have account")
        self.login_window.destroy()
        self.choice=Frame(self.root,width=500,height=300,bg='white')
        self.choice.place(x=100,y=50)

        self.stu_name=Label(self.choice,text='Name: ',font=('Courier New',15,'bold'),bg='white',fg='steel blue',width=15)
        self.stu_name.place(x=50,y=60)
        self.name=Entry(self.choice,bg='white',fg='steel blue',font=('Courier New',13,'bold'),width=17)
        self.name.place(x=230,y=60)

        self.stu_age=Label(self.choice,text='Age: ',font=('Courier New',15,'bold'),bg='white',fg='steel blue',width=15)
        self.stu_age.place(x=50,y=100)
        self.age=Entry(self.choice,bg='white',fg='steel blue',font=('Courier New',13,'bold'),width=17)
        self.age.place(x=230,y=100)

        self.stu_username=Label(self.choice,text='UserName: ',font=('Courier New',15,'bold'),bg='white',fg='steel blue',width=15)
        self.stu_username.place(x=50,y=140)
        self.username=Entry(self.choice,bg='white',fg='steel blue',font=('Courier New',13,'bold'),width=17)
        self.username.place(x=230,y=140)

        self.stu_passw=Label(self.choice,text='Set Password: ',font=('Courier New',15,'bold'),bg='white',fg='steel blue',width=15)
        self.stu_passw.place(x=50,y=180)
        self.password=Entry(self.choice,bg='white',fg='steel blue',font=('Courier New',13,'bold'),width=17,show='x')
        self.password.place(x=230,y=180)

        self.signup_btn=Button(self.choice,text="SignUp",bg='white',fg='steel blue',font=fonts,width=10,command=self.stu_home)
        self.signup_btn.place(x=200,y=230)
        back_button=Button(self.choice,text='< Back',font= ('Arial', 11),command=self.goto_login_student,bg='white',fg='steelblue')
        back_button.place(x=30,y=20)

    
    def goto_signup_seller(self):
        print("seller do't have account")
        self.login_window.destroy()
        self.choice=Frame(self.root,width=500,height=300,bg='white')
        self.choice.place(x=100,y=50)

        self.sell_name=Label(self.choice,text='Name: ',font=('Courier New',15,'bold'),bg='white',fg='steel blue',width=15)
        self.sell_name.place(x=50,y=60)
        self.name=Entry(self.choice,bg='white',fg='steel blue',font=('Courier New',13,'bold'),width=17)
        self.name.place(x=230,y=60)

        self.sell_add=Label(self.choice,text='Address: ',font=('Courier New',15,'bold'),bg='white',fg='steel blue',width=15)
        self.sell_add.place(x=50,y=100)
        self.address=Entry(self.choice,bg='white',fg='steel blue',font=('Courier New',13,'bold'),width=17)
        self.address.place(x=230,y=100)

        self.sell_mobileno=Label(self.choice,text='MobileNo:',font=('Courier New',15,'bold'),bg='white',fg='steel blue',width=15)
        self.sell_mobileno.place(x=50,y=140)
        self.mobileno=Entry(self.choice,bg='white',fg='steel blue',font=('Courier New',13,'bold'),width=17)
        self.mobileno.place(x=230,y=140)

        self.sell_username=Label(self.choice,text='UserName: ',font=('Courier New',15,'bold'),bg='white',fg='steel blue',width=15)
        self.sell_username.place(x=50,y=180)
        self.username=Entry(self.choice,bg='white',fg='steel blue',font=('Courier New',13,'bold'),width=17)
        self.username.place(x=230,y=180)

        self.sell_passw=Label(self.choice,text='Set Password: ',font=('Courier New',15,'bold'),bg='white',fg='steel blue',width=15)
        self.sell_passw.place(x=50,y=220)
        self.password=Entry(self.choice,bg='white',fg='steel blue',font=('Courier New',13,'bold'),width=17,show='x')
        self.password.place(x=230,y=220)

        self.signup_btn=Button(self.choice,text="SignUp",bg='white',fg='steel blue',font=fonts,width=10,command=self.sell_home)
        self.signup_btn.place(x=200,y=260)
        back_button=Button(self.choice,text='< Back',font= ('Arial', 11),command=self.goto_login_seller,bg='white',fg='steelblue')
        back_button.place(x=30,y=20)

    def stu_home(self):
        
        if self.name.get()=="" or self.age.get()=="" or self.username=="" or self.password=="":
            messagebox.showerror('error', 'error enter details correctly')
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="***",database="trail")
            my_cursor=conn.cursor()
            self.query = f"insert into student values('{self.name.get()}',{self.age.get()},'{self.username.get()}','{self.password.get()}')"
            my_cursor.execute(self.query)
            self.choice.destroy()
            # messagebox.showinfo('WELCOME', 'WELCOME USER')
            conn.commit()
            conn.close()
            self.goto_login_student()

    def sell_home(self):
        if self.name.get()=="" or self.address.get()=="" or self.mobileno.get()=="" or self.username=="" or self.password=="":
            messagebox.showerror('error', 'error enter details correctly')
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="***",database="trail")
            my_cursor=conn.cursor()
            self.query = f"insert into sellar values('{self.name.get()}','{self.address.get()}','{self.mobileno.get()}','{self.username.get()}','{self.password.get()}')"
            my_cursor.execute(self.query)
            self.choice.destroy()
            # messagebox.showinfo('WELCOME', 'WELCOME USER')
            conn.commit()
            conn.close()
            self.goto_login_seller()

    def stu_homepage(self):
        self.login_window=Frame(self.root, width=500, height=300,bg= 'white',borderwidth=4)
        self.login_window.place(x=100, y=50)
        self.root.title("Student Homepage")
        signup_button = Button(self.login_window, text="Rushita Medical Shop",font= ('Arial', 11), command=lambda: self.details("rushita"),bg='white',fg='steel blue',width=30)
        signup_button.place(x=110, y=50)
        signup_button = Button(self.login_window, text="Yagna Medical Shop",font= ('Arial', 11), command=lambda: self.details("yagna"),bg='white',fg='steel blue',width=30)
        signup_button.place(x=110, y=100)
        signup_button = Button(self.login_window, text="Rupa Medical Shop",font= ('Arial', 11), command=lambda: self.details("sri"),bg='white',fg='steel blue',width=30)
        signup_button.place(x=110, y=150)
        signup_button = Button(self.login_window, text="Suryaja Medical Shop",font= ('Arial', 11), command=lambda: self.details("surya"),bg='white',fg='steel blue',width=30)
        signup_button.place(x=110, y=200)

        self.logout=Button(self.login_window,text="<",bg='white',fg='steel blue',font=('Arial',15),command=self.homestu)
        self.logout.place(x=60,y=125)
    def home_sell(self):
        self.choice=Frame(self.root,width=500,height=300,bg='white',borderwidth=4)
        self.choice.place(x=100,y=50)
        self.root.title("Seller Homepage")
        self.l=Label(self.choice,text="Welcome to PILL PARCEL....",bg='white',font=('Arial', 15),fg='steel blue')
        self.l.place(x=100,y=20)

        self.quote=Label(self.choice,text='"The key to mastering sales is the ability\n to understand and respond \nto the needs of the customer." - Unknown',bg='white',fg='black',font=fonts)
        self.quote.place(x=80,y=100)
        self.view=Button(self.choice,text='Logout',bg='white',fg='steel blue',font=('Arial',8),command=self.goto_login_seller)
        self.view.place(x=80,y=190)
        self.logout=Button(self.choice,text='View Prescription',bg='white',font=('Arial', 8),fg='steel blue',command=self.sell_homepage)
        self.logout.place(x=340,y=190)

    def sell_homepage(self):
        login_window = Frame(root, width=500, height=300, bg='white', borderwidth=4)
        login_window.place(x=100, y=50)

        prescription_tree = Treeview(login_window, columns=("prescription", "student"), show="headings", height=10)
        # prescription_tree.column("prescription",width=300,anchor='w')
        # prescription_tree.column("student",width=200,anchor='w')

        prescription_tree.heading("prescription", text="Prescription")
        prescription_tree.heading("student", text="Student")
        prescription_tree.place(x=50, y=20)
        back_button=Button(login_window,text='< Back',font= ('Arial', 8),command=self.home_sell,bg='white',fg='steelblue')
        back_button.place(x=40,y=260)
        clear=Button(login_window,text='clear',font= ('Arial', 8),bg='white',fg='steelblue',command=self.clear_pre)
        clear.place(x=430,y=260)

        try:
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="***",
                database="trail")

            cursor = db_connection.cursor()

            # seller = ""
            query = f"select prescription, student from prescription where sellar='{self.seller}'"
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
            current_student = None
            for prescription, student in result:
                lines = prescription.split("\n")
                for line in lines:
                    if student != current_student:
                        prescription_tree.insert("", "end", values=(line, student))
                        current_student = student
                    else:
                        prescription_tree.insert("", "end", values=(line,))

            db_connection.commit()
        except mysql.connector.Error as error:
            print("Error:", error)
        finally:
            if 'db_connection' in locals() or 'db_connection' in globals():
                db_connection.close()


    def clear_pre(self):
        db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="***",
                database="trail")

        cursor = db_connection.cursor()
        query = f"delete from prescription where sellar='{self.seller}'"
        cursor.execute(query)
        db_connection.commit()
        self.sell_homepage()


    def details(self, seller_name):
        self.login_window.destroy()
        self.root.title("Enter your Prescription")
        self.login_window=Frame(self.root, width=500, height=300,bg= 'white',borderwidth=4)
        self.login_window.place(x=100, y=50)
        prescription_label = Label(self.login_window, text='Enter Prescription:', font=('Arial', 15), bg='white', fg='steel blue', width=20)
        prescription_label.place(x=50, y=20)

        self.prescription_text = Text(self.login_window, width=40, height=10, wrap="word", font=('Arial', 12))
        self.prescription_text.place(x=50, y=60)

        # Add a button to submit the prescription
        submit_button = Button(self.login_window, text="Submit Prescription", font=('Arial', 11), command=lambda: self.submit_prescription(seller_name), bg='white', fg='steel blue')
        submit_button.place(x=180, y=240)
        self.logout=Button(self.login_window,text="<back",bg='white',fg='steel blue',font=('Arial',8),command=self.stu_homepage)
        self.logout.place(x=30,y=21)

    def submit_prescription(self, seller_name):
        prescription_content = self.prescription_text.get("1.0", "end-1c")
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="***",
            database="trail")

        cursor = db_connection.cursor()

        try:
            # Insert prescription into the database
            query = f"insert into prescription values('{prescription_content}','{self.user}','{seller_name}')"
            cursor.execute(query)
            db_connection.commit()

            # Send SMS notification to the seller
            from twilio.rest import Client
            if seller_name == "yagna":
                account_sid = '***'
                auth_token = '***'

                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    body='Prescription submitted by a student. Please check your dashboard.',
                    from_='***',  # Replace with your Twilio phone number
                    to='***'  # Replace with the seller's phone number
                )
            else:
                account_sid = '***'
                auth_token = '***'

                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    body='Prescription submitted by a student. Please check your dashboard.',
                    from_='***',  # Replace with your Twilio phone number
                    to='***'  # Replace with the seller's phone number
                )

            print('Prescription submitted and SMS sent successfully. SID:', message.sid)
            print(message.body)

        except mysql.connector.Error as error:
            print("Error:", error)

        finally:
            if 'db_connection' in locals() or 'db_connection' in globals():
                db_connection.close()

        self.stu_homepage()

    def homestu(self):
        # self.choice.destroy
        self.choice=Frame(self.root,width=500,height=300,bg='white',borderwidth=4)
        self.choice.place(x=100,y=50)
        self.root.title("Student Homepage")
        self.l=Label(self.choice,text="Welcome to PILL PARCEL....",bg='white',font=('Arial', 15),fg='steel blue')
        self.l.place(x=100,y=20)

        self.quote=Label(self.choice,text='"In the world of medicine, \na pharmacist is a friend you can trust."',bg='white',fg='black',font=fonts)
        self.quote.place(x=80,y=100)
        self.view=Button(self.choice,text='Logout',bg='white',fg='steel blue',font=('Arial',8),command=self.goto_login_student)
        self.view.place(x=80,y=190)
        self.choose=Label(self.choice,text="Submit prescription by",bg='white',font=('Arial', 9),fg='steel blue')
        self.choose.place(x=220,y=190)
        self.logout=Button(self.choice,text='Choosing',bg='white',font=('Arial', 8),fg='steel blue',command=self.stu_homepage)
        self.logout.place(x=350,y=190)
    


root = Tk()
root.title('PILL PARCEL')
root.geometry('700x400+450+100')
root.resizable(False, False)

login = Login(root)
root.mainloop()


