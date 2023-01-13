# DSA Assignment for 18023660 Mable-Ann Yi-An Chang

# 3.1 Sorting

# 3.1.1.b

# author : Silvia Moros
# date : August 2020
# This program sorts the words " London ", " Canterbury ", " York " and " Leicester " by their length(in ascending order ) and prints the result out .
# First , we define our input as an array of strings
cities = [" London ", " Canterbury ", " York ", " Leicester "]
# You can also try it with a very long list . Uncomment this line to do so.
# cities = cities = [’ Lancaster ’, ’ Sunderland ’, ’ Wo lv er ha mp to n ’, ’ Nottingham ’, ’ Oxford ’, ’ Plymouth ’, ’ Salisbury ’, ’ Salford ’, ’ Wakefield ’, ’ Lichfield ’, ’Wells ’, ’ Preston ’, ’ Brighton and Hove ’, ’St Albans ’, ’ Kingston upon Hull ’, ’ Chichester ’, ’ Durham ’, ’ Liverpool ’, ’Bath ’, ’ Bradford ’, ’ Cambridge ’, ’ Ely ’, ’York ’, ’ Exeter ’, ’ Birmingham ’, ’ Carlisle ’, ’ Portsmouth ’, ’ Chester ’, ’Ripon ’, ’ Coventry ’, ’ Gloucester ’, ’ Sheffield ’, ’ Winchester ’, ’ Lincoln ’, ’ Canterbury ’, ’ Westminster ’, ’ Newcastle upon Tyne ’, ’ Peterborough ’, ’ Worcester ’, ’Leeds ’, ’ Norwich ’, ’Stoke -on - Trent ’, ’ Southampton ’, ’ Bristol ’, ’Derby ’, ’ Truro ’, ’ Manchester ’, ’ Hereford ’, ’City of London ’, ’ Leicester ’]
# Initialize our result , which will be empty for now

result = []

# Initialize our loop variables
i = 0
j = 0
number_of_cities = len(cities)

# len () of a list gives you the number of elements in it
# len () of a string will give you the length of it

n = number_of_cities
number_of_steps = 0

# Sort using selection sort
for i in range(0, number_of_cities):
    minimum_length = len(cities[0])
    minimum_element = cities[0]

    for j in range(0, n):
        if (len(cities[j]) < minimum_length):
            minimum_length = len(cities[j])
            minimum_element = cities[j]

        number_of_steps = number_of_steps + 1

    # At the end of the second loop , we will have the shorter element in minimum_element
    # We just need to add it to our results and remove it from our working list

    result.append(minimum_element)
    cities.remove(minimum_element)
    n = n - 1

print("")
print(" The ordered list is:")
print(str(result))
print(" The list had " + str(number_of_cities) + " cities and I ordered it in " + str(
    number_of_steps) + " steps .")

##3.1.2.b

# author : Silvia Moros
# date : August 2020
# This program sorts the words " London ", " Canterbury ", " York " and " Leicester " by their length(in ascending order ) and prints the result out .
# First , we define our input as an array of strings
# cities = [" London ", " Canterbury ", " York ", " Leicester "]
# You can also try it with a very long list . Uncomment this line to do so.
cities = [" Lancaster ", " Sunderland ", " Wolverhampton ", " Nottingham ", " Oxford ", " Plymouth ", " Salisbury ",
          " Salford ", " Wakefield ", " Lichfield ", " Wells ", " Preston ", " Brighton and Hove ", " St Albans ",
          " Kingston upon Hull ", " Chichester ", " Durham ", " Liverpool ", " Bath ", " Bradford ", " Cambridge ",
          " Ely ", " York ", " Exeter ", " Birmingham ", " Carlisle ", " Portsmouth ", " Chester ", " Ripon ",
          " Coventry ", " Gloucester ", " Sheffield ", " Winchester ", " Lincoln ", " Canterbury ", " Westminster ",
          " Newcastle upon Tyne ", " Peterborough ", " Worcester ", " Leeds ", " Norwich ", " Stoke -on - Trent ",
          " Southampton ", " Bristol ", " Derby ", " Truro ", " Manchester ", " Hereford ", " City of London ",
          " Leicester "]
# Initialize our result , which will be empty for now

result = []

# Initialize our loop variables
i = 0
j = 0
number_of_cities = len(cities)

# len () of a list gives you the number of elements in it
# len () of a string will give you the length of it

n = number_of_cities
number_of_steps = 0

# Sort using selection sort
for i in range(0, number_of_cities):
    minimum_length = len(cities[0])
    minimum_element = cities[0]

    for j in range(0, n):
        if (len(cities[j]) < minimum_length):
            minimum_length = len(cities[j])
            minimum_element = cities[j]

        number_of_steps = number_of_steps + 1

    # At the end of the second loop , we will have the shorter element in minimum_element
    # We just need to add it to our results and remove it from our working list

    result.append(minimum_element)
    cities.remove(minimum_element)
    n = n - 1

print("")
print(" The ordered list is:")
print(str(result))
print(" The list had " + str(number_of_cities) + " cities and I ordered it in " + str(
    number_of_steps) + " steps .")

# 3.1.2.a

