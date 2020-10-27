""" Learning Python 01 """


"""
Project 001 - name.py
Proper handling of person names and using a variable for simplicity
"""

# ~ name = "aDA lovelace"

# ~ print(name.title())
# ~ print(name.lower())
# ~ print(name.upper())

# ~ first_name = "ada"
# ~ last_name = "lovelace"
# ~ full_name = first_name + " " + last_name
# ~ print(full_name.title())

# ~ print("Hello, " + full_name.title() + "!")

# ~ message = "Hello, " + full_name.title() + "!"
 
# ~ print(message)


"""
Project 002 - apostrophe.py
Proper handling of strings
"""

# ~ message = "One of Python's strengths is its diverse community."
# ~ print(message)

# single quotes can confuse the compiler
# ~ message = 'One of Python's strengths is its diverse community.'
# ~ print(message)


"""
Project 003 - White_space.py
Proper handling of white space in strings
"""

# ~ print("Python")
 
# ~ print("\tPython")

# ~ print("Languages:\nPython\nC\nJavaScript") 
# ~ print()

# ~ favorite_language = 'python '
# ~ print(favorite_language.rstrip() + favorite_language.rstrip())
# ~ print(favorite_language + favorite_language)

# ~ favorite_language = favorite_language.rstrip()
# ~ print(favorite_language + favorite_language)


# ~ favorite_language = ' python ' 
# ~ print(favorite_language + favorite_language)

# ~ favorite_language = favorite_language.rstrip()
# ~ favorite_language = favorite_language.lstrip()

# ~ print(favorite_language + favorite_language)

# ~ favorite_language = ' python ' 
# ~ print(favorite_language + favorite_language)
# ~ favorite_language = favorite_language.strip()
# ~ print(favorite_language + favorite_language)


"""
Project 004 - bicycles.py
Accessing elements in a list
"""

# ~ #a1 = 'trek'
# ~ #a2 = 'cannondale'
# ~ #a3 = 'redline'
# ~ #a4 = 'specialized'

# ~ bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# ~ #bicycles = ['trek'.title(), 'cannondale'.title(), 'redline'.title(), 'specialized'.title()]
# ~ #bicycles = [a1.title(), a2.title(), a3.title(), a4.title()]
# ~ print(bicycles)
# ~ print()

# ~ print(bicycles[0])      #access the first element in the list
# ~ print(bicycles[0].title())
# ~ print(bicycles[3])
# ~ print(bicycles[-1])     #Access the last item in a list
# ~ print(bicycles[-4])
# ~ #print(bicycles[-5])    #list index out of range, since ther is only 4 elements in the list

# ~ message = "My first bicycle was a " + bicycles[0].title() + "."
# ~ print(message)


"""
Project 005 - motorcycles.py
modifying elements in a list
"""

# ~ #motorcycles = []

# ~ #motorcycles.append('honda')    #append add an element to the end of a list
# ~ #motorcycles.append('yamaha')
# ~ #3motorcycles.append('suzuki') 

# ~ #motorcycles = ['honda', 'yamaha', 'suzuki']
# ~ #print(motorcycles)

# ~ #motorcycles[0] = 'ducati'
# ~ #print(motorcycles)

# ~ #motorcycles.append('ducati')
# ~ #motorcycles.insert(1, 'ducati')    #insert add an element to a list at a specific location (index)
# ~ #print(motorcycles)

# ~ #del motorcycles[0]     #del delete a specific element from a list
# ~ #print(motorcycles)

# ~ #popped_motorcycle = motorcycles.pop()      #pop remove the last element from a list which can be saved to somewhere else if needed
# ~ #print(motorcycles)
# ~ #print(popped_motorcycle)

# ~ #last_owned = motorcycles.pop()
# ~ #print("The last motorcycle I owned was a " + last_owned.title() + ".")
# ~ #motorcycles.append(last_owned)
# ~ #print(motorcycles)

# ~ #first_owned = motorcycles.pop(0)       #pop(0) remove an element by position (index) from a list, which again can be saved to somehere else if needed
# ~ #print('The first motorcycle I owned was a ' + first_owned.title() + '.')
# ~ #motorcycles.insert(0, first_owned)
# ~ #print(motorcycles)

