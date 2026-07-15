#exo1:
# password = input('enter paasword:')
# score = 0

# def check_password(password,score):
#     if len (password) < 8:
#         print('weak password')
#         score+=0
#     elif len (password)>8 or len(password)<12:
#         print('medium passsword ')
#         score+=1
#     elif len(password)>13:
#         print('strong password ')
#         score+=2
    
#     if any (char.isdigit() for char in password):
#         score+=1
    
#     if any(char in '!@#$%^&*' for char in password):
#         score+=1

#     print(f'STRENGTH :{len(password)}')
#     print(f"score:{score}/4")


# check_password(password,score)
    

#exo2:
# port = [21,22,23,25,53,80,443,3306,8080,8443]

# def port_services(port):

#         services = {
#         21 : 'FTP - try anonymous login',
#         22 : 'SSH - try default credentials',
#         23 : 'Telnet (DANGEROUS), uncrepted',
#         25 : 'SMTP Mail server',
#         53 : 'DNS - try zone transfer',
#         80 : 'HTTP - check for web vulnerabilities',
#         443 :'HTTPS - check SSL/TLS config',
#         3306 : 'MySQL - try SQL injection',
#         8080: ' HTTP ALTARNATE - check for admin penels',
#         8443: 'HTTPS altarnate - check for dev servers'    
#     }
        
#         for p in port:
#             print(services[p])

# port_services(port)

#exo3

# password= input('Enter password:')
# common_password=["123456", "password", "admin", "root", 
#  "letmein", "qwerty", "monkey", "1234", 
#  "abc123", "pass123"]
# print('[+]Starting brut force...')



# def brut_force(password,common_password):
#       for p in common_password:
#         # (f'trying:{p}')
#          if p == password:
#             print(f'BURT FORCE SUCCED {p}={password}')  
#             attempt=0 
#             for p in common_password:
#               attempt+= 1
#               if p == password:
#                 print(f'number of attems{attempt}')


#             break
         
#          elif p!= password:
#             print(f' failed {p}?={password}')
#       else:
#           print('brut failed!!')

        
          
    
     
        

        




brut_force(password,common_password)