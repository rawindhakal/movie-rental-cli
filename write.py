#importing date and tile
import datetime
#function to write in a file when a movie is rented
from read import dictionary_movie


def write_rent(name, movieidTemp, movieNameTemp, moviePriceTemp, phoneNumber):
    filename = "RentedMovie/" + name + "_" + str(phoneNumber) +".txt"
    file = open(filename, "w")
    file.write("*****************************************\n")
    file.write("Rented on:"+str(datetime.datetime.now()))
    file.write("\nCustomer Name:"+name)
    file.write("\nCustomer Phone Number:"+str(phoneNumber))
    file.write("\nMovie ID \t\t Movie Name \t\t \tPrice")
    file.write("\n")
    for i in range(len(movieidTemp)):
        file.write(movieidTemp[i]+"\t\t\t\t"+movieNameTemp[i]+"\t\t\t\t"+moviePriceTemp[i])
        file.write("\n")
    #to calculate the amount of rented movies
    total = 0
    for i in moviePriceTemp:
        i = i.replace("$", "")
        total = total + float(i)
    file.write("\nThe total price for renting movies is:"+"$"+str(total))

    file.close()

def writeNExit():
    # writes the main database file and exits the program
    file = open("movies.txt", "w")
    for key, value in dictionary_movie.items():
        file.write(key + "," + value[0] + "," + value[1] + "," + value[2])
        file.write("\n")
    file.close()
    