# ~ #print('The first motorcycle I owned was a ' + str(motorcycles[0].title()) + '.')
# ~ #print(motorcycles)

# ~ motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# ~ print(motorcycles)

# ~ #motorcycles.remove('ducati')   #remove an element by value rather than position (index)
# ~ #print(motorcycles)

# ~ too_expensive = 'ducati'
# ~ motorcycles.remove(too_expensive)
# ~ print(motorcycles)
# ~ print("\nA " + too_expensive.title() + " is too expensive for me.")


"""
Project 006 - cars.py
Organizing a list
"""

#cars = ['bmw', 'audi', 'toyota', 'subaru']
#cars.sort()    sort will reorder a list alphabetically
#print(cars)

#car_numbers = [6, 4, 22, 5, 773, 34, -1]
#car_numbers.sort() #Sort work on strings as well as integers
#print(car_numbers)

#cars.sort(reverse=True)    #reverse the sorting
#print(cars)


# ~ cars = ['bmw', 'audi', 'toyota', 'subaru']
# ~ print("Here is the original list:")
# ~ print(cars)

# ~ print("\nHere is the sorted list:")
# ~ print(sorted(cars))     #created a temporary sorted copy of a list

# ~ print("\nHere is the original list again:")
# ~ print(cars)

# ~ cars.reverse()      #reorder a list so it is in reverse order
# ~ print(cars)

# ~ cars.reverse()
# ~ print(cars)

# ~ car_list_lenght = len(cars)     #finds the lenght of a list
# ~ print(car_list_lenght)

# ~ print(len(cars))

# ~ cars = ['audi', 'bmw', 'subaru', 'toyota']

# ~ #for car in cars:    #creates a loop that run though a list and run code for each element in the list
# ~ #    if car == 'bmw':
# ~ #        print(car.upper())
# ~ #    else:
# ~ #        print(car.title())

# ~ car = 'subaru'
# ~ print("Is car == 'subaru'? I predict True.")
# ~ print(car == 'subaru')
# ~ print("\nIs car == 'audi'? I predict False.")
# ~ print(car == 'audi')

# ~ car2 = True
# ~ print("\n" + str(car2))
# ~ print(car2)


"""
Project 007 - magicians.py
Adding more code to a loop
"""

# ~ magicians = ['alice', 'david', 'carolina']
# ~ #for magician in magicians:
# ~ #	print(magician)

# ~ for magician in magicians:
	# ~ print(magician.title() + ", that was a great trick!") 

# ~ for magician in magicians:
	# ~ print("\n" + magician.title() + ", that was a great trick!")
	# ~ print("I can't wait to see your next trick, " + magician.title() + ".")
	
# ~ print("\nThank you, everyone. That was a great magic show!")


"""
Project 008 - numbers.py
Looking a ranges of numbers and how to work with numbers in a list
"""

# ~ #for value in range(1,6):
 # ~ #print(value)

# ~ #for value in range(0,5):
 # ~ #print(value+1)
 
# ~ #numbers = list(range(1,6))
# ~ #print(numbers)

# ~ #numbers = list(range(6))
# ~ #del numbers[0]
# ~ #print(numbers)

# ~ #even_numbers = list(range(2,11,2))
# ~ #print(even_numbers)

# ~ #squares = []
# ~ #for value in range(1,11):
# ~ #	square = value**2       #in python ** represent exponents
# ~ #	squares.append(square)
# ~ #print(squares)

# ~ #for value in range(1,11):
# ~ #	squares.append(value**2)
# ~ #print(squares)

# ~ squares = [value**2 for value in range(1,11)]
# ~ print(squares)

# ~ digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# ~ print(min(digits))  #min finds the smalled number in a list
# ~ print(max(digits))  #max finds the largest number in a list
# ~ print(sum(digits))  #sum finds the sum of all numbers in a list


"""
Project 009 - players.py
slicing a list
"""

# ~ #players = ['charles', 'martina', 'michael', 'florence', 'eli']
# ~ #print(players[0:3])    #players[0:3] create a slice (a copy) of the elements between 0 and 3 (first 3 elements) in a list and output them using the same format as the original list.
# ~ #print(players)         #if no index range was indicated, the entire list is copied. 
# ~ #print(players[1:4])    #a slice can start at any point in the list.
# ~ #print(players[:4])     #if the first index is missing, python start at the first elment in the list.
# ~ #print(players[2:])     #if the second index is missing, python end at the last element in the list.
# ~ #print(players[-3:])    #negative index numbers start counting from the end of the list. In this case, the last 3 elements of the list is sliced. 

