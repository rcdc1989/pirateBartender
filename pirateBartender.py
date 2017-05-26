# Pirate Bartender: Challenges

# Raphael Capon
# 2017-05-26

# a set of functions to gather user input on taste preference
# based on a set of questions
# we then use a set of ingredients (which matches question list) to generate
# a "drink" 

# we also generate a drink name according to a predetermined format,
# to do this, we use pre-populated lists of nouns and verbs as well as
# existing ingredient preference information

import random #for use in assigning ingredients

def get_input():
    """takes dict of questions returns dict of T/F based on used input"""
    
    #GIVEN DATA:
    #for simplicity, we populate our dictionary here
    #it might be better to create a class which helps with this
    questions = {
        "strong": "Do ye like yer drinks strong?",
        "salty": "Do ye like it with a salty tang?",
        "bitter": "Are ye a lubber who likes it bitter?",
        "sweet": "Would ye like a bit of sweetness with yer poison?",
        "fruity": "Are ye one for a fruity finish?",
        }
    
    drink_data = {}
    user_input = ""
    
    for entry in questions.keys(): #Loop through questions
        
        #continue asking until appropriate input is given
        while user_input != 'yes' and user_input !='no': 
            user_input = input(questions[entry] + " (enter yes or no) ") 
        
        #fill in the userInput dictionary with new information
        if user_input == "yes":
            drink_data[entry] = True
            
        else:
            drink_data[entry] = False
            
        user_input = "" #reset user input, so we don't skip the while loop

    return drink_data
    
def mix_drink(drink_data):
    """takes dict of user data and dict of ingredients
    returns a list of drink ingredients"""
   
    #GIVEN DATA:
    #for simplicity, we populate our dictionary here
    #it might be better to create a class which helps with this 
    ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
    }
    
    drink = []
    
    for entry in drink_data.keys(): #loop through drink "characteristics"
        
        if drink_data[entry] : #if that characteristic has "true" then...
            drink.append(random.choice(ingredients[entry]))  
            #we randomly select and ingredient from appropriate ingredients list
            
    return drink
    
def name_drink(drink_data,drink):
    """takes dict of T/F statements for "flavours" based on user input
    as well as a number of drink ingredients and returns a funny (?)
    drink name with the following structure:
            Flavour Noun Verb "with" Ingredient    
    """
    
    nouns = ["spelunker","assailant","hobgoblin",
             "barrel","ski-doo","cosmetics salesperson"]
    verbs = ["hopper","mesmerizer","annoyer",
             "patronizer","complainer","grabber",
             "destroyer","evaporator"]
    
    # we assign a random selection of words to
    flavour = ""
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    ingredient = random.choice(drink)
    
    while flavour == "":
    
        flavour = random.choice(list(drink_data.keys()))
        
        if drink_data[flavour] == False:
            
            flavour = ""
            
    return flavour + " " + noun+ " " + verb + " with a " + ingredient
    
    
#execute when the program is run from the command line,    
if __name__ == '__main__':
    
    bar_open = True
    customers = {"Salty Bob":{"strong": False,
                              "salty": True,
                              "bitter": False,
                              "sweet": False,
                              "fruity": False}
                }
    inventory = {"glug of rum":2, "slug of whisky":2, "splash of gin":2,
                 "olive on a stick":2, "salt-dusted rim":2, "rasher of bacon":2,
                 "shake of bitters":2, "splash of tonic":2, "twist of lemon peel":2,
                 "sugar cube":2, "spoonful of honey":2, "spash of cola":2,
                 "slice of orange":2, "dash of cassis":2, "cherry on top":2,
                 }
    
    while bar_open == True: #keep looping until user decides to quit
        
        #identify customer:
        customer_name = input("Hi matey, what's yer name?")
        if customer_name in customers:#check if customer is in database
            #if customer is found, extract drink preference
            print("Didn't you drink yer fill last time, " + customer_name + "?")
            choices = customers[customer_name]
            
        else:
            #if customer does not exist, we create a new entry and
            #get user input
            print("'ello poppet! \n")
            choices = get_input()
            customers[customer_name] = choices
        
        #continue generating drinks with the same choices if
        #user is "still thirsty"
        thirsty = True #reset "thirsty" from previous run-through
        while thirsty == True  :
        
            drink = mix_drink(choices)
            
            for ingredient in drink:
                
                if inventory[ingredient] > 0:
                    
                    inventory[ingredient] = inventory[ingredient] - 1 
                
                else:
                    
                    print("\nYARR! \n looks like we ran out of " + ingredient +
                          " I'll go pillage some more\n...\n...\n")
                    inventory[ingredient] = inventory[ingredient] + 2 
                            
            drink_name = name_drink(choices,drink)
            print("arg! enjoy your \n" + '"' + drink_name +'"')
            print("contains: " + str(drink) + "\n")
            
            #ask for and check user input before looping again
            if input("are ye still thirsty? (yes or no) ") != "yes": 
                
                thirsty = False
                print("Alrighty, don't get lost at sea now!")
                
            else:
                
                print("OK, another coming right up!")
                
        if input("\n YAARR I can't read...is this bar still open?" +
                 "(yes or no)") != "yes":
            bar_open = False
            
# this is the main function I used for initial testing:    
# def main():
    
#      test_input = get_input(questions)
#      print (test_input)
     
#      print("lol")
    
#      test_drink = mix_drink(test_input,ingredients)
#      print(test_drink)
     
#      test_drink_name = name_drink(test_input,test_drink)
#      print(test_drink_name)




