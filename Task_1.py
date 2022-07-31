# 1 Check whether a string is palindrome or not
from cv2 import sort


def check_palindrome():
    word1 = str(input("Enter string: "))
    word = word1.lower()
    if(word == word[::-1]):
        print(f"{word} is palindrome.")
    else:
        print(f"{word} is not palindrome")
#check_palindrome()


#2 convert a matrix : [[1,2], [3,4], [5,6],[7,8]] into [[1,3,5,7][2,4,6,8]]
def transpose_matrix():
    matrix1 = [[1,2], [3,4], [5,6],[7,8]]
    transposed = [[row[i] for row in matrix1] for i in range(len(matrix1[0]))]

    ##Using loop
    for row in matrix1:
        print(row)
        for i in range(2):
            print(row[i])
    print(transposed)



#transpose_matrix()

#3 check prime number
def check_prime_number():
    num = int(input("Enter positive number: "))
    if num>1:
        for i in range(2, num):
            if(num%i == 0):
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
            
    else:
        print("Invalid number")
#check_prime_number()


#4 count vowels in a string of input
def count_vowels():
    vowel = str(input("Enter string: ")).lower()
    a=0
    for i in vowel:
        if i in 'aeiou':
            a = a+1
    #print(a) 
#count_vowels()


#5 get the positive numbers in a mix list of string, pos and neg numbers.[ Use list comprehension]
def pos_and_neg_numbers():
    list2 = ['a', 'jkl', 1, 'b', -3, 23, -43, 'j', 3, 5]
    int_list = [i for i in list2 if type(i)== int] #Separate int from list
    
    for p in int_list:
        if p >=0:
            print(p)
    
    #positive number (2nd method)
    num2 = [each for each in list2 if type(each)==int and each>1]
    print(num2)

#pos_and_neg_numbers()


#6 from numbers 1 to 100, print “Fizz” if it is multiple of 3 and “Buzz” if it is multiple of 5, “FizzBuzz” if it is multiple of both 3 and 5.
def multiple_of_5_and_3():
    for i in range(1, 101):
        if(i%3==0 and i%5==0):
            print("FizzBuzz")
        elif(i%3==0):
            print("Flizz")
        elif(i%5 == 0):
            print("Buzz")
        
        else:
            print(i)
#multiple_of_5_and_3()

#7 filter even nos from list .[ Use list comprehension]
def filter_even_number():
    list3 = [1, 4, 436, 657, -345, 23, 0, 3]
    even_nos = [i for i in list3 if (i%2==0)]
    print("Even numbers: ", even_nos)
#filter_even_number()

#8 return True if elements of a list and its reverse are the same. [use slicing]
def palindrome_list():
    list4 = [1, 2, 3, 2, 1]
    if list4 == list4[::-1]:
        print("Is same")
    else:
        print("Not same")
#palindrome_list()


# filter dict b : so that we can get only values which consists of letters 'abc'
#using dict comprehension    
#res = {'2':'approved', '3':'abcde'}
def filter_dict():
    b = {'1':'pending', '2':'approved', '3':'abcde'}
    res = {k:v for k,v in b.items() if ('a' or 'b' or'c') in v}
    print(res)
#filter_dict()

'''Tasks: Jul 28, 2022 Deadline: Aug 1
9. Create a Hangman Game , where the first input can be any string. Then you have 5
chances to guess the word. For each chance, you get a letter to pick. If the letter is not
contained in the string, your chance is reduced, if you enter a letter that is in the string,
fill up the blanks with those letters and continue.'''
def Hangman():
        user_input = str(input("Enter a word: "))
        print("Word length: ", len(user_input))
        word = [x for x in user_input]

        correct_input =[]
        incorrect_input = []
        #print(word)

        
        while len(correct_input) != len(word):
            if len(incorrect_input) != 5:
                player_guess = str(input("Guess a letter: "))
                #for player_guess in word:
                if player_guess in word:
                    print("Correct")
                    if player_guess not in correct_input:

                        c=word.count(player_guess)
                        for i in range(0,c):  #Insert duplicate letters
                            correct_input.append(player_guess)
                        print("Correct Guesses: ", correct_input)

                    else:
                        print("Already guessed")
                else:
                    print("Incorrect")
                    if player_guess not in incorrect_input:
                        incorrect_input.append(player_guess)
                        #print("Incorrect Guesses: ", len(incorrect_input))
                        print("Number of guesses left: ", (5-len(incorrect_input)))
                    else:
                        print("Already guessed")
            else:
                print("         Game over")
                print( "         _____________")
                print( "         !           |")
                print( "      |0   0|        |")
                print( "         |           |")
                print( "        /|\          |")
                print( "       / | \         |")
                print( "         |           |")
                print( "        / \          |")
                print( "       /   \         |")
                print( "                     |")

                print("correct answer: ", user_input)
                break
        else:
            print("Congratulation")
            print("Correct answer: ", user_input)



