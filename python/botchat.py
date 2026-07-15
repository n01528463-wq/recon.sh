print('Starting chat bot ...')
while True:

  user= input('YOU:')#compare only letters

  def chat_bot(user):
        
        if user in ('hello','hi'):
            print('BOT: hello there how can i assiste you!')
        elif user in ('bye','goodbye'):
            print('BOT:see ya !!')
        
        elif user in ('add','+'):
            print('BOT: okay lets do some math')
            num1  = input('enter the first number:')
            num2  = input('enter the second number:')
            
            num1=float(num1)
            num2=float(num2)
            # sum = num1 + num2
            # print(f'BOT: the sum is {sum}')
        # try:
            sum = num1 +num2
        # except TypeError as e:
        #         print (f'BOT:something is wrong {e}')
            print(f'BOT: the sum is : {sum}')

        else:
           print('BOT: sorry i dont undestand?')
                                        
        
    
  chat_bot(user)




