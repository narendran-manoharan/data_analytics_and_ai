'''def concatenation(a, b):
    output = a + b
    #print(output)

concatenation("Hello, ", "Python Learner!")

#print(7+3)
#print(10-4)
#print(6*4)
#print(20/4)

#print("My name", "is Python ", "and ","i love coding!")

var_1 = "My "
var_2 = "name "
var_3 = "is "
var_4 = "Python "
var_5 = "and "
var_6 = "I "
var_7 = "love "
var_8 = "coding "
output = (var_1 + var_2 + var_3 + var_4 + var_5 + var_6 + var_7 + var_8)
#print(output)

##Print this sentence using a combination of text and math:
#The result of 8 times 3 is 24
#Hint:
#You can use math inside print() and combine it with text using commas or string formatting.

def multiplication(a, b):
    output = a * b
    #print(f"The result of {a} times {b} is {output}")

multiplication(8, 3)

a = 8
b = 3

#print(f"The result of {a} times {b} is 24")

my_favorite_food = "Biryani"
#print(my_favorite_food)

#One that prints your favourite number plus 10.

my_favorite_number = 7
#print(10 + my_favorite_number)

#One that prints a fun fact about you.

my_fun_fact = "Travelled Western Europe with my cat!"
print(my_fun_fact)'''


def guessthenumber(user_input):
    numbers = [1, 10, 40, 23, 19, 42, 12, 18, 17, 21, 8, 2]
    answer = []
    for number in numbers:
        for number2 in numbers:
            if number != number2 and number + number2 == user_input:
                answer.append((number, number2))
            

    if answer:
        return (answer)
    else:
        return None
#guessthenumber(19)
print(guessthenumber(20))