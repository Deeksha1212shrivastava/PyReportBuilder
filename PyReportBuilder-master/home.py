from tkinter import *
from tkinter import Tk, Button, Label, Frame, filedialog, messagebox, ttk
from PIL import ImageTk, Image
import mysql.connector
from mysql.connector import Error
import pandas as pd
# from tkcalendar import Calendar
from datetime import date


class HomePage:
    # def __init__(self,login_window ):
    #     self.login_window = login_window

    def __init__(self):
        # GUI PART
        self.home_window = Tk()
        self.home_window.title("Home Page")
        self.home_window.geometry('994x664')
        self.home_window.resizable(0, 0)

        # bg_color = "#FFA3AC"
        self.bg_color = "lavender"
        self.home_window.configure(background=self.bg_color)

        # report heading
        self.welcome_label = Label(self.home_window, text="Report Generator", font=("Helvetica", 30), bg=self.bg_color, fg="#00043C")
        self.welcome_label.pack(padx=20, pady=20, side='top')

        # logout button
        self.logout_button = Button(self.home_window, text="Log Out", font=("Helvetica", 12, 'bold'), bg='red', fg='white', command=self.logout)
        self.logout_button.place(x=850, y=35)
        self.menu()
        self.GUIofapp()

        self.host = 'localhost'
        self.username = 'root'
        self.password = 'Shruti098%'
        self.database = 'userdata'
        self.table_name = 'trainingsdb'

        # # Connect to the MySQL database
        # self.conn = mysql.connector.connect( host = self.host, user = self.username, password = self.password, database = self.database )
        # self.cursor = self.conn.cursor()

    def GUIofapp(self):

        # frame 1
        self.frame1 = Frame(self.home_window, bg=self.bg_color, bd=2, relief="groove", width=500, height=500)
        self.frame1.pack(padx=(40,15), pady=70, side=LEFT, fill=BOTH, expand=True)
        
        # frame 2
        self.frame2 = Frame(self.home_window, bg=self.bg_color, bd=2, relief="ridge", width=500, height=500)
        self.frame2.pack(padx=(15,15), pady=70, side=LEFT, fill=BOTH, expand=True)

        # frame 3
        self.frame3 = Frame(self.home_window, bg=self.bg_color, bd=2, relief="groove", width=500, height=500)
        self.frame3.pack(padx=(15,40), pady=70, side=LEFT, fill=BOTH, expand=True)

        # self.frame1.place(x=75, y=200)
        # self.frame2.place(x=400, y=200)

        # ------------------------------------------- FRAME 01
        # Add a heading 1 in frame 1
        self.heading1 = Label(self.frame1, text='Upload Excel File', font=('Microsoft Yahei UI Light', 20, 'bold'), bg=self.bg_color, fg='#00043C')
        self.heading1.pack(padx=10, pady=10)

        self.subheading11 = Label(self.frame1, text="Select a file to upload in Database.", font=('Microsoft Yahei UI Light', 12), bg=self.bg_color, fg='#00043C')
        self.subheading11.pack(padx=10, pady=10)

        # Add a button *Choose a File* in frame 1
        self.button11 = Button(self.frame1, text='Choose a File', font=("Helvetica", 12, 'bold'), bg='green3', fg='white', command=self.open_file)
        self.button11.pack(padx=10, pady=10)

        # Add a Label 1 in frame 1
        self.filename_label = Label(self.frame1, text="", font=('Microsoft Yahei UI Light', 9, 'bold'), wraplength=280, bg=self.bg_color) # Adjust wrap length as needed
        self.filename_label.pack()

        # Add a button  *Upload to DataBase*  in frame 1
        self.button12 = Button(self.frame1, text='Upload to DataBase', font=("Helvetica", 12, 'bold'), bg='green3', fg='white', command=self.send_data_to_database)
        self.button12.pack(padx=10, pady=10)

        # ----------------------------------------- FRAME 02
        # Add a heading 2 for frame 2 
        self.heading2 = Label(self.frame2, text="SEARCH Trainings", font=('Microsoft Yahei UI Light', 20, 'bold'), bg=self.bg_color, fg='#00043C')
        self.heading2.pack(padx=10, pady=10, side='top')
                
        # Add a heading 4 in frame 2
        self.subheading21 = Label(self.frame2, text="Choose the Month and Year", font=('Microsoft Yahei UI Light', 12), bg=self.bg_color, fg='#00043C')
        self.subheading21.pack(padx=10, pady=10)

        frameinside = Frame(self.frame2, background=self.bg_color)
        frameinside.pack( ipadx=10, ipady=10)

        frameinside2 = Frame(self.frame2, background=self.bg_color)
        frameinside2.pack( ipadx=10, ipady=10)

        def generate_date():
            month = self.month_combo.get()
            year = self.year_combo.get()

            # Generate the complete date
            date_str = f"{month}/01/{year}"
            print("Generated Date:", date_str)

        month_label = ttk.Label(frameinside,  font=('Microsoft Yahei UI Light', 10), text="Month:",background=self.bg_color)
        month_label.pack(padx=5, side='left')
        
        self.month_combo = ttk.Combobox(frameinside, values=['01', '02', '03', '04','05', '06', '07', '08','09', '10', '11', '12'], width=10)
        self.month_combo.configure(font=("Helvetica", 10), background="blue")
        self.month_combo.set('month')
        self.month_combo.pack(padx=5, side='left')

        # Year Dropdown
        year_label = ttk.Label(frameinside2 ,font=('Microsoft Yahei UI Light', 12), text="Year:", background=self.bg_color)
        year_label.pack(padx=5,side='left')

        # Get current year
        current_year = date.today().year

        # Create a list of years from the current year up to 10 years in the future
        year_values = [str(year) for year in range(current_year - 10, current_year +1)]

        self.year_combo = ttk.Combobox(frameinside2, values=year_values, width=10)
        # self.year_combo.packside='top'()
        self.year_combo.configure(font=("Helvetica", 10), background="blue")
        self.year_combo.set('year')
        self.year_combo.pack(padx=5, side='left')

        # Generate Date Button
        self.select_date_button = Button(self.frame2, text="Select Date",font=("Helvetica", 12, 'bold'), bg="sky blue", fg="#ffffff", command=self.search_dates)
        self.select_date_button.pack(padx=10, pady=10)

        # ----------------------------------------- FRAME 03

        self.heading3 = Label(self.frame3, text="Generate Report", font=('Microsoft Yahei UI Light', 20, 'bold'), bg=self.bg_color, fg='#00043C')
        self.heading3.pack(padx=10, pady=10, side='top')

        # Add a heading 3 in frame 3
        self.subheading31 = Label(self.frame3, text="Select options from Dropdown", font=('Microsoft Yahei UI Light', 12), bg=self.bg_color, fg='#00043C')
        self.subheading31.pack(padx=10, pady=10)

        # Create the first dropdown
        self.options_list1 = ["Select", "Gender", "State", "Organization Sector", "Organization belongs to SME/Non-SME","Officer belongs to SC/ST (Yes/No)", "Officer belongs to PWD category (Yes/No)"]
        
        self.dropdown1 = ttk.Combobox(self.frame3, values=self.options_list1, state="readonly")
        self.dropdown1.set("Select")
        self.dropdown1.configure(font=("Helvetica", 12), background="blue")
        self.dropdown1.pack(padx=10, pady=(10, 10))

        # Create the second dropdown
        self.options_list2 = []

        self.dropdown2 = ttk.Combobox(self.frame3, values=self.options_list2, state="readonly")
        self.dropdown2.set("Select")
        self.dropdown2.configure(font=("Helvetica", 12), background="blue")
        self.dropdown2.pack(padx=10, pady=(10, 10))

        self.dropdown1.bind("<<ComboboxSelected>>", self.update_dropdown2)

        # Add a button to *generate report* in frame 2
        self.report_button = Button(self.frame3, text="Generate", font=("Helvetica", 12, 'bold'), bg="#FF9800", fg="#ffffff", command = self.fetch_data)
        self.report_button.pack(padx=10, pady=10)

    def update_dropdown2(self, event):

        selected_option = self.dropdown1.get()

        if selected_option == "Select":
            self.options_list2 = ["Select"]
            # break
        elif selected_option == "Gender":
            self.options_list2 = ["Male", "Female"]
            # break
        elif selected_option == "State":
            self.options_list2 = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala","Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "New Delhi", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttarakhand", "Uttar Pradesh", "West Bengal"]
            # break
        elif selected_option == "Organization Sector":
            self.options_list2 = ('Central Government', 'State Government', 'Defence', 'PSU', 'Finance','Banking', 'Power', 'Energy', 'Telecom', 'Transport','Manufacturing', 'LEA', 'Academia', 'Private', 'IT', 'ITeS')
            # break
        elif selected_option == "Organization belongs to SME/Non-SME":
            self.options_list2 = ["SME", "Non-SME"]
            # break
        elif selected_option == "Officer belongs to SC/ST (Yes/No)":
            self.options_list2 = ["Yes", "No"]
            # break
        elif selected_option == "Officer belongs to PWD category (Yes/No)":
            self.options_list2 = ["Yes", "No"]
            # break
        else:
            self.options_list2 = ["Select"]

        self.dropdown2["values"] = self.options_list2
        self.dropdown2.current(0)

    def menu(self):
        def myfun():
            print("File menu working")

        def quitw():
            result = messagebox.askquestion(
                "Quit", "Are you sure you want to quit?")
            if result == "yes":
                self.frame2.destroy()

        # making a menu bar
        self.mymenu = Menu(self.home_window)
        self.mymenu.add_command(label="File", command=myfun)
        # self.mymenu.add_command(label="Home", command=open_second_script)
        self.mymenu.add_command(label="Quit", command=quitw)
        self.mymenu.add_command(label="Help", command=myfun)
        self.home_window.config(menu=self.mymenu)

    def open_file(self):

        filename = filedialog.askopenfilename(title="Select Excel file", filetypes=[("Excel files", "*.xlsx;*.xls")])

        if filename:

            # self.data = pd.read_excel(filename)
            # self.send_data_to_database(self.data)
            self.excel_data = pd.read_excel(filename)

            # df.empty: This condition checks if the DataFrame df is empty, meaning it does not contain any rows or columns. It is typically used to check if the DataFrame has any data.
            if self.excel_data.empty:
                messagebox.showinfo(title="Failure", message="Excel file is empty!!")
                return

            # print(self.excel_data)

            # self.tick_mark_label.config(text="✔ File Loaded Successfully", fg="green")

            self.filename_label.config(text="Selected file: " + filename, fg='green2')
            messagebox.showinfo(title="Success", message="Excel file opened successfully.")
            
            check = True
        else:

            self.filename_label.config(text="❌ File Loading Failed", fg="red")
            messagebox.showinfo(title="Failure", message="Excel file opening failed. Try Again!!!")

            # self.tick_mark_label.config(text="❌ File Loading Failed", fg="red")
            check = False

    def send_data_to_database(self):
        
        # Connect to the MySQL database
        self.conn = mysql.connector.connect( host = self.host, user = self.username, password = self.password, database = self.database )
        self.cursor = self.conn.cursor()

        insert_query = ''' INSERT INTO trainingsdb (
            TrainingProgramName,
            TrainingProgramDate,
            Name,
            Designation,
            Gender,
            Email,
            MobileNumber,
            Organization,
            OfficeAddress,
            State,
            OrganizationSector,
            OrganizationCategorySMEorNonSME,
            OfficerBelongsToSCOrST,
            OfficerBelongsToPWD
        ) values (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
        '''
        success_count = 0
        for index, row in self.excel_data.iterrows():
            record_data = []
            # for value in row:
            
            # for column_name, value in row.items():

            for column_name in row.index:
                if column_name != 'SNo':  # Skip the 'SNo' column
                    value = row[column_name]        # to comment later
                    if pd.isnull(value):
                        record_data.append(None)  # Convert NaN values to None (null)
                    else:
                        record_data.append(value)
                
            # print('index = ',index)
            # print('row = ',row)
            # print('record_data = ',record_data)
            try:
                self.cursor.execute(insert_query, record_data)  # Execute the query
                self.conn.commit() 
                success_count += 1

            except Exception as e:
                print("Error inserting record:", e)

        self.cursor.close()
        self.conn.close()

        if (success_count == 0):
            messagebox.showerror("Error","Error inserting record")
        else :
            # Display a message box with the success count
            messagebox.showinfo("Query Execution Result", f"Query executed successfully for {success_count} records.")

    def fetch_data(self):

        # Create a mapping dictionary for column name variations
        column_mapping = {
            'SNo'                 : 'ID',
            'Training Program Name' : 'TrainingProgramName',
            'Training Program Date' : 'TrainingProgramDate',
            'Name of the Officer'   : 'Name',
            'Designation'           : 'Designation',
            'Gender'                : 'Gender',
            'Email Address'         : 'Email',
            'Mobile Number'         : 'MobileNumber',
            'Organization'          : 'Organization',
            'State'                 : 'State',
            'Organization Sector'   : 'OrganizationSector',
            'Office Address with State/UT details'     : 'OfficeAddress',
            'Organization belongs to SME/Non-SME'      : 'OrganizationCategorySMEorNonSME',
            'Officer belongs to SC/ST (Yes/No)'        : 'OfficerBelongsToSCOrST',
            'Officer belongs to PWD category (Yes/No)' : 'OfficerBelongsToPWD'
        }

        # Obtain the user input for column name and search value
        column = self.dropdown1.get()
        value = self.dropdown2.get()
        month = self.month_combo.get()
        year = self.year_combo.get()

        if column == 'Select' or value == 'Select':
            messagebox.showinfo("Select Data", "Choose a Column and VAlue")
            return

        column_name = column_mapping[column]

        # Connect to the MySQL database
        self.conn = mysql.connector.connect( host = self.host, user = self.username, password = self.password, database = self.database )
        self.cursor = self.conn.cursor()

        try: 
            # Query 1
            query1 = ''' SELECT (SELECT COUNT(*) FROM trainingsdb) AS total_candidates, (SELECT COUNT(*) FROM trainingsdb WHERE LOWER(gender) LIKE LOWER('%female%')) AS total_females, (SELECT COUNT(*) FROM trainingsdb WHERE (OfficerBelongsToSCOrST) LIKE LOWER('%yes%')) AS SC_ST_candidates, COUNT(DISTINCT State) AS total_distinct_states FROM trainingsdb; '''
            self.cursor.execute(query1)
            result1 = self.cursor.fetchall()

            # Get the column names
            columns = [desc[0] for desc in self.cursor.description]
            # Combine column names and result rows
            rows_with_column_names = [columns] + list(result1)
            # Print the result as a table
            print('\n','fetching data from database!')
            for row in rows_with_column_names:
                print("{:<20} {:<20} {:<20} {:<20}".format(*row))

            print ('\n',column,":",value,'\n')

            #  performing query for all data in dataBase
            if (month == 'month') or (year == 'year'):

                # Fetch the count of rows from the result
                query2 = f"SELECT COUNT(*) FROM trainingsdb WHERE LOWER({column_name}) = LOWER('{value}' )"
                self.cursor.execute(query2)
                result2 = self.cursor.fetchall()
                r = len(result2)

                print( f"COUNT of {column} with value {value} : {r}")

                if len(result2) == 0:
                    print("NONE records match!")
                    messagebox.showinfo('Empty Set', 'NO record available in the database')
                else:
                    # Fetch all the rows from the result
                    query3 = f"SELECT * FROM trainingsdb WHERE LOWER({column_name}) = LOWER('{value}')"
                    self.cursor.execute(query3)
                    result3 = self.cursor.fetchall()

                    messagebox.showinfo('RESULTS', str(len(result3)) + ' record available in the database')
                    for row in result3:
                        print(row)
                        
            
            else:
                #  performing query for selected date in the data in dataBase
                # Fetch the count of rows from the result
                query2 = f"SELECT COUNT(*) FROM trainingsdb WHERE LOWER({column_name}) = LOWER('{value}' and MONTH(TrainingProgramDate) = {month} AND YEAR(TrainingProgramDate) = {year})"
                self.cursor.execute(query2)
                result2 = self.cursor.fetchall()
                r = len(result2)
                print( f"COUNT of {column} with value {value} : {r}")

                if len(result2) ==0:
                    print("NONE records match!")
                    messagebox.showinfo('Empty Set', 'NO record available in the database')
                else:
                    # Fetch all the rows from the result
                    query3 = f"SELECT * FROM trainingsdb WHERE LOWER({column_name}) = LOWER('{value}' and MONTH(TrainingProgramDate) = {month} AND YEAR(TrainingProgramDate) = {year})"
                    self.cursor.execute(query3)
                    result3 = self.cursor.fetchall()

                    messagebox.showinfo('RESULTS', str(len(result3)) + ' record available in the database')
                    for row in result3:
                        print(row)
                        

                    # # Get the column names
                    # columns2 = [desc[0] for desc in self.cursor.description]
                    # # Combine column names and result rows
                    # rows_with_column_names = [columns2] + list(result2)
                    # # Print the result as a table
                    # for row in rows_with_column_names:
                    #     print("{:<5} {:<5} {:<15} {:<10} {:<10} {:<5} {:<10} {:<10} {:<10} {:<10} {:<15} {:<20} {:<10} {:<5} {:<5}".format(*row))

        except mysql.connector.Error as e:
            print("Error executing the queries:", e)
        except Error as e:
            print("Error executing the search query:", e)
        
        self.cursor.close()
        self.conn.close()
    
    def search_dates(self):

        # Connect to the MySQL database
        self.conn = mysql.connector.connect( host = self.host, user = self.username, password = self.password, database = self.database )
        self.cursor = self.conn.cursor()

        month = self.month_combo.get()
        year = self.year_combo.get()
        print('Searching Trainings for the Date: ',month+'/01/'+year)
    
        if (month == 'month') or (year == 'year'):
            messagebox.showinfo("Select Date", "Choose a Month and Year")
            return 
        try: 
            query = f"SELECT TrainingProgramName FROM trainingsdb WHERE MONTH(TrainingProgramDate) = {month} AND YEAR(TrainingProgramDate) = {year};"
            self.cursor.execute(query)
            result = self.cursor.fetchall()

            if self.cursor.nextset():
                # Move to the next result set and consume any unread result
                pass

            if len(result) == 0:
                messagebox.showinfo('Empty Set','No DATA is available in the selected date!!!')
                print('Empty Set','No DATA is available in the selected date!!!')
            else:
                for row in result:
                    print(row)

            query2 = f"SELECT COUNT(*) FROM trainingsdb WHERE MONTH(TrainingProgramDate) = {month} AND YEAR(TrainingProgramDate) = {year};"
            self.cursor.execute(query2)
            result2 = self.cursor.fetchall()
            print('Total number of trainings: ', result2)
            # for row in results:
            #     print(row)
            # print(results2)            

        except Error as e:
            print("Error searching dates:", str(e))
            messagebox.showerror('Error searching dates:', str(e))

        self.conn.commit()
        self.cursor.close()
        self.conn.close()


    def generate_report():
        pass

    def logout(self):
        self.home_window.destroy()
        self.login_window.deiconify()

    def run(self):
        self.home_window.mainloop()


# Example usage:
if __name__ == "__main__":
    # home_page = HomePage(login_window)
    home_page = HomePage()
    home_page.run()



