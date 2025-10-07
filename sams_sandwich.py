#Sam's sandwich
import datetime

def bread_selection():
    bread_list=["White","Brown","Italian","Granary","Rye"]
    count=0
    print("We have the following breads: ")
    while count < len(bread_list): #prints out each item on the list
        print(count+1, "  ",bread_list[count])
        count+=1
    bread_selected=int(input("Which bread did you want? Enter a number "))
    return bread_list[bread_selected-1]

def meat_selection():
    meat_list=["Chicken","Pork","Bacon","Beef","Lamb","No meat"]
    count=0
    print("We have the following meats: ")
    while count < len(meat_list): #prints out each item on the list
        print(count+1, "  ",meat_list[count])
        count+=1
    meat_selected=int(input("Which meat did you want? Enter a number "))
    return meat_list[meat_selected-1]

def cheese_selection():
    cheese_list=["Mozzarella","Chedder","Feta","Parmesan","Tasty","No cheese"]
    count=0
    print("We have the following cheeses: ")
    while count < len(cheese_list): #prints out each item on the list
        print(count+1, "  ",cheese_list[count])
        count+=1
    cheese_selected=int(input("Which cheese did you want? Enter a number "))
    return cheese_list[cheese_selected-1]

def dressing_selection():
    dressing_list=["Caesar","Balsamic vinaigrette","Italian","Honey mustard","Ranch","No dressing"]
    count=0
    print("We have the following dressings: ")
    while count < len(dressing_list): #prints out each item on the list
        print(count+1, "  ",dressing_list[count])
        count+=1
    dressing_selected=int(input("Which dressing did you want? Enter a number "))
    return dressing_list[dressing_selected-1]

def salad_selection():
    salad_list=["Lettuce","Tomato","Carrot","Cucumber","Onion","No salad"]
    count=0
    print("We have the following salads, you can have as many as you want ")
    while count < len(salad_list): #prints out each item on the list
        print(count+1, "  ",salad_list[count])
        count+=1
    print("Press enter/return when you have finished chosing your salads ")
    salads_added = "" #will hold a string of more than one item
    selected_salad = " "#prompts the user to enter in a number to select a salad

    while selected_salad != "": #if enter is not pressed it will keep prompting you to enter in a number
        selected_salad = input(f"What number salad do you want?\n You have selected: {salads_added}")
        if selected_salad != "": #if you press enter this if statemnet will not run
            selected_salad = int(selected_salad)
            #this variable keeps adding on each selected item from salad list
            salads_added = salads_added + "  " + salad_list[selected_salad-1]
    return salads_added.strip() #removes empty space at start of the string

def output_textfile(first_name,cellphone_number,sandwich_order):
    date_time=datetime.datetime.now()
    outFile=open("Sam's_Sandwich.txt","a")
    print(f"\n***Order for {first_name} - {cellphone_number}:***")
    outFile.write(f"\nDate of booking:{date_time}")
    for item in sandwich_order:
        print(item)
        outFile.write(f"\n End of order: {date_time}")
    print(f"***End of order : {date_time}***")
    outFile.write("\n")
    outFile.write("\n")
    outFile.close()

#main program
print("Welcome to Sam's Sandwich Shop")
first_name=str(input("Please enter in your first name "))
cellphone_number=str(input("Please enter in your cellphone number "))
bread_choice=bread_selection() #creating a variable that calls up the bread function and returns their choice
meat_choice=meat_selection() #creating a variable that calls up the meat function and returns their choice
cheese_choice=cheese_selection() #creating a variable that calls up the cheese function and returns their choice
dressing_choice=dressing_selection() #creating a variable that calls up the dressing function and returns their choice
salad_choice=salad_selection() #creating a variable that calls up the dressing function and returns their choice
sandwich_order=[]
sandwich_order.append(first_name)
sandwich_order.append(cellphone_number)
sandwich_order.append(f"Bread choice: {bread_choice}")
sandwich_order.append(f"Meat choice: {meat_choice}")
sandwich_order.append(f"Cheese choice: {cheese_choice}")
sandwich_order.append(f"Salad choice(s): {salad_choice}")
output_textfile(first_name,cellphone_number,sandwich_order)