# author: Mable-Ann Chang
# date: 13 January 2023
# Define an empty list to hold the user's cities
cities = []

# Ask the user for the number of cities they want to enter
num_cities = int(input("How many cities do you want to enter? "))

# Use a for loop to get the user's cities
for i in range(num_cities):
    city = input("Enter city number " + str(i + 1) + ": ")
    cities.append(city)

# Initialize our result, which will be empty for now
result = []

# Initialize our loop variables
i = 0
j = 0
number_of_cities = len(cities)
n = number_of_cities
number_of_steps = 0

# Sort using selection sort
for i in range(0, number_of_cities):
    minimum_length = len(cities[0])
    minimum_element = cities[0]
    for j in range(0, n):
        if (len(cities[j]) < minimum_length):
            minimum_length = len(cities[j])
            minimum_element = cities[j]
            number_of_steps = number_of_steps + 1

    # At the end of the second loop, we will have the shorter element in minimum_element
    # We just need to add it to our results and remove it from our working list
    result.append(minimum_element)
    cities.remove(minimum_element)
    n = n - 1

# Print the ordered list and the number of steps it took to sort it
print("")
print("The ordered list is:")
print(str(result))
print("The list had " + str(number_of_cities) + " cities and I ordered it in " + str(number_of_steps) + " steps.")

#3.1.2.b

# First, ask the user for their list of cities
cities_input = input("Enter your list of cities, separated by commas: ")

# Split the input string into a list of cities
cities = cities_input.split(",")

# Strip leading and trailing whitespace from each city
cities = [city.strip() for city in cities]

# Initialize our result, which will be empty for now
result = []

# Initialize our loop variables
i = 0
j = 0
number_of_cities = len(cities) # len() of a list gives you the number of elements in it
                               # len() of a string will give you the length of it
n = number_of_cities
number_of_steps = 0

# Sort using selection sort
for i in range(0, number_of_cities):
    minimum_length = len(cities[0])
    minimum_element = cities[0]
    for j in range(0, n):
        if (len(cities[j]) < minimum_length):
            minimum_length = len(cities[j])
            minimum_element = cities[j]
        number_of_steps = number_of_steps + 1
    # At the end of the second loop, we will have the shorter element in minimum_element
    # We just need to add it to our results and remove it from our working list
    result.append(minimum_element)
    cities.remove(minimum_element)
    n = n - 1

print("")
print("The ordered list is:")
print(str(result))
print("The list had " + str(number_of_cities) + " cities and I ordered it in " + str(number_of_steps) + " steps.")

# 3.1.2.c

def insertion_sort(lst):
    # Iterate through the elements of the list, starting with the second element
    for i in range(1, len(lst)):
        # Save the value of the current element
        value = lst[i]
        # Save the index of the current element
        j = i
        # Iterate backwards through the sorted sublist
        while j > 0 and lst[j - 1] > value:
            # Shift the larger element to the right
            lst[j] = lst[j - 1]
            j -= 1
        # Insert the current element into its correct position
        lst[j] = value

#Collatz Conjecture
#3.2.1

def collatz(n):
    # Create a loop that runs as long as n is greater than 1
    while n > 1:
        # If n is even, set n to n/2
        if n % 2 == 0:
            n = n // 2
        # If n is odd, set it to 3n + 1
        else:
            n = 3 * n + 1
        # Print the value of n in each iteration
        print(n)

# Test the function with a sample input
collatz(10)

def collatz(n):
    # Return early if n is less than or equal to 1
    if n <= 1:
        return
    # Create a loop that runs as long as n is greater than 1
    while n > 1:
        # If n is even, set n to n/2
        if n % 2 == 0:
            n = n // 2
        # If n is odd, set it to 3n + 1
        else:
            n = 3 * n + 1
        # Print the value of n in each iteration
        print(n)

# Test the function with a sample input
collatz(10)

#3.2.2.b

def collatz(n):
    # Create a loop that runs as long as n is greater than 1
    while n > 1:
        # If n is even, set n to n/2
        if n % 2 == 0:
            n = n // 2
        # If n is odd, set it to 3n + 1
        else:
            n = 3 * n + 1

# Measure the run time for different input values of n
start_time = perf_counter()
collatz(1)
end_time = perf_counter()
print(f"Run time for n = 1: {end_time - start_time:.6f} seconds")

start_time = perf_counter()
collatz(7)
end_time = perf_counter()
print(f"Run time for n = 7: {end_time - start_time:.6f} seconds")

start_time = perf_counter()
collatz(15)
end_time = perf_counter()
print(f"Run time for n = 15: {end_time - start_time:.6f} seconds")

#3.3.3

from collections import Counter


def most_frequent_words(text):
    # Split the text into a list of words
    words = text.split()

    # Count the frequency of each word using a dictionary
    word_counts = Counter(words)

    # Sort the dictionary by value in descending order, then by key in ascending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

    # Print the top 5 most frequent words and their frequencies
    print("Most frequent words:")
    for i in range(5):
        word, count = sorted_word_counts[i]
        print(f"{word}: {count}")


# Read the text file and store its contents in a string
with open("text.txt", "r") as f:
    text = f.read()

most_frequent_words(text)