# ~ #players = ['charles', 'martina', 'michael', 'florence', 'eli']

# ~ #print("Here are the first three players on my team:")
# ~ #for player in players[:3]:
# ~ #	print(player.title())

# ~ my_foods = ['pizza', 'falafel', 'carrot cake']
# ~ friend_foods = my_foods[:]      #my_foods[:] create a copy of the original list. This avoids saving the same list to two variables. 

# ~ my_foods.append('cannoli')
# ~ friend_foods.append('ice cream')

# ~ print("\nMy favorite foods are:")
# ~ print(my_foods)
# ~ print("\nMy friend's favorite foods are:")
# ~ print(friend_foods)


"""
Project 010 - dimensions.py
looking a tuples (a kind of list, but different)
"""

# ~ dimensions = (200, 50)
# ~ #print(dimensions[0])
# ~ #print(dimensions[1])

# ~ #dimensions[0] = 250    #this assignment fails because an element in a tuple can't be changed. 

# ~ #for dimension in dimensions:
# ~ #   print(dimension)

# ~ print("Original dimensions:")
# ~ for dimension in dimensions:
    # ~ print(dimension)

# ~ dimensions = (400, 100)     #this assignment succeed because it assign a newly crated tuple to the old variable (overwriting the old tuple).
# ~ print("\nModified dimensions:")
# ~ for dimension in dimensions:
    # ~ print(dimension)

"""
Project 011 - voting.py
if is used when you want to run code in the case of a condition being true
"""

# ~ age = 17
# ~ if age >= 18:       #if the conditional statement (age >= 18) is true, then python runs the following code
    # ~ print("You are old enough to vote!")
    # ~ print("Have you registered to vote yet?")
# ~ else:               #else code is run only if the previous if statement was false.
    # ~ print("Sorry, you are too young to voite.")
    # ~ print ("Please register to vote as soon as you turn 18!")

    
"""
Project 012 - amusement_park.py  
elif is used when you only want one block of code to run and there is more than two blocks of code.
"""

# ~ age = 652

# ~ if age <= 4:
    # ~ print("Your admissin ticket is $0.")
# ~ elif age < 18:
    # ~ print("Your admission ticket is $5.")
# ~ else:
    # ~ print("Your admission ticket is $10.")

# ~ if age < 4:
    # ~ price = 0
# ~ elif age < 18:
    # ~ price = 5
# ~ elif age < 65:
    # ~ price = 10
# ~ elif age >= 65:
    # ~ price = 5

# ~ print("Your admission ticket is $" + str(price) + ".")


"""
Project 013 - toppings.py    
A series of if is statements are better when you want to run multiple blocks of code
"""

# ~ requested_toppings = ['mushrooms', 'extra cheese']

# ~ if 'mushrooms' in requested_toppings:
    # ~ print("Adding mushrooms.")
# ~ if 'pepperoni' in requested_toppings:
    # ~ print("Adding pepperoni.")
# ~ if 'extra cheese' in requested_toppings:
    # ~ print("Adding extra cheese.")

# ~ print("\nFinished making your pizza!")

# ~ requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# ~ for requested_topping in requested_toppings:
    # ~ if requested_topping == 'green peppers':
        # ~ print("Sorry, we are out of green peppers right now.")
    # ~ else:
        # ~ print("Adding " + requested_topping + ".")

# ~ print("\nFinished making your pizza!")

# ~ requested_toppings = []

# ~ if requested_toppings:      #test for at least one element in a list
    # ~ for requested_topping in requested_toppings:
        # ~ print("Adding " + requested_topping + ".")
    # ~ print("\nFinished making your pizza!")
# ~ else:
    # ~ print("Are you sure you want a plain pizza?")   

# ~ available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# ~ requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# ~ for requested_topping in requested_toppings:    #in test for an element existing in a list
    # ~ if requested_topping in available_toppings:
        # ~ print("Adding " + requested_topping + ".")
    # ~ else:
        # ~ print("Sorry, we don't have " + requested_topping + ".")

