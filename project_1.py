import tkinter as tk
import os
from time import sleep

window = tk.Tk()

window.title("Bank")

window.geometry("400x480+300+200")

window.resizable(False, False)

framecolor = "gray"

cerceve = tk.Frame(window, bg=framecolor)
cerceve.pack()
cerceve.place(relwidth=1, relheight=1)


def registerScreen():
    screen = tk.Tk()

    screen.title("Register Screen")

    screen.geometry("400x480+300+200")

    screen.resizable(False, False)

    framecolor = "gray"

    cerceve = tk.Frame(screen, bg=framecolor)
    cerceve.pack()
    cerceve.place(relwidth=1, relheight=1)

    registerFrame = tk.Frame(screen, bg=framecolor)
    registerFrame.place(x=100, y=120)

    name_var = tk.StringVar()
    pass_var = tk.StringVar()

    tk.Label(registerFrame, text="Full Name", font=("Goudy old style ", 15, "bold"), fg="orange", bg=framecolor).pack()
    user_entry = tk.Entry(registerFrame, textvariable=name_var, font=("Times new roman", 15), bg="lightgray")
    user_entry.pack()

    tk.Label(registerFrame, text="Password", font=("Goudy old style ", 15, "bold"), fg="orange", bg=framecolor).pack()
    user_pass = tk.Entry(registerFrame, textvariable=pass_var, font=("Times new roman", 15), bg="lightgray", show="*")
    user_pass.pack()

    def regDeny():
        tk.Label(registerFrame, text="User Already exists", font=("Goudy old style ", 15, "bold"), fg="red",
                 bg=framecolor).pack()

    def regConf():
        tk.Label(registerFrame, text="Register Success", font=("Goudy old style ", 15, "bold"), fg="green",
                 bg=framecolor).pack()

    def registerUser():

        initialBalance = 50
        user_NameInfo = user_entry.get()
        user_PassInfo = user_pass.get()

        list_of_pass = os.listdir()
        if user_NameInfo in list_of_pass:
            regDeny()

        elif user_NameInfo in list_of_pass:
            registerFile = open(user_NameInfo, "r")
            confirmreg = registerFile.read().splitlines()
            if user_PassInfo in confirmreg:
                regDeny()

        else:
            registerFile = open(user_NameInfo, "w")
            registerFile.write(user_NameInfo + "\n")
            # registerFile.write(" ")
            registerFile.write(user_PassInfo)
            registerFile.close()

            balanceFile = open(user_NameInfo + "Balance", "w")
            balanceFile.write(str(initialBalance))
            balanceFile.close()

            user_entry.delete(0, tk.END)
            user_pass.delete(0, tk.END)
            regConf()
            # sleep(1.5)

    registerButton = tk.Button(registerFrame, text="Register", bg=framecolor, fg="orange", font=("Goudy old style", 15),
                               activebackground="coral", command=registerUser)
    registerButton.pack(pady=35)

    screen.mainloop()