#Hangman()
#10. Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336
def multiply_list():
    mul_list = [8,2, 3, -1, 7]
    a=1
    for i in mul_list:
        a = a*i
        print(a)
#multiply_list()

# 11. Write a Python program to get the maximum and minimum value in a dictionary.
#my_dict = {'x':500, 'y':5874, 'z':560}
def max_min_dict():
    my_dict = {'x':500, 'y':5874, 'z':560}
    sorted_list = sorted(my_dict.values())
    max_value = sorted_list[-1]
    min_value = sorted_list[0]
    print("Maximum value: ", max_value)
    print("Minimum value: ", min_value)
#max_min_dict()

# 12. Write a Python program to combine two dictionary adding values for
# common keys. d1 = {'a':100, 'b': 200, 'c':300}
# d2 = {'a':300, 'b':200, 'd':400}
# Sample output: {'a':400, 'b':400, 'd':400, 'c':300}
def add_dictionary():
    d1 = {'a':100, 'b': 200, 'c':300}
    d2 = {'a':300, 'b':200, 'd':400}
    d3 = dict(d1)
    d3.update(d2)
    for k,v in d1.items():
        for i,j in d2.items():
            if k==i:
                d3[i] = v+j
    print(d3)


#add_dictionary()


# 13. Write a Python program to create and display all combinations of
# letters, selecting each letter from a different key in a dictionary.
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd



# 14. Add two lists using map and lambda

# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]
# Output: [5, 7, 9]
def add_list_using_map_lambda():
    numbers1 = [1, 2, 3]
    numbers2 = [4, 5, 6]

    added_list = list(map(lambda x,y: x+y, numbers1, numbers2))
    print(added_list)
#add_list_using_map_lambda()

# 15. Sort a list of string values. Once by ascending and then by
# descending according to alphabetical letters.
# a = [‘abc’, ‘def’, ‘avh’, ‘bbb’, ‘ccc’, ‘zed’, ‘zas’]

def sort_list():
    a = ['abc', 'def', 'avh', 'bbb', 'ccc', 'zed', 'zas']
    ascending = sorted(a)
    descending = sorted(a, reverse=True)
    print(ascending)
    print(descending)
#sort_list()

# 16. TicTacToe Game.
# Note: No need for UI. Use matrix concepts to place your ‘X’ or ‘O’. Input
# turn by turn for two players and one can win by horizontal/vertical or
# diagonal match.
# 17. Li = ['abc', 'def', 'ghi']
# Op = [ [‘a’,’b’,’c], [‘d’,’e’,’f’], [‘g’,’h’,’i’]]. Use map.

'''def list_map(l):
    
    for i in l:
        for j in i:
            return j
Li = ['abc', 'def', 'ghi']
res = map(list_map, Li)
a = set(res)
print(a)'''


# 18. X = [5,10,15]
# Y = [3,6,9]
# Op = [8,16,24]. Use map and lambda
def sum_list_lambda():
    X = [5,10,15]
    Y = [3,6,9]
    sum_list = list(map(lambda i,j : i+j, X, Y))
    print(sum_list)
#sum_list_lambda()

# 19. Dynamically pass parameters in a function which passes multiple positive and neg
# integers. Return sum of all the values passed.
# Eg:
# A(1,2,3) op = 6
# A(1,2,3,4) op = 10
# 20. Convert radian to degree.
# 21. Convert binary number to Decimal


# 22. Check if the first and last element in a list is equal.
def first_last_element():
    list = ['a', 'b', 'c', 2, 'a']
    if list[0] == list[-1]:
        print("Equal")
    else:
        print("Not equal")
#first_last_element()