# ~ print("\nFinished making your pizza!")


"""
Project 014 - alien.py
dictionary stuff
"""

# ~ alien_0 = {'color': 'green', 'points': 5, 'color': 'blue'}   #this create a dictionary with key-value pairs inside

# ~ print(alien_0['color'])
# ~ print(alien_0['points'])

# ~ new_points = alien_0['points']

# ~ print("You just earned " + str(new_points) + " points!")

# ~ alien_0 = {'color': 'green', 'points': 5}
# ~ print(alien_0)

# ~ alien_0['x_position'] = 0       #this is how you add new key-value pairs to the dictionary
# ~ alien_0['y_position'] = 25
# ~ #alien_0.append('shiptype': 'falcon')    #this doesn't seem to work with a dictionary

# ~ print(alien_0)

# ~ alien_0 = {}

# ~ alien_0['color'] = 'green'
# ~ alien_0['points'] = 5

# ~ print(alien_0)

# ~ alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

# ~ print("Original x-position: " + str(alien_0['x_position']))

# ~ # Move the alien to the right.
# ~ # Determine how far to move the alien based on its current speed.
# ~ if alien_0['speed'] == 'slow':
    # ~ x_increment = 1
# ~ elif alien_0['speed'] == 'medium':
    # ~ x_increment = 2
# ~ else:
 # ~ # This must be a fast alien.
 # ~ x_increment = 3

# ~ # The new position is the old position plus the increment.
# ~ alien_0['x_position'] = alien_0['x_position'] + x_increment
# ~ print("New x-position: " + str(alien_0['x_position']))

# ~ alien_0 = {'color': 'green', 'points': 5}

# ~ print(alien_0)

# ~ del alien_0['points']   #this is how you remove a key-value pair from a dictionary

# ~ print(alien_0)

""""""

# ~ favorite_languages = {      #you can break down a dictionary over several lines
    # ~ 'jen': 'python',
    # ~ 'sarah': 'c',
    # ~ 'edward': 'ruby',
    # ~ 'phil': 'python',
    # ~ }

# ~ print("Sarah's favorite language is " +     #you can also break up other functions
# ~ favorite_languages['sarah'].title() +
# ~ ".")

# ~ for name, language in favorite_languages.items():
    # ~ print(name.title() + "'s favorite language is " + 
        # ~ language.title() + ".")

# ~ for name in favorite_languages.keys():
    # ~ print(name.title())

# ~ for value in favorite_languages.values():
    # ~ print(value.title())

# ~ #looping through the keys is the default behavior
# ~ for name in favorite_languages:     
    # ~ print(name.title())

# ~ friends = ['phil', 'sarah']
# ~ for name in favorite_languages.keys():
    # ~ print(name.title())

    # ~ if name in friends:
        # ~ print(" Hi " + name.title() + 
            # ~ ", I see that your favorite language is " + 
            # ~ favorite_languages[name].title() + "!")

# ~ if 'erin' not in favorite_languages.keys():
    # ~ print("Erin, please take our poll!")

# ~ #this set up a loop for a temporary sorted version of the dictionary
# ~ for name in sorted(favorite_languages.keys()):
    # ~ print(name.title() + ", thank you for taking the poll.")

# ~ #testing if the dictionary is still the same
# ~ for name in favorite_languages.keys():
    # ~ print(name.title())

# ~ #this goes through every value in the dictionary, even repeating ones.
# ~ print("The following languages have been mentioned:")
# ~ for language in favorite_languages.values():
    # ~ print(language.title())

# ~ #the set() function creates a list with only unique values
# ~ print("The following languages have been mentioned:")
# ~ for language in set(favorite_languages.values()):
    # ~ print(language.title())

""""""

# ~ favorite_languages = {
    # ~ 'jen': ['python', 'ruby'],
    # ~ 'sarah': ['c'],
    # ~ 'edward': ['ruby', 'go'],
    # ~ 'phil': ['python', 'haskell'],
    # ~ }

# ~ for name, languages in favorite_languages.items():
    # ~ print("\n" + name.title() + "'s favorite languages are:")
    # ~ for language in languages:
        # ~ print("\t" + language.title())

"""
Project 015 - user.py
loops and dictionaries
"""

