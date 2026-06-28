#Basics input,print command

print('=' * 40)
print(' FIND ALL BUGS -by n3o')
print('=' * 40)

target = input('Enter target IP or domain:')
port = input('Enter target port:')
port = int(port)

print('\n[*] Target:', target)
print('[*] Port:', port)
print('[*]Starting reconnaissance...')

print("\n[*] Data types:")
print(type(target))


#If statement

#--- check if port is valid
if port < 1 or port > 65535:
    print('[-] Invalid port number:', port)
else:
    print('[+] Valid port:', port)
#check for intresting ports
if port == 80:
    print('[*] HTTP detected -check for web vulnerabilities:')
elif port == 443:
    print('[*] HTTPS detected -check SSL/TSL config')
elif port == 22:
    print('[*] SSH detected -trv default credentials')
elif port == 3306:
    print('[*] MySQL detected -try SQL injection')
else:
    print('[*]Unknown port -enumerate futher..')

# Loop through common ports
print("\n[*] Checking common ports...")

common_ports = [21,22,23,25,53,80,443,3306,8080,8443]

for port in common_ports:
    if port == 21 :
       print(f' [+] Port {port} -> FTP')
    elif port == 22:
        print(f' [+] Port {port} -> SSH')
    elif port == 23:
        print(f' [+] Port {port} -> Telnet (DANGEROUS)')
    elif port == 25:
        print(f' [+] Port {port} -> SMTP(mail)')
    elif port == 53:
        print(f' [+] Port {port} -> DNS')
    elif port == 80:
        print(f' [+] Port {port} -> HTTP')
    elif port == 443:
        print(f' [+] Port {port} -> HTTPS')
    elif port == 3306:
        print(f' [+] Port {port} -> MySQL')
    elif port == 8080:
        print(f' [+] Port {port} -> HTTP alternate')
    elif port == 8443:
        print(f' [+] Port {port} -> https altarnete')


print('[+] Starting reconnaissance ...')

#Functions:
def identify_service(port):
    services = {
        21 : 'FTP - try anonymous login',
        22 : 'SSH - try default credentials',
        23 : 'Telnet (DANGEROUS), uncrepted',
        25 : 'SMTP Mail server',
        53 : 'DNS - try zone transfer',
        80 : 'HTTP - check for web vulnerabilities',
        443 :'HTTPS - check SSL/TLS config',
        3306 : 'MySQL - try SQL injection',
        8080: ' HTTP ALTARNATE - check for admin penels',
        8443: 'HTTPS altarnate - check for dev servers'    
    }
    if port in services:
        print (f' [+] Port {port} -> {services[port]}')
    else :
        print(f' [?] Port {port}, unknown - enumerate manually ')

# Test with multiple ports
test_ports = [21, 80, 443, 3306, 9999]
for p in test_ports:
    identify_service(p)
