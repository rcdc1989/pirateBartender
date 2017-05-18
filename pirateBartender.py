# Pirate Bartender

# Raphael Capon
# 2017-05-18

# a set of functions to gather user input
# based on a set of questions
# we then use a set of ingredients to output
# a "drink" which assigns ingredients based on input


import random #for use in assigning ingredients

#GIVEN DATA:
questionsDict = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredientsDict = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}


def getInput(questions):
    #   """takes dict of questions returns dict of T/F based on used input"""  
    
    drinkData = {}
    userInput = ""
    
    for entry in questions.keys():
        
        while userInput != 'yes' and userInput !='no':
            userInput = input(questions[entry] + " (enter yes or no) ")
        
        if userInput == "yes":
            drinkData[entry] = True
            
        else:
            drinkData[entry] = False
            
        userInput = ""

    return drinkData
    
    
def mixDrink(drinkData, ingredients):
    
    drink = []
    print("arg")
    
    for entry in drinkData.keys():
        
        if drinkData[entry] :
            
            drink.append(random.choice(ingredients[entry])) 
            
    return drink
    
def main():
    
    testInput = getInput(questionsDict)
    print (testInput)
    
    testDrink = mixDrink(testInput,ingredientsDict)
    print(testDrink)
    
    
    
main()