# ~ user_0 = {
    # ~ 'username': 'efermi',
    # ~ 'first': 'enrico',
    # ~ 'last': 'fermi',
    # ~ }  

# ~ for key, value in user_0.items():       #set up a loop for a dictionary
    # ~ print("\nKey: " + key)
    # ~ print("Value: " + value)

"""
Project 016 - aliens.py
Lists and dictionaries
"""

# ~ alien_0 = {'color': 'green', 'points': 5}
# ~ alien_1 = {'color': 'yellow', 'points': 10}
# ~ alien_2 = {'color': 'red', 'points': 15}

# ~ aliens = [alien_0, alien_1, alien_2]

# ~ for alien in aliens:
    # ~ print(alien)

# ~ aliens = []

# ~ #make 30 green aliens.
# ~ for alien_number in range(30):
    # ~ new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    # ~ aliens.append(new_alien)

# ~ #change color, speed and points for the first 3 aliens in the list
# ~ for alien in aliens[0:3]:
    # ~ if alien['color'] == 'green':
        # ~ alien['color'] = 'yellow'
        # ~ alien['speed'] = 'medium'
        # ~ alien['points'] = 10
    # ~ elif alien['color'] == 'yellow':
        # ~ alien['color'] = 'red'
        # ~ alien['speed'] = 'fast'
        # ~ alien['points'] = 15

# ~ #show the first 5 aliens
# ~ for alien in aliens[:5]:
    # ~ print(alien)
# ~ print("...")


# ~ #show how many aliens have been created.
# ~ print("Total amount of aliens: " + str(len(aliens)))


"""
Project 017 - pizza.py
You can nest a list inside a dictionary
"""

# ~ #store information about a pizza being ordered.
# ~ pizza = {
    # ~ 'crust': 'thick',
    # ~ 'toppings': ['mushroom', 'extra cheese'],
    # ~ }

# ~ #Summarize the order.
# ~ print("You ordered a " + pizza['crust'] + "-crust pizza " + 
    # ~ "with the following toppings:")

# ~ for topping in pizza['toppings']:
    # ~ print("\t" + topping)
    

"""
Project 018 - many_users.py
A dictionary in a dictionary
"""

# ~ users = {
    # ~ 'aeinstein': {
        # ~ 'first': 'albert',
        # ~ 'last': 'einstein',
        # ~ 'location': 'princeton',
        # ~ },
    # ~ 'mcurie': {
        # ~ 'first': 'marie',
        # ~ 'last': 'curie',
        # ~ 'location': 'paris',
        # ~ },
    # ~ }

# ~ for username, user_info in users.items():
    # ~ print("\nUsername: " + username)
    # ~ full_name = user_info['first'] + " " + user_info['last']
    # ~ location = user_info['location']
    # ~ print("\tFull name: " + full_name.title())
    # ~ print("\tLocation: " + location.title())


"""
Project 019 - parrot.py
using the input() function
"""

# ~ message = input("Tell me something, and I will repeat it back to you: ")
# ~ print(message)

""" greeter.py """

# ~ name = input("Please enter your name: ")
# ~ print("Hello, " + name + "!")

""""""

# ~ prompt = "If you tell us who you are, we can personalize the messages you see."
# ~ prompt += "\nWhat is your first name? "

# ~ name = input(prompt)
# ~ print("\nHello, " + name + "!")

""" rollercoaster.py """

# ~ height = input("How tall are you, in inches? ")
# ~ height = int(height)

# ~ if height >= 36:
    # ~ print("\nYou're tall enough to ride!")
# ~ else:
    # ~ print("\nYou'll be able to ride when you're a little older.")

""" even_or_odd.py """

# ~ #The modulo operator % gives you the remainder after dividing with a number.
# ~ number = input("Enter a number, and I'll tell you if it's even or odd: ")
# ~ number = int(number)

# ~ if number % 2 == 0:
    # ~ print("\nThe number " + str(number) + " is even.")
# ~ else:
    # ~ print("\nThe number " + str(number) + " is odd.")
    
"""
Project 020 - counting.py
Introducing while loops
"""

# ~ current_number = 1
# ~ while current_number <= 5:
    # ~ print(current_number)
    # ~ current_number += 1

""" parrot.py """

