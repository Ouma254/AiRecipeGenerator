from Recipe import Recipe


class Account(Recipe):
    # the class attributes and constructor
    # def __init__(self,username, password, status, order):
    #     self.username = username
    #     self.password = password
    #     self.status = status
    #     self.order = order

    # the class functions
    def login(self):
        counts = 3
        trials = 0
        attempts = 0
        password = "ai_driven"
        user_password = ""

        print(">>>....AI Driven Recipe Generator....<<<<")
        print("               WELCOME          ")
        print("Please input your login Details")

        #check on user input credentails
        while attempts < 3:
            name = input("USERNAME: ")
            password_input = input("Enter password:  ")
            if password_input == password:
                print("login successful!!")
                account.menu_of_foodstuff()
                break

            if user_password != password:
                counts -= 1
                print(f"Incorrect password. You have {counts} attempts remaining")
        if trials == attempts:
            print(f"Login Fails ")

        # the user inputs the login credentails


account = Account()
account.login()