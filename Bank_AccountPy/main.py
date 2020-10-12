import mysql.connector

connect_DB = mysql.connector.connect(user="root", passwd="S@b3d0ri@My5ql", host="localhost")
print(connect_DB)
mycursor = connect_DB.cursor()

# Quick introduction to the program
print("This is a simple Bank Account Model Design in Python.")
print("You will be able to add a new account, make deposit, withdraw money and check balance.")
print("")

# Request for the user's account number and immediate deposit

print("Please follow the options below:")
print("1. Add a new account.")
print("2. Make a deposit.")
print("3. Check balance.")
print("4. Withdraw money.")


def one():
    print("New Account")
    print("Name: ")
    input_name = input("")
    print("Add Account Number: ")
    input_number = int(input(""))
    print("Make a deposit: Y/N")
    input_deposit = input("")

    # Save the details in the database
    sqlFormula = "INSERT INTO Bank_Account.Account_Data (Name, Account_Number) VALUES (%s,%s)"
    data1 = (input_name, input_number)

    mycursor.execute(sqlFormula, data1)  # execute the sql code
    connect_DB.commit()  # Save the details in the database

    # success message
    print("Account Created")
    print("Name: " + input_name)
    print("Account number: " + input_number)

    # update the deposit into the database
    # sort out the deposit thing


def two():
    print("Deposit")
    print("Name: ")
    input_name = input("")
    print("Account Number: ")
    input_number = int(input(""))
    print("How much do you want to deposit?")
    input_deposit = float(input(""))

    # Save the details in the database
    sqlFormula = "SELECT Money FROM `Bank_Account`.`Account_Data` where Name = %s and Account_Number = %s;"
    data1 = (input_name, input_number)

    mycursor.execute(sqlFormula, data1)

    # Get the details from the database
    my_result = mycursor.fetchall()  # get the current money in the account

    for result in my_result:

        result_conversion = float(result[0])  # convert tuple first value to float

        if input_deposit < 0.0:
            print("You cannot deposit more money that your current balance")
        else:
            money_removed = result_conversion + input_deposit  # subtract from the current balance
            print("You deposited: " + str(input_deposit) + " from your account")
            print("Your balance is: " + str(money_removed))

        # Update the new balance into the database


def three():
    print("Balance")
    print("Name: ")
    input_name = (input(""))
    print("Account Number: ")
    input_number = (input(""))

    # Save the details in the database
    sqlFormula = "SELECT Money FROM `Bank_Account`.`Account_Data` where Name = %s and Account_Number = %s;"
    data1 = (input_name, input_number)
    # Save the details in the database
    mycursor.execute(sqlFormula, data1)

    my_result = mycursor.fetchall()  # save and show the changes in the mysql database

    for result in my_result:
        print(result[0])


def four():
    print("Withdraw")
    print("Name: ")
    input_name = input("")
    print("Account Number: ")
    input_number = int(input(""))
    print("How much do you want to withdraw?")
    input_withdraw = float(input(""))

    # Save the details in the database
    sqlFormula = "SELECT Money FROM `Bank_Account`.`Account_Data` where Name = %s and Account_Number = %s;"
    data1 = (input_name, input_number)

    mycursor.execute(sqlFormula, data1)

    # Get the details from the database
    my_result = mycursor.fetchall()  # get the current money in the account

    for result in my_result:

        result_conversion = float(result[0]) # convert tuple first value to float

        if input_withdraw > result_conversion:
            print("You cannot remove more money that your current balance")
        else:
            money_removed = result_conversion - input_withdraw  # subtract from the current balance
            print("You withdrew: " + str(input_withdraw) + " from your account")
            print("Your balance is: " + str(money_removed))

        # Update the new balance into the database


def error_handler():
    return "Invalid Input"


switcher = [one, two, three, four]
print("Enter your option")
options = int(input(""))
switcher = {

    1: one,

    2: two,

    3: three,

    4: four

}

output = switcher.get(options, error_handler)()
print("")
print(output)


connect_DB.close()