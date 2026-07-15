import socket
from datetime import datetime



print ('='*80)
print('                              PORT SCANNER v1.0           ')
print('='*80)
target=input('[*] Enter target (IP or domain):')
print(f'[*] Resolving {target}....')    

try:
    ip = socket.gethostbyname(target)
    print(f'[+] IP adress:{ip}')  
except socket.gaierror:
        print("[-] Could not resolve domain")

start=int(input('[*] Start port: '))
end =int(input('[*] End port: '))

def is_port_open( ip,port):
            
           s = socket.socket()
           s.settimeout(0.5)              # wait max 0.5 seconds
           result = s.connect_ex((ip,port))  # 0 = open
           s.close()
           return result == 0  

          

               

def identify_service(port):

    results={ 21 : 'FTP - try anonymous login',
        22 : 'SSH - try default credentials',
        23 : 'Telnet (DANGEROUS), uncrepted',
        25 : 'SMTP Mail server',
        53 : 'DNS - try zone transfer',
        80 : 'HTTP - check for web vulnerabilities',
        443 :'HTTPS - check SSL/TLS config',
        3306 : 'MySQL - try SQL injection',
        8080: ' HTTP ALTARNATE - check for admin penels', 
        8443: 'HTTPS altarnate - check for dev servers'}
    return results.get(port,'unknown')

print(' ')
print('WAIT it takes time  -_-')
print(f'[*] Scanning {end} ports.... ')
print(' ')  
for port in range (start,end+1):
       if is_port_open(ip, port):
             service = identify_service(port)
             print(f'[+] Port {port} -> {service}')

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename= input('[*] Enter file name:'+  timestamp)

# with open(filename, 'a') as f:
   
with open(filename, 'a') as f: 
    f.write(f'\nScan Summary\n')
    f.write(f'Target: {target} ({ip})\n')
    f.write(f'Range: {start}-{end}\n')
    f.write(f'Timeline: {timestamp}\n')
    f.write (f'Port {port} -> {service}\n')


is_port_open(ip,port)
identify_service(port)  

print('[+] Scan complete !')

    
    



print('='*80)
print('                            SCAN SUMARY')
print('='*80)
print(f'[*] Target: {target} ({ip})')
print(f'[*] Range: {start}-{end}')
print(f'[*] Report saved : {filename}')
print(f'[*] Timeline : {timestamp}')












