# Check whether a string is palindrome or not
def check_palindrome():
    word = str(input("Enter string: "))
    if(word == word[::-1]):
        print(f"{word} is palindrome.")
    else:
        print(f"{word} is not palindrome")
#check_palindrome()


#convert a matrix : [[1,2], [3,4], [5,6],[7,8]] into [[1,3,5,7][2,4,6,8]]
def transpose_matrix():
    matrix1 = [[1,2], [3,4], [5,6],[7,8]]
    transposed = [[row[i] for row in matrix1] for i in range(len(matrix1[0]))]
    print(transposed)

#transpose_matrix()

#check prime number
def check_prime_number():
    num = int(input("Enter positive number: "))
    if num>1:
        for i in range(2, num):
            if(num%i == 0):
                print(f"{num} is not a prime number")
                break
            else:
                print(f"{num} is a prime number")
                break
    else:
        print("Invalid number")
#check_prime_number()


#count vowels in a string of input
def count_vowels():
    vowel = str(input("Enter string: ")).lower()
    a=0
    for i in vowel:
        if i in 'aeiou':
            a = a+1
    print(a) 
#count_vowels()


#get the positive numbers in a mix list of string, pos and neg numbers.[ Use list comprehension]
def pos_and_neg_numbers():
    list2 = ['a', 'jkl', 1, 'b', -3, 23, -43, 'j', 3, 5]
    int_list = [i for i in list2 if type(i)== int] #Separate int from list
    
    for p in int_list:
        if p >=0:
            print(p)

#pos_and_neg_numbers()


#from numbers 1 to 100, print “Fizz” if it is multiple of 3 and “Buzz” if it is multiple of 5, “FizzBuzz” if it is multiple of both 3 and 5.
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

#filter even nos from list .[ Use list comprehension]
def filter_even_number():
    list3 = [1, 4, 436, 657, -345, 23, 0, 3]
    even_nos = [i for i in list3 if (i%2==0)]
    print("Even numbers: ", even_nos)
#filter_even_number()

#return True if elements of a list and its reverse are the same. [use slicing]
def palindrome_list():
    list4 = [1, 2, 3, 2, 1]
    if list4 == list4[::-1]:
        print("Is same")
    else:
        print("Not same")
#palindrome_list()