def loginScreen():
    screen = tk.Tk()

    screen.title("Login Screen")

    screen.geometry("400x480+300+200")

    screen.resizable(False, False)

    framecolor = "gray"

    cerceve = tk.Frame(screen, bg=framecolor)
    cerceve.pack()
    cerceve.place(relwidth=1, relheight=1)

    loginFrame = tk.Frame(screen, bg=framecolor)
    loginFrame.place(x=100, y=120)

    name = tk.StringVar()
    passw = tk.StringVar()

    def login_success():
        tk.Label(loginFrame, text="Login Success", font=("Goudy old style ", 15, "bold"), fg="lightgreen",
                 bg=framecolor).pack()

    def password_not_recognized():
        message = tk.Label(loginFrame, text="Incorrect Password", font=("Goudy old style ", 15, "bold"), fg="red",
                           bg=framecolor).pack()

    def user_not_found():
        message = tk.Label(loginFrame, text="User Not Found", font=("Goudy old style ", 15, "bold"), fg="red",
                           bg=framecolor).pack()

    tk.Label(loginFrame, text="Full Name", font=("Goudy old style ", 15, "bold"), fg="orange", bg=framecolor).pack()
    user_entry = tk.Entry(loginFrame, textvariable=name, font=("Times new roman", 15), bg="lightgray")
    user_entry.pack()

    tk.Label(loginFrame, text="Password", font=("Goudy old style ", 15, "bold"), fg="orange", bg=framecolor).pack()
    user_pass = tk.Entry(loginFrame, textvariable=passw, font=("Times new roman", 15), bg="lightgray", show="*")
    user_pass.pack()

    def loginUser():

        verifyUserName = user_entry.get()
        verifyPassw = user_pass.get()

        def withdrawConfirmation():

            withdraw = tk.Tk()

            withdraw.title("Withdraw Menu")

            withdraw.geometry("400x480+300+200")

            withdraw.resizable(False, False)

            framecolor = "gray"

            cerceve = tk.Frame(withdraw, bg=framecolor)
            cerceve.pack()
            cerceve.place(relwidth=1, relheight=1)

            withdrawFrame = tk.Frame(withdraw, bg=framecolor)
            withdrawFrame.place(x=100, y=120)

            # name = tk.StringVar()
            amount = tk.StringVar()

            def withdraw_success():
                tk.Label(withdrawFrame, text="CONFIRM", font=("Goudy old style ", 15, "bold"), fg="lightgreen",
                         bg=framecolor).pack()

            def withdraw_deny():
                tk.Label(withdrawFrame, text="DENY", font=("Goudy old style ", 15, "bold"), fg="red",
                         bg=framecolor).pack()

            # tk.Label(loginFrame, text = "Full Name", font = ("Goudy old style ", 15, "bold"), fg = "orange", bg = framecolor).pack()
            # user_entry =  tk.Entry(loginFrame, textvariable = name,font = ("Times new roman", 15), bg = "lightgray")
            # user_entry.pack()

            tk.Label(withdrawFrame, text="Amount", font=("Goudy old style ", 15, "bold"), fg="orange",
                     bg=framecolor).pack()
            user_amount = tk.Entry(withdrawFrame, textvariable=amount, font=("Times new roman", 15), bg="lightgray")
            user_amount.pack()

            def withdraw():
                amount = int(user_amount.get())
                print(amount)
                currentBalanceFile = open(verifyUserName + "Balance", "r")
                balance = currentBalanceFile.read()
                currentBalanceFile.close()
                if int(balance) < amount:
                    withdraw_deny()
                else:
                    # currentBalanceFile.close()
                    currentBalanceFile = open(verifyUserName + "Balance", "w")
                    new = int(balance) - int(amount)
                    currentBalanceFile.write(str(new))
                    currentBalanceFile.close()
                    withdraw_success()

                    

            withDrawConf = tk.Button(withdrawFrame, text="Withdraw", bg=framecolor, fg="orange",
                                     font=("Goudy old style", 15), activebackground="coral", command=withdraw)
            withDrawConf.pack(pady=50)

        list_of_balance = os.listdir()
        if verifyUserName + "Balance" in list_of_balance:
            currentBalanceFile = open(verifyUserName + "Balance", "r")
            currentBalance = currentBalanceFile.read()
            currentBalanceFile.close()
        user_entry.delete(0, tk.END)
        user_pass.delete(0, tk.END)

        list_of_users = os.listdir()
        if verifyUserName in list_of_users:
            loginFile = open(verifyUserName, "r")
            confirm = loginFile.read().splitlines()
            if verifyPassw in confirm:
                login_success()
                window.destroy()
                screen.destroy()

                def main():
                    root = tk.Tk()

                    root.title("GUI")

                    root.geometry("400x480+300+200")

                    root.resizable(False, False)

                    framecolor = "gray"

                    cerceve = tk.Frame(root, bg=framecolor)
                    cerceve.pack()
                    cerceve.place(relwidth=1, relheight=1)

                    # "Account: Bora Kaplan \n \n Account ID: 2452 \n \n Balance: 86592"

                    def AccInfoPrinter():
                        info = tk.Frame(root, borderwidth=0, height=500, width=500)
                        info.place(relx=0.252, rely=0.121, anchor="n")
                        tk.Label(info,
                                 text="Account: " + verifyUserName + "\n \n" + "Account ID: " + "ID" + "\n \n" + "Balance: " + currentBalance,
                                 bg=framecolor, fg="orange", font=("Arial", 13)).pack()

                    for row in range(2):
                        for column in range(2):
                            canvas = tk.Canvas(root, bg=framecolor, height=229, width=188)
                            canvas.grid(row=row, column=column, padx=4, pady=4)
                            AccInfoPrinter()

                    withdrawButton = tk.Button(root, text="Withdraw", command=withdrawConfirmation,
                                               activeforeground="green", activebackground="lightgreen", width=12,
                                               height=4)
                    withdrawButton.grid(row=1, column=1)

                    def depositConfirmation():
                        tk.messagebox.showinfo("Bora Bank", "Your deposit has been confirmed")

                    depositButton = tk.Button(root, text="Deposit", command=depositConfirmation,
                                              activeforeground="green", activebackground="lightgreen", width=12,
                                              height=4)
                    depositButton.grid(row=1, column=0)

                    root.mainloop()

                main()




            else:
                password_not_recognized()


        else:
            user_not_found()

    loginButton = tk.Button(loginFrame, text="Login", bg=framecolor, fg="orange", font=("Goudy old style", 15),
                            activebackground="coral", command=loginUser)
    loginButton.pack(pady=35)

    screen.mainloop()


def login():
    tk.messagebox.showinfo("Bora Bank", "Login Confirmed")


def register():
    tk.messagebox.showinfo("Bora Bank", "Your register has been confirmed")


def welcome():
    welcome = tk.Frame(window, borderwidth=0, height=500, width=500)
    welcome.place(relx=0.5, rely=0.1, anchor="n")
    tk.Label(welcome, text="Welcome To Bank", bg=framecolor, fg="pink", font=("Arial", 20)).pack()


for row in range(2):
    for column in range(2):
        canvas = tk.Canvas(window, bg=framecolor, height=234, width=194, borderwidth=1, highlightthickness=0)
        canvas.grid(row=row, column=column, padx=1, pady=1)
        welcome()

loginButton = tk.Button(window, text="Login", command=loginScreen, activeforeground="green",
                        activebackground="lightgreen", width=12, height=4)
loginButton.grid(row=1, column=1)

registerButton = tk.Button(window, text="Register", command=registerScreen, activeforeground="green",
                           activebackground="lightgreen", width=12, height=4)
registerButton.grid(row=1, column=0)

window.mainloop()


