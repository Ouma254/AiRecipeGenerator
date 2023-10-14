class Recipe:
    def menu_of_foodstuff(self):
        print("...Welcome to AI Driven Recipe Generator...")
        # this function displays a list of meals the recipes are available
        list_of_meals = ['Ugali', 'Rice', 'Meat', 'Porridge', 'Tomatoes', 'Pizza']
        print("\n LIST OF THE AVAILABLE FOODS YOU HAVE THEIR RECIPES:")
        print(f"\n FOODS: \n{list_of_meals}")

        while True:
            print("\nOptions :")
            print("1. Ugali")
            print("2. Rice")
            print("3. Meat")
            print("4. Porridge")
            print("5. Tomatoes")
            print("6. Tea")
            print("0. Quit")


            # the user choice
            user_choice = input("Enter the name of the meal to get its recipe: ")

            if user_choice == 'Ugali' or user_choice == 'ugali':
                recipe.ugali_steps()
            elif user_choice == 'Rice' or user_choice == 'rice':
                recipe.rice_steps()
            elif user_choice == 'Meat' or user_choice == 'meat':
                recipe.meat_steps()
            elif user_choice == 'Porridge' or user_choice == 'porridge':
                recipe.porridge_steps()
            elif user_choice == 'Tomatoes' or user_choice == 'tomatoes':
                recipe.tomatoes_steps()
            elif user_choice == 'Pizza' or user_choice == 'pizza':
                recipe.tea_steps()
            elif user_choice == 'Quit' or user_choice == 'quit':
                print("THANK YOU FOR USING AI RECIPE GENERATOR")
                break
            else:
                print("Error Invalid Choice!!")

    def ugali_steps(self):
        print("Ugali preparation steps:")
        steps_for_ugali = {
            '1. ': 'Add 2 500ml cups full of water to a clean sufuria',
            '2. ': 'Place the Sufuria on Fire',
            '3. ': 'Let the boil for 10 minutes',
            '4. ': 'Add enough floor on the boiling water',
            '5. ': 'Stir the mixture until it becomes firm',
            '6. ': 'Let mix on fire for few seconds to harden',
            '7. ': 'Remove the Ugali from fire and put on the serving bowl',
            '8. ': 'Your Ugali is ready for serving'
        }
        print(f"\n {steps_for_ugali}")
        print("Do you enjoy using AI Recipe")

    def rice_steps(self):
        print("Hi, Let me help you prepare some rice")
        steps_for_rice = {
            '1. ': 'Add 2 500ml cup of water in a Sufuria',
            '2. ': 'Boil the Water a while',
            '3. ': 'Rinse the clean the Rice with clean water',
            '4. ': 'Add the Salt, Oil to the Water',
            '5. ': 'Add any other ingredients of your choice to water for flavors',
            '6. ': 'Add Rice to Water and Let it boil with the water',
            '7. ': '10 - 15 minutes will be enough for the rice to boil and be ready to serve',
            '8. ': 'Rice is ready for serving'
        }
        print(f"\n {steps_for_rice}")
        print("Thank you choosing AI Recipe")

    #     meat preparation
    def meat_steps(self):
        print("Welcome, Let Prepare Meat")
        steps_meat = {
            'a.': 'Wash the meat ',
            'b.': 'Let the meat boil for the 15 minutes',
            'c.': 'Rinse the meat',
            'd.': 'Add Oil to the Cooking Pot',
            'e.': 'In the boiling oil, add onions, Tomatoes',
            'f.': 'Stir the mixture Until red mixture forms',
            'g.': 'Add boiled Meat to the mixture and keep stirring',
            'h.': 'Add half full cup of water and let it boil for 10 minutes',
            'i.': 'Remove the pot from fire ',
            'j.': 'Meat is ready for serve'
        }

        print(f"\n {steps_meat}")
        print("Thank you for Choosing AI Recipe")

    def porridge_steps(self):
        print("Let's prepare some Porridge")

        steps_for_porridge = {
            'a.': 'Add 2 cups of Water to Cooking Pot',
            'b.': 'Heat the water Till it boils',
            'c.': 'Using another pot prepare a solution of floor and cold water',
            'd.': 'Add the solution mixture to the boiling water',
            'e.': 'Stir the mixture to form a uniform mixture ',
            'f.': 'Let the mixture heat and boil',
            'g.': 'Remove form the fire and let it cool abit',
            'h.': 'Porridge is ready for serving'
        }

        print(f"\n {steps_for_porridge}")
        print("Let's Serve Porridge")

    def tomatoes_steps(self):
        print("Prepare Tomatoes")
        steps_for_tomatoes = {
            '1.': 'Chop the tomatoes',
            '2.': 'Wash and Clean the Tomatoes',
            '3.': 'Add correct amount of Oil to the Cooking Pot',
            '4.': 'Add the Tomatoes to the Oil and let it boil',
            '5.': 'As the tomatoes the changes Brown remove from the oil',
            '6.': 'Tomatoes are now ready for serve'
        }
        print(f"\n {steps_for_tomatoes}")
        print("Lets Eat some Tomatoes together")

    def tea_steps(self):
        print("Lets Prepare some Tea(Strong): ")
        steps_tea = {
            'a.': 'Add the Correct Amount of Water in Cooking Pot',
            'b.': 'Add tea leaves to the water',
            'c.': 'Let the mixture heat to boil',
            'd.': 'Filter-out the tea leaves from the boiled mixture',
            'e.': 'Add Sugar to the Tea',
            'f.': 'Tea is read for Serving'
        }

        print(f"\n {steps_tea}")
        print("Hot tea is cool")








recipe = Recipe()