#31
# print (' port detactor:')

# port = input('enter port number :')


# def port_detection (port):
    
#     services = { 
#                  '21':   "FTP — anonymous:anonymous login",
#     '22':   "SSH — hydra brute force",
#     '23':   "Telnet — capture with Wireshark",
#     '25':   "SMTP — user enumeration + spoofing",
#     '53':   "DNS — zone transfer (dig axfr)",
#     '80':   "HTTP — SQLi, XSS, CSRF, file upload",
#     '443':  "HTTPS — same as 80 + SSL vulns",
#     '3306': "MySQL — SQLi + default root credentials",
#     '8080': "HTTP Alt — admin panels, dev servers",
#     '8443': "HTTPS Alt — forgotten services"
#     }

#     if port in services:
#       print (f' {services[port]}')
#     else :
#        print('unknown')
    
#     with open('scan_result.txt','a') as f:
#           f.write(f'port{port}- {services[port]}')


# port_detection(port)

#36
# target = 22
# def scan(target):
    
#     results = {        '21':   "FTP — anonymous:anonymous login",
#     '22':   "SSH — hydra brute force",
#     '23':   "Telnet — capture with Wireshark",
#     '25':   "SMTP — user enumeration + spoofing",
#     '53':   "DNS — zone transfer (dig axfr)",
#     '80':   "HTTP — SQLi, XSS, CSRF, file upload",
#     '443':  "HTTPS — same as 80 + SSL vulns",
#     '3306': "MySQL — SQLi + default root credentials",
#     '8080': "HTTP Alt — admin panels, dev servers",
#     '8443': "HTTPS Alt — forgotten services" }

#     for target in range(1, 25):
#       results.append(target)

#     print(results)


# scan(target)

#37
port= input (' enter target port:')    
port = int(port)
while True:

  def results_port (port):
    results={  21:   "FTP — anonymous:anonymous login",
    22:   "SSH — hydra brute force",
    23:   "Telnet — capture with Wireshark",
    25:   "SMTP — user enumeration + spoofing",
    53:   "DNS — zone transfer (dig axfr)",
    80:   "HTTP — SQLi, XSS, CSRF, file upload",
    443:  "HTTPS — same as 80 + SSL vulns",
    3306: "MySQL — SQLi + default root credentials",
    8080: "HTTP Alt — admin panels, dev servers",
    8443: "HTTPS Alt — forgotten services"}
    

    if  port in results and port > 1 or port < 6553:
        print ('valid port')
        print(f'information port {results[port]}')
        
    else :
       print(f'unknown {port}')
  
  results_port(port)
  break
  

