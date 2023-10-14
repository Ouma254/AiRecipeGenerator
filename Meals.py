class Meals:
    def preferred_meals(self):
        print("Menu Items")
        global prefer_for_dishes
        prefer_for_dishes = {
            'No.': '   ITEMS        PRICE',
            '1.': ' Rice-Dengu  -ksh. 150/=',
            '2.': ' Ugali-Beef      -ksh. 500/=',
            '3.': ' Rice-Fish       -ksh. 400/=',
            '4.': ' Ugali-Fish      -ksh. 700/=',
            '5.': ' Ugali-Cabbage   -ksh. 150/=',
            '6.': ' Rice-Fish-Cab   -ksh. 600/=',
            '7.': ' Rice-Beef       -ksh. 650/='
        }
        print(f"\n {prefer_for_dishes}\n")

    def ordered_meals(self):
        global user_orders
        user_orders = input("Please Make your order of meals")
        orders_made = [user_orders]
        print(f"Orders {orders_made}")

    def pay_for_order(self):
        while True:
            print("\nOptions: ")
            print("1. M-pesa payment ")
            print("2. Display the total bill && Pay")
            print("q. Exit")

            choice_inputs = input("Select one: \n")

            if choice_inputs == '1':
                meals.mpesa_payment()
            elif choice_inputs == '2':
                meals.ordered_meals()
                meals.total_bill()
            elif choice_inputs == 'q':
                print("Process Finished Successfully")
                break
            else:
                print("Invalid Choice")

    def mpesa_payment(self):
        print("Service Unavailable Currently!!")
        print("Try again later")

    def total_bill(self):
        payment_menu = {
            'break_fast': [
                "tea-bread : ksh.60 ",
                "tea-chapati : ksh.70 ",
                "Tea-mandazi : ksh.50 ",
                "Tea : ksh.30 "
            ],
            'lunch': [
                "Ugali-Cabbage : ksh. 150 ",
                "Ugali-Beef : ksh.600 "
                "ugali-fiah ksh.500 ",
                "Rice-Ndengu ksh.150 ",
                "Rice-Fish-Cabbage ksh.450 ",
                "Rice-Beef ksh.400"
            ]
        }







meals = Meals()
meals.ordered_meals()