# ~ prompt = "\nTell me something, and I will repeat it back to you:"
# ~ prompt += "\nEnter 'quit' to end the program. "

# ~ message = ""

# ~ while message != 'quit':
    # ~ message = input(prompt)

    # ~ if message != 'quit':
        # ~ print(message)

""" Using a flag """

# ~ prompt = "\nTell me something, and I will repeat it back to you:"
# ~ prompt += "\nEnter 'quit' to end the program. "

# ~ active = True

# ~ while active:
    # ~ message = input(prompt)

    # ~ if message == 'quit':
        # ~ active = False
    # ~ else:
        # ~ print(message)

""" cities.py """

# ~ prompt = "\nPlease enter the name of a city you have visited:"
# ~ prompt += "\n(Enter 'quit' when you are finished.) "

# ~ while True:
    # ~ city = input(prompt)
    
    # ~ if city == 'quit':
        # ~ break
    # ~ else:
        # ~ print("I'd love to go to " + city.title() + "!")

""" counting.py """

# ~ current_number = 0

# ~ while current_number < 10:
    # ~ current_number += 1
    # ~ if current_number % 2 == 0:
        # ~ continue
    
    # ~ print(current_number)

""" avoiding infinite loops """

# ~ x = 1

# ~ while x <= 5:
    # ~ print(x)
    # ~ x += 1  #leaving this out would create an infinite loop

""" Using a while loop with lists and dictionaries """

# ~ # Start with users that need to be verified, 
# ~ #  and an empty list to hold confirmed users.
# ~ unconfirmed_users = ['alice', 'brian', 'candace']
# ~ confirmed_users = []

# ~ # Verify each user until there are no more unconfirmed users.
# ~ # Move each verified user into the list of confirmed users.
# ~ while unconfirmed_users:
    # ~ current_user = unconfirmed_users.pop()
    
    # ~ print("Verified user: " + current_user.title())
    # ~ confirmed_users.append(current_user)
    
# ~ # Display all confirmed users.
# ~ print("\nThe following users have been confirmed:")
# ~ for confirmed_user in confirmed_users:
    # ~ print(confirmed_user.title())

""" pets.py - removing all instances of specific values from a list """

# ~ pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# ~ print(pets)

# ~ while 'cat' in pets:
    # ~ pets.remove('cat')

# ~ print(pets)

""" Filling a dictionary with user input """

# ~ responses = {}

# ~ # Set a flag to indicate that polling is active.
# ~ polling_active = True

# ~ while polling_active:
    # ~ # Prompt for the person's name and response.
    # ~ name = input("\nWhat is your name? ")
    # ~ response = input("Which mountain would you like to climb someday? ")
    
    # ~ # Store the response in the dictionary:
    # ~ responses[name] = response
    
    # ~ # Find out if anyone else is going to take the poll.
    # ~ repeat = input("Would you like to let another person respond? (yes/ no) ")
    # ~ if repeat == 'no':
        # ~ polling_active = False

# ~ # Polling is complete. Show the results.
# ~ print("\n--- Poll Results ---")
# ~ for name, response in responses.items():
    # ~ print(name + " would like to climb " + response + ".")


"""
Project 021 - Functions
"""

""" greeter """

# ~ def greet_user():
    # ~ """Display a simple greeting"""
    # ~ print("Hello")

# ~ greet_user()

""" Passing Information to a Function """

# ~ def greet_user(username):
    # ~ """Display a simple greeting."""
    # ~ print("Hello, " + username.title() + "!")

# ~ greet_user('jesse')

""" Passing arguments, Positional arguments """

# ~ def describe_pet(animal_type, pet_name):
    # ~ """Display information about a pet."""
    # ~ print("\nI have a " + animal_type + ".")
    # ~ print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# ~ describe_pet('hamster', 'harry')

""" Multiple Function Calls """

# ~ def describe_pet(animal_type, pet_name):
    # ~ """Display information about a pet."""
    # ~ print("\nI have a " + animal_type + ".")
    # ~ print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# ~ describe_pet('hamster', 'harry')
# ~ describe_pet('dog', 'willie')

""" Keyword arguments """

