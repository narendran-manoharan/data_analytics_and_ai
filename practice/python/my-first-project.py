challenger = {
	"name": "Katniss Everdeen",
	"age": 16,
	"district": 12,
	"weapon": "Bow and Arrow", 
	"status": "Victor"
}

# add your code here

numbers = []
for i in range(15): #for every number in the range 0 - 15
    numbers.append(i) #append the numbers list with each number you found in the range


#numbers = [i for i in range(15)]

my_word = "crazy world"
#print(i for i in my_word)

x = "ABCDEF"


matrix = [ [0, 1, 2, 3],
          [4, 5, 6, 7],
          [8, 9, 10, 11],
]
#new_matrix = return([[row[i] for row in matrix] for i in range(4)])

student_data = [{"name": "John Smith", "email": "john@gmail.com", "subjects": ["Math, Psychology, Physics, Chemistry,  Biology"]},
{"name": "Mary Jones", "email": "mary@gmail.com", "subjects": ["Fine Art, Music, Biology, Geography, Politics"]}
    ]


def product_numbers(a, b):
    product = (a ** b)
    return product

result = product_numbers(32, 35)
#print(result)

def add_numbers(*list_integers):
    total = 0
    for x in list_integers:
        total += x
     
    return total

#print(add_numbers(1, 2, 3, 4, 5, 6, 7))

#def concatenate_words(**words):
    #result = " "
    #for word in words.values():
        #result += word
        #result += " "
    #eturn result
#print(concatenate_words(a = "I", b = "had", c = "a", d = "nice", e = "weekend"))

#user_age = False

#update_user_age = int(input("Enter your age: "))
#if update_user_age >= 18:
    user_age = True
#    print("Welcome, you are of legal age!")
#else:
 #   print("Sorry, come back when you are 18!")

#check on May 12
##def new_func( **args ):
    print(f"The arguments are {args}")

##def pass_func(function_name, **args):
    print("This function takes another function as an argument")
    function_name(f = args["l"])

##pass_func(new_func, l = "spam")##

#def new_function(func):
    def wrapper():
        print("No clue about what's happening!")
        func()
        print("Let's see what happens now!")
    
    return wrapper

#@new_function
#def compl_shit():
    print("Still wondering!")

#compl_shit()

#numbers = [12, 45, 60, 87, 999, 200, 84, 42, 87, 77, 2, 3, 77, 99, 20]
#print(list(filter(lambda i: i % 2 == 0, numbers)))

#def choose_odd_numbers(numbers):
    #new_odd_numbers = []
    #for i in numbers:
        #if i % 2 != 0:
            #new_odd_numbers.append(i)
    #return new_odd_numbers

#new_odd_numbers = choose_odd_numbers(numbers)
#print(new_odd_numbers)

#new_odd_numbers_2 = choose_odd_numbers([34234598, 234347, 454870, 9738785, 65, 89])
#print(new_odd_numbers_2)




