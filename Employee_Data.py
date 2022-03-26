import sqlite3

from prettytable import PrettyTable

connection = sqlite3.connect("company.db")

tablelist = connection.execute("select name from sqlite_master where type='table' and name='Employee'").fetchall()

if tablelist != []:

    print("Table already exsist")

else:
    connection.execute(''' Create Table Employee(
                employee_code integer primary key autoincrement,
                employee_name text,
                phone integer,
                email text,
                employee_designation text,
                salary integer,
                company_name text

)''')

print("Employee Table Created Successfully")

while True:
    print("Select an option in an given menu")
    print("1. Add Employee data")
    print("2. View all Employees")
    print("3. Search an Employee using Employee name")
    print("4. Update an Employee details using Employee code")
    print("5. Delete an Employee using Employee code")
    print("6. Display all the details of employees whose salary is greater than 50000")
    print("7. Display the count of total number of Employee in the company")
    print("8. Display all the details in alphabetical order, within the specific salary range")
    print("9. Display all the employees data, whose salary is less than the average salary of all the employees")
    print("10. Exit")

    Choice = int(input("Enter your Choice"))

    if Choice == 1:
        getemployee_name = input("Enter the Employee name:")
        getphone = input("Enter the Employee phone no:")
        getemail = input("Enter the Employee email:")
        getdesignation = input("Enter the Employee designation:")
        getsalary = input("Enter the Employee salary:")
        getcompany_name = input("Enter the Company name:")

        result = connection.execute("insert into Employee(employee_name,phone,email,employee_designation,salary,company_name) values('"+getemployee_name+"',"+getphone+",'"+getemail+"','"+getdesignation+"',"+getsalary+",'"+getcompany_name+"')")

        connection.commit()

        print("Employee data inserted Successfully")

    elif Choice == 2:
        result = connection.execute("select * from Employee")

        table = PrettyTable(["employee_code","employee_name","phone","email","employee_designation","salary","company_name"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])

        print(table)

    elif Choice == 3:
        getemployee_name = input("enter the Employee_name to be search:")

        result = connection.execute("select * from Employee where employee_name= '"+getemployee_name+"'")

        table = PrettyTable(["employee_code","employee_name","phone","email","employee_designation","salary","company_name"])

        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])

        print(table)

    elif Choice == 4:
        getemployee_code = input("Enter the Employee code:")
        getemployee_name = input("Enter the Employee name:")
        getphone = input("Enter the Employee phone no:")
        getemail = input("Enter the Employee email:")
        getdesignation = input("Enter the Employee designation:")
        getsalary = input("Enter the Employee salary:")
        getcompany_name = input("Enter the Company name:")

        result = connection.execute("update Employee set employee_name='"+getemployee_name+"',phone="+getphone+",email='"+getemail+"',employee_designation='"+getdesignation+"',salary="+getsalary+",companyname='"+getcompany_name+"' where employee_code="+getemployee_code+"")
        connection.commit()

        print("Employee data updated successfully")

        result = connection.execute("select * from Employee where employee_code="+getemployee_code+"")

        print("Employee data updated")

    elif Choice == 5:
        getemployee_code = input("enter the Employee code: ")

        connection.execute("delete from Employee where employee_code="+getemployee_code)
        connection.commit()

        print("Employee data deleted successfully")

        result = connection.execute("select * from Employee")

        print("Employee data updated")

        table = PrettyTable(["employee_code","employee_name","phone","email","employee_designation","salary","company_name"])

        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])

        print(table)

    elif Choice == 6:
        result = connection.execute("select * from Employee where salary>(select salary=50000 as salary from Employee)")

        table = PrettyTable(["employee_code","employee_name","phone","email","employee_designation","salary","company_name"])

        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])

        print(table)

    elif Choice == 7:
        result = connection.execute("select count(*) as employee_code from Employee")

        table = PrettyTable(["Employee_count"])

        for i in result:
            table.add_row([i[0]])
        print(table)

    elif Choice == 8:
        lower_range = input("enter the lower range")
        higher_range = input("enter the higher range")
        result = connection.execute("select * from Employee where salary between "+lower_range+" AND "+higher_range+" order by asec")

        table = PrettyTable(["employee_code","employee_name","phone","email","employee_designation","salary","company_name"])

        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])

        print(table)

    elif Choice == 9:
        result = connection.execute("select * from Employee where salary<(select avg(salary) from Employee)")

        table = PrettyTable(["employee_code","employee_name","phone","email","employee_designation","salary","company_name"])

        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])

        print(table)

    elif Choice == 10:
        connection.close()
        break

    else:
        print("Invalid Choice")























