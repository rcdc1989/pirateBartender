# Pirate Bartender: Challenges

# Raphael Capon
# 2017-05-26

# a set of functions to gather user input
# based on a set of questions
# we then use a set of ingredients to output
# a "drink" which assigns ingredients based on input

import random #for use in assigning ingredients

#GIVEN DATA:
#for simplicity, we populate our dictionaries here
#it might be better to create a class which helps with this
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}
    
def get_input(questions):
    """takes dict of questions returns dict of T/F based on used input"""  
    
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
    
def mix_drink(drink_data, ingredients):
    """takes dict of user data and dict of ingredients
    returns a list of drink ingredients"""
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
            
    return flavour + " " + noun+ " " + verb + " with " + ingredient
    
if __name__ == '__main__':
    
    thirsty = True
    
    while thirsty == True  :
        
        choices = get_input(questions)
        drink = mix_drink(choices,ingredients)
        print(drink)
        drink_name = name_drink(choices,drink)
        print("arg! enjoy your " + drink_name +"\n")
        
        if input("are ye thirsty? (yes or no) ") != "yes":
            
            thirsty = False
            
            
    
# this is the main function I used for testing:    
# def main():
    
#      test_input = get_input(questions)
#      print (test_input)
     
#      print("lol")
    
#      test_drink = mix_drink(test_input,ingredients)
#      print(test_drink)
     
#      test_drink_name = name_drink(test_input,test_drink)
#      print(test_drink_name)




