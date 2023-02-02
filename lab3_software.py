import pandas as pd


class Employee:
    def _init_(self, employeeid, name, age, salary, df):
        self.employeeid = employeeid
        self.name = name
        self.age = age
        self.salary = salary
        self.df = df

    def update_table(self, i):
        data = {
            "Employee ID": [self.employeeid],
            "Name": [self.name],
            "Age": [self.age],
            "Salary(PM)": [self.salary]
        }
        self.df = pd.DataFrame(data)
        for j in range(i-1):
            Employeeid = input("Enter Employee ID:")
            Name = input("Enter Name:")
            Age = int(input("Enter Age:"))
            Salary = int(input("Enter Salary:"))
            data2 = {
                "Employee ID": [Employeeid],
                "Name": [Name],
                "Age": [Age],
                "Salary(PM)": [Salary]
            }
            df2 = pd.DataFrame(data2)
            self.df = pd.concat([self.df, df2])
        return self.df

    def sort_age(self):
        self.sdf = self.df.sort_values(by=["Age"], ascending=True)
        return self.sdf

    def sort_name(self):
        self.sdf = self.df.sort_values(by=["Name"], ascending=True)
        return self.sdf

    def sort_salary(self):
        self.sdf = self.df.sort_values(by=["Salary(PM)"], ascending=True)
        return self.sdf


Employeeid = input("Enter Employee ID:")
Name = input("Enter Name:")
Age = int(input("Enter Age:"))
Salary = int(input("Enter Salary:"))
ob = Employee(Employeeid, Name, Age, Salary, None)
print(ob.update_table(5))
print("\n")

choice = 1

while choice:
    print("0. Exit")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print(ob.sort_age())
    elif choice == 2:
        print(ob.sort_name())
    elif choice == 3:
        print(ob.sort_salary())
    elif choice == 0:
        print("Exiting")
    else:
        print("Invalid Option")

# ob = Employee("161E90","Raman",41,56000)
# ob = Employee("161F91", "Himandri", 38, 67500)
# ob = Employee("161F99", "Jaya", 51, 82100)
# ob = Employee("171E20", "Tejas", 30, 55000)
# ob = Employee("171G30", "Ajay", 45, 44000)