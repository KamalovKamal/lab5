# task 1
# def func(gramm):
#      ounces = 28.3495231 * gramm
#      print(ounces)

# gramm = int(input())
# func(gramm)

# task 2
# def func(far):
#     celsiy = ((5/9) * (far-32))
#     print (celsiy)

# far = int(input())
# func(far)

# task 3
# def schitalka_nog(h,l):
#     b=(l-(2*h))/2
#     a=h-b
#     print("голов = ", a,"ног = ", b)

# h=int(input())
# l=int(input())
# schitalka_nog(h,l)

# task 4
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def filter_prime(numbers):
#     prime_numbers = [num for num in numbers if is_prime(num)]
#     return prime_numbers

# user_input = input()
# numbers = [int(num) for num in user_input.split()]

# prime_numbers = filter_prime(numbers)
# print(*(prime_numbers))

# task 5
# from itertools import permutations

# def print_permutations(b):
#     words = permutations(b)
#     for word in words:
#         print(''.join(word))

# a = input()
# print_permutations(a)

# task 6
# def reverse_words(sentence):
#     words = sentence.split()
    
#     reversed_sentence = ' '.join(reversed(words))
#     return reversed_sentence


# a = input()
# reversed = reverse_words(a)
# print( reversed)

# task 7
# def has_3(nums):
#     for i in range(len(nums) - 1):
#         if nums[i] == 3 and nums[i + 1] == 3:
#             return True
#     return False

# a = [int(b) for b in input().split()]
# result = has_3(a)
# print(result) 

# task 8
# def spy_game(k):
#     for i in range(len(k)-2):
#         if(k[i]==0 and k[i+1]==0 and k[i+2]==7):
#             return True
#         return False 

# k = [int(a) for a in input().split()]
# print(spy_game(k))

# task 9
# def obyem(r,pi):
#     return(float((4/3)*pi*r*r*r))
# pi = 3.14
# r= int(input())
# print(float(obyem(r,pi)))

# task 10
# def uniq(a):
#     l=[]
#     for i in a: 
#         if i not in l: 
#             l.append(i) 
#     return(l)
    
# a = [int(s) for s in input().split()] 

# result = uniq(a)   
# for i in result: 
#     print(i, end=' ')

# task 11
# def IsPolindrome(word):
#     if(word==word[::-1]):
#         print("Is polindrome:", word)
#     else:
#         print("Is not polindrome:", word)
# word=str(input())
# IsPolindrome(word)

# task 12
# def histogram(a):
#     for i in range(len(a)):
#         for j in range(a[i]):
#             print('*',end='')
#         print('\n')
# a=[int(s) for s in input().split()]
# histogram(a) 

# task 13
import random

def guess_the_number_game():
    player_name = input("Hello! What is your name?\n")
    print(f"Well, {player_name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    
    guesses = 0
    while True:
        try:
            guess = int(input("Take a guess.\n"))
            guesses += 1

            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print(f"Good job, {player_name}! You guessed my number in {guesses} guesses!")
                break
        except ValueError:
            print("Please enter a valid number between 1 and 20.")

# Запуск игры
guess_the_number_game()
