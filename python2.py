print('n30 search for vulnerabilities system..')
print ('======================================')
 
target = input('Enter IP or domain terget:')
port = input('Enter the target port:')
port = int(port)

print("========================================")
print('target:',target)
print('port:', port)

if port < 1 or port > 65535 :
    print ('unvalid port !!')
else:
    print ('valid port.')


def indentify_service(port):
  
  services = {
    '21':   "FTP — anonymous:anonymous login",
    '22':   "SSH — hydra brute force",
    '23':   "Telnet — capture with Wireshark",
    '25':   "SMTP — user enumeration + spoofing",
    '53':   "DNS — zone transfer (dig axfr)",
    '80':   "HTTP — SQLi, XSS, CSRF, file upload",
    '443':  "HTTPS — same as 80 + SSL vulns",
    '3306': "MySQL — SQLi + default root credentials",
    '8080': "HTTP Alt — admin panels, dev servers",
    '8443': "HTTPS Alt — forgotten services"
  }
  if port in services:
     print(f'target-> {port} service attack-> {services[port]}')
     with open('scan_results.txt','a') as f:
         f.write(f'port{port}- {services[port]}')
  else :
     print('unknown port...')
     with open('scan_results.txt','a') as f:
        f.write(f'port{port} - unknown')

  

while True:
   answer = input('coutinue yes or no:')
   if answer == 'yes':
     port = input('enter target port:')
     indentify_service(port)
     print('Summary...')
   elif answer == 'no':
      break
   else:
      break



