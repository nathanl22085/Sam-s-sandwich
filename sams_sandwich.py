#Sam's sandwich
import datetime

#this function will ensure the user can only enter in a valid number within a range

def force_number(message,lower,upper):
    while True:
        try:
            num=int(input(message))
            if num>=lower and num<=upper:
                break 
            else:
                print(f"Invalid number, please enter in {lower} - {upper}")
        except:
            print("Error - Only type in numbers please")
    return num

#creating a function that forces the users name

def force_name(message,lower,upper):
    while True: #This is an infinite loop
        name=str(input(message)).title() #asking for and storing the users name, adds a capital letter to it
        if len(name) >=lower and len(name)<=upper and name.isalpha():
            break #The loop is broken if the above condition is met
        else:
            print("Invaild name")
    return name #returns a valid name back to the variable that called the function

def force_cellphone_number(message,lower,upper):
    while True: #infinite loop that keeps repeating until a valid number is input
        cell=str(input(message))
        if len(cell)>=lower and len(cell)<=upper and cell.isnumeric():
            break
        else:
            print(f"Error! Please enter in between {lower} - {upper}")
    return cell #returning back a valid number within the range

#this function will be called up in other fucntions and rerun to customise the print statement to the related topic
def print_list(list,item):
    count=0
    print(f"We have the following {item}: ")
    while count < len(list): #prints out each item on the list
        print(count+1, "  ",list[count])
        count+=1
    return

#this function contains a list of breads and calls up the print_list function to display the options for the user to choose from
def bread_selection():
    bread_list=["White","Brown","Italian","Granary","Rye"]
    print_list(bread_list,"breads") #calls up the list and adds the item name bread
    bread_selected=force_number("Which bread did you want? Enter a number ",1,len(bread_list))
    return bread_list[bread_selected-1]

#this function contains a list of meats and calls up the print_list function to display the options for the user to choose from
def meat_selection():
    meat_list=["Chicken","Pork","Bacon","Beef","Lamb","No meat"]
    print_list(meat_list,"meats")
    meat_selected=force_number("Which meat did you want? Enter a number ",1,len(meat_list))
    return meat_list[meat_selected-1]

#this function contains a list of cheeses and calls up the print_list function to display the options for the user to choose from
def cheese_selection():
    cheese_list=["Mozzarella","Chedder","Feta","Parmesan","Tasty","No cheese"]
    print_list(cheese_list,"cheeses")
    cheese_selected=force_number("Which cheese did you want? Enter a number ",1,len(cheese_list))
    return cheese_list[cheese_selected-1]

#this function contains a list of dressings and calls up the print_list function to display the options for the user to choose from
def dressing_selection():
    dressing_list=["Caesar","Balsamic vinaigrette","Italian","Honey mustard","Ranch","No dressing"]
    print_list(dressing_list,"dressings")
    dressing_selected=force_number("Which dressing did you want? Enter a number ",1,len(dressing_list))
    return dressing_list[dressing_selected-1]

#this function contains a list of salads and calls up the print_list function to display the options for the user to choose from
def salad_selection():
    salad_list=["Lettuce","Tomato","Carrot","Cucumber","Onion","No salad"]
    print_list(salad_list,"salads")
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
    outFile.write(f"\nDate of booking:{date_time}\n")
    for item in sandwich_order:
        print(item)
        outFile.write(item)
        outFile.write(f"\n")
    print(f"***End of order : {date_time}***")
    outFile.write("\n")
    outFile.write("\n")
    outFile.close()

def main_function():
    print("Welcome to Sam's Sandwich Shop")
    first_name=force_name("Please enter in your first name eg Bob (2-20 characters) ",2,20)
    cellphone_number=force_cellphone_number("Please enter in your cellphone number, eg 123456789 (no need to include the 0, between 8-12 characters) ",8,12)
    bread_choice=bread_selection() #creating a variable that calls up the bread function and returns their choice
    meat_choice=meat_selection() #creating a variable that calls up the meat function and returns their choice
    cheese_choice=cheese_selection() #creating a variable that calls up the cheese function and returns their choice
    dressing_choice=dressing_selection() #creating a variable that calls up the dressing function and returns their choice
    salad_choice=salad_selection() #creating a variable that calls up the salad function and returns their choice
    sandwich_order=[]
    #the .append functions add to the list "sandwich order"
    sandwich_order.append(f"Name: {first_name}")
    sandwich_order.append(f"Cellphone number: {cellphone_number}")
    sandwich_order.append(f"Bread choice: {bread_choice}")
    sandwich_order.append(f"Meat choice: {meat_choice}")
    sandwich_order.append(f"Cheese choice: {cheese_choice}")
    sandwich_order.append(f"Dressing choice: {dressing_choice}")
    sandwich_order.append(f"Salad choice(s): {salad_choice}")
    output_textfile(first_name,cellphone_number,sandwich_order)

#main program
main_function()