# ~ def describe_pet(animal_type, pet_name):
    # ~ """Display information about a pet."""
    # ~ print("\nI have a " + animal_type + ".")
    # ~ print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# ~ describe_pet(animal_type='hamster', pet_name='harry')
# ~ describe_pet(pet_name='harry', animal_type='hamster')

""" Default values """

# ~ def describe_pet(pet_name, animal_type='dog'):
    # ~ """Display information about a pet."""
    # ~ print("\nI have a " + animal_type + ".")
    # ~ print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# ~ #this is still technically a positional argument
# ~ describe_pet(pet_name='willie')

""" Return values """

# ~ def get_formatted_name(first_name, last_name):
    # ~ """Return a full name, neatly formatted."""
    # ~ full_name = first_name + ' ' + last_name
    # ~ return full_name.title()
    
# ~ musician = get_formatted_name('jimi', 'hendrix')
# ~ print(musician)

""" Making an argument optional """

# ~ def get_formatted_name(first_name, last_name, middle_name=''):
    # ~ if middle_name:
        # ~ full_name = first_name + ' ' + middle_name + ' ' + last_name
    # ~ else:
        # ~ full_name = first_name + ' ' + last_name
    # ~ return full_name.title()

# ~ musician = get_formatted_name('jimi', 'hendrix')
# ~ print(musician)

# ~ musician = get_formatted_name('john', 'hooker', 'lee')
# ~ print(musician)

""" Returning a dictionary """

# ~ def build_person(first_name, last_name, age=''):
    # ~ """Return a dictionary of information about a person."""
    # ~ person = {'first': first_name, 'last': last_name}
    # ~ if age:
        # ~ person['age'] = age
    # ~ return person
    
# ~ musician = build_person('jimi', 'hendrix', age=27)
# ~ print(musician)

""" Using functions with while loops """


# ~ def get_formatted_name(first_name, last_name):
    # ~ """Return a full name, neatly formatted."""
    # ~ full_name = first_name + ' ' + last_name
    # ~ return full_name.title()

# ~ # This is an infinite loop!
# ~ while True:
    # ~ print("\nPlease tell me your name:")
    # ~ print("(enter 'q' at any time to quit)")
    # ~ f_name = input("First name: ")
    # ~ if f_name == 'q':
        # ~ break
    # ~ l_name = input("Last name: ")
    # ~ if l_name == 'q':
        # ~ break
    
    # ~ formatted_name = get_formatted_name(f_name, l_name)
    # ~ print("\nHello, " + formatted_name + "!")

""" Passing a list """

# ~ def greet_users(names):
    # ~ """Print a simple greeting to each user in the list."""
    # ~ for name in names:
        # ~ msg = "Hello, " + name.title() + "!"
        # ~ print(msg)
    
# ~ usernames = ['hannah', 'ty', 'margot']
# ~ greet_users(usernames)

""" Modifying a list in a function """

# ~ unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# ~ completed_models =  []

# ~ while unprinted_designs:
    # ~ current_design = unprinted_designs.pop()
    # ~ print("Printing model: " + current_design)
    # ~ completed_models.append(current_design)

# ~ print("\nThe following models have been printed:")
# ~ for completed_model in completed_models:
    # ~ print(completed_model)

# ~ unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# ~ completed_models =  []

# ~ def print_models(unprinted_designs, completed_models):
    # ~ while unprinted_designs:
        # ~ current_design = unprinted_designs.pop()
        # ~ print("Printing model: " + current_design)
        # ~ completed_models.append(current_design)

# ~ def show_completed_models(completed_models):
    # ~ print("\nThe following models have been printed:")
    # ~ for completed_model in completed_models:
        # ~ print(completed_model)
        
# ~ print_models(unprinted_designs, completed_models)
# ~ show_completed_models(completed_models)

""" Preventing a function from modifying a list """

# ~ # You can send a copy of a list to a function
# ~ function_name(list_name[:])

""" Passing an arbitrary number of arguments """

# ~ def make_pizza(*toppings):
    # ~ """Summarize the pizza we are about to make."""
    # ~ print("\nMaking a pizza with the following toppings:")
    # ~ for topping in toppings:
        # ~ print("- " + topping)

# ~ make_pizza('pepperoni')
# ~ make_pizza('mushrooms', 'green peppers', 'extra cheese')

""" Mixing positional and arbitrary arguments """

