def formatInput(textline) :
    textLine = textline.lower().strip()
    wordList = textLine.split()
    textLine = " ".join(wordList)
    return  textLine
print(" " * 20 + "Good Morning Canada!")
print("_"*70)
#Making a dictionary holding  all of the values
menu_items= {"small breakfast","regular breakfast","big breakfast","egg","bacon","sausage","hashbrown","toast","coffee","tea"}

#listing all the prices of the breakfast items
egg= 0.99
bacon= 0.49
sausage= 1.49
hashbrown= 1.19
toast= 0.79
coffee= 1.49
tea = 1.09
Tax= 0.13
cost = 0
cost_total = 0
#make a true/false statement for the users selection
invalid_choice = False

# Loop to check whether the choice of food is in the menu
while not invalid_choice:
    user_choice = formatInput(input("Enter item (q to terminate): small breakfast,regular breakfast, big breakfast, egg,bacon,sausage, hashbrown, toast, coffee, tea"))
    if user_choice == "q":
        break
    if user_choice not in menu_items:
        while user_choice not in menu_items:
            print("Sorry item is not in the menu, please try again")
            user_choice= input("Enter item (q to terminate): small breakfast, regular breakfast,big breakfast, egg, bacon, sausage, hashbrown, toast, coffee,tea")
            if user_choice == "q":
                break
            continue
        person_quantity= input(("Enter quantity: "))
# If statements to allow user to choose what type of breakfast they want
        if user_choice== "small breakfast":
            cost= cost + (egg *1) + (hashbrown *1) + (toast*2) + (bacon *2) + (sausage *1)
        if user_choice== "regular breakfast":
            cost= cost + (egg *2) + (hashbrown *1) + (toast*2) + (bacon *4) + (sausage *2)
        if user_choice== "big breakfast":
            cost= cost + (egg *3) + (hashbrown *2) + (toast*4) + (bacon *6) + (sausage *3)
# Calculating the cost of each item from the menu selections
        if user_choice == "egg":
            cost= cost + egg
        if user_choice == "bacon":
            cost= cost + bacon
        if user_choice == "sausage":
            cost= cost + sausage
        if user_choice == "hash brown":
            cost= cost +hashbrown
        if user_choice == "toast":
            cost= cost + toast
        if user_choice == "coffee":
            cost= cost + coffee
        if user_choice == "tea":
            cost= cost + tea
 # Loop that check if person_quantity is numeric or not(a real number)
    while not person_quantity.isnumeric():
        print("Please enter a valid number")
        person_quantity= input("Enter quantity: ")

    # Loop to check whether the number that in entered is lower than zero b/c we can't have a negative number
    person_quantity = int(person_quantity)
    if int(person_quantity<0):
        while int(person_quantity<0):
            print("Number is invalid")
            person_quantity= input("Enter quantity: ")
            continue
    # else statement computes the cost of the customers order if the number they entered is valid(>0)
    else:
        cost = cost * person_quantity
        cost_total = cost_total + cost
    # calculating the value of the tax for the customers order
    tax_value = cost_total * Tax
    # computing the total for the customers order
    total = cost_total + tax_value
    print()
    # Making sure all numeric outputs should only have 2 decimal places
    print("Cost: $%.2f" % cost_total)
    print("Tax: $%.2f" % tax_value)
    print("Total: $%.2f" % total)















