import datetime
import read
import write
from read import movie_id
from read import dictionary_movie
#function to write a file when a movie is returned
def rent(name, movieidTemp1, movieNameTemp1, moviePriceTemp1, day, phoneNumber):
    filename = "ReturnMovie/" + name +"_"+str(phoneNumber) +".txt"
    file = open(filename, "w")
    file.write("*****************************************\n")
    file.write("Returned On:" + str(datetime.datetime.now()))
    file.write("\nCustomer Name:" + name)
    file.write("\nCustomer Phone Number:" + str(phoneNumber))
    file.write("\nMovie ID \t\t Movie Name \t\t Price")
    file.write("\n")
    for i in range(len(movieidTemp1)):
        file.write(movieidTemp1[i] + "\t\t\t\t" + movieNameTemp1[i] + "\t\t\t\t" + moviePriceTemp1[i])
        file.write("\n")
    #calculate the total amount to be paid while return
    total = 0
    for i in moviePriceTemp1:
        i = i.replace("$", "")
        total = total + float(i)
    file.write("The total price for renting movies is:" + "$" + str(total))
    #function to calculate the fine on movie
    total_fine = 0
    price = 0
    for i in range(len(day)):
        if day[i] > 10:
            fine_day = day[i] - 10
            for j in moviePriceTemp1:
                j = j.replace("$", "")
                price = float(j)
            total_fine = 1.5 + price + fine_day
    file.write("\nTotal fine for returning movie is:"+"$"+str(total_fine))

def reurnMovie(name, phoneNumber):
    # to return movie
    movieidTemp1 = []
    movieNameTemp1 = []
    moviePriceTemp1 = []
    day = []
    value = "y"
    while value == "y":
        movieid = input("Enter the movie id to return:")
        if movieid in movie_id:  # movie id check
            movieidTemp1.append(movieid)
            movieNameTemp1.append(dictionary_movie[movieid][0])  # adding movie name to new temp list
            moviePriceTemp1.append(dictionary_movie[movieid][2])  # adding movie price to new temp list
            # check for rent days
            while True:
                try:
                    days = int(input("How many days did you rent a movie:"))
                    day.append(days)
                    break
                except:
                    print("entered day format is invalid please input again")
        else:
            print("Movie id not valid please check")
        value = input("Do you want to return another movie (y/n)")
    # calling rent function from rent module with paramaters
    rent(name, movieidTemp1, movieNameTemp1, moviePriceTemp1, day, phoneNumber)
    # adding quantity of the movies returned by user
    for i in movieidTemp1:
        a = int(dictionary_movie[i][2])
        b = a + 1
        dictionary_movie[i][2] = str(b)

def rentMovie(name, phoneNumber):
    # To rent
    movieidTemp = []
    movieNameTemp = []
    moviePriceTemp = []
    ans = 'y'
    while ans == 'y':
        movieid = input("Enter the movie id:")
        if movieid in movie_id:  # checks if entered movie id is present in our database or not
            item = read.dictionary_movie[movieid][2]
            if int(item) > 0:  # checks if the entered movie quantity is >0 or nor
                movieidTemp.append(movieid)
                movieNameTemp.append(dictionary_movie[movieid][0])  # wites the name of movie in new temp list
                moviePriceTemp.append(dictionary_movie[movieid][1])  # wites the price of movie in new temp list
            else:
                print("Selected movie is out of stock you may choose another movie")
        else:
            print("Enter the correct ID")
        ans = input("Do you want to rent other movie:(y/n)")  # ask user if they want to rent other movie or not
    # function to call wite_rent module passing parrameters
    write.write_rent(name, movieidTemp, movieNameTemp, moviePriceTemp, phoneNumber)
    # it substracts the quantity of movie id rented
    for i in movieidTemp:
        a = int(dictionary_movie[i][2])
        b = a - 1
        dictionary_movie[i][2] = str(b)