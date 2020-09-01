import read
import write
from read import movie_id
from read import dictionary_movie
import rent
#takes input from user name and phone number
name = input("please register your name:")
#confirms the phonenumber is integer
while True:
    try:
        phoneNumber = int(input("Enter your phone Number:"))
        break
    except:
        print("Invalid Phone Number")
#displays welcome screen
print("***Welcome!! " + name + "***")
print("Your registration Name is "+name+" and phone number is:"+str(phoneNumber))
print("Welcome to Movie Rental System")
#runs menu unless user want to exit
while True:
    print("Choose your option:")
    print("Press 1: View all list of movies.")
    print("Press 2: Rent a movies.")
    print("Press 3: Return a movies.")
    print("Press 4: Exit the application.")
    #checks if the input is correct or not if not displays message
    while True:
        try:
            choice = int(input("enter the choice."))
            break
        except:
            print("enter the correct input!!")
    if choice == 1:
        #display the menu 
        read.display()
    elif choice == 2:
        rent.rentMovie(name, phoneNumber)

    elif choice == 3:
        rent.reurnMovie(name, phoneNumber)
    elif choice == 4:
        write.writeNExit()
        break
    else:
        print("enter the correct option.")
