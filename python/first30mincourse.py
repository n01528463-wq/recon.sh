# name = 'bob'#string
# print('hello' + name + '!')

# number = -10#intger
# decimal = 1.23#float
# has_money=True#boolen
# coordinates=(2,3,4)#tuple we can not change it 
# name=[1,23,45]#list can be change
# unique={1,3,56,5}#set cna not contain duplicates
# users={'admin':1,'bob':2}#dictionary have a key and a value

# number='12'
# number=int(number)
# print(12+number)

# age: int =10#make sure to follow the type it will be easy to find the error
# # age: int = '12' it will be red
# name: str = 'bob'
# print(f'name:{name}')# the f string =format

# #functions
# def add (a: float, b:float) -> float:
#     print(f'adding {a}+{b}')
#     return a + b
# print( 12+23)
# print(1,2+22.4)

# def greet(name,greeting):
#     print(f'{greeting},{name}!')

# greet(name='bob', greeting="hello")

# #looping
# #two types while loop infinite , for loop falnate looping

# for i in range(3):
#     print('hello')#used a lot with lists

# names=['ama','see','done']
# for name in names:
#     print(f'hello,{name}')
#     print('....')
# i=0
# while i<3:
#     print(i)
#     i+=1
# a=1
# b=4
# print(a>=b)#false out put
# > < >= <= !=  == famous operator using them a lot

#if,elif,else
# while True:
#  user_input=input('you:')
#  if user_input =='hello':
#     print('bot:hello!')
#  elif user_input =="how are you":
#     print('bot:good,how about you')
#  elif user_input=='bye':
#     print('bot:goodbye')
#     break
#  else:
#     print('sorry i dont undestand') 

#error handeling
# a ,b=10,'ff'

# try:
#   print(a+b)
# except Exception as e:
#   print(f'something went wrong:{e}')

# print('continue with the program')


#exept typeerror as e: more specific
#you can add multiple exept block use type eeror not exeption
#cause it makes the error desapear!

# importing
# import math
# import math as m
# from math import sqrt,tan

# print(math.sqrt(3))
# print(m.sqrt(4))
# print(sqrt(5))
# print(tan(2))


#the first chat bot
print('Starting chat bot ...')
user= input('YOU:').lower#compare only letters
while True:
    def chat_bot(user):
        if user in ['hi,hello']:
            print('BOT: hello there how can i assiste you!')
        elif user in ['bye,goodbye']:
            print('see ya !!')
            # break
        elif user in ['add,+']:
            print('BOT: okay lets do some math')
            num1=input('enter the first number:').float
            num2=input('enter the second number:').float
        else:
            print('dont undestand')
        try:

            sum = num1 +num2
        except TypeError as e :
            print(f'something went wrong {e}')
            print('contiun program...')
        print(f' the result:{sum}')
    





    



