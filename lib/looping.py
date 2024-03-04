#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter = 10
    while counter > 0 :
        print (counter)
        counter -= 1
    print ("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    int_list = [ int * int for int in int_list ]
    return int_list

def fizzbuzz():
    # code goes here!
    
    for counter in range (1, 101) :
        if counter % 3 == 0 and counter % 5 == 0 :
            print ("FizzBuzz")
        elif counter % 3 == 0 :
            print ("Fizz")
        elif counter % 5 == 0 :
            print ("Buzz")
        else :
            print (counter)
    pass
