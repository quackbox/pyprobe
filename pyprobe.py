import sys
import requests # using the requests library probably isn't the fastest way to go.

active_http = []
    
# function definitions
def ping_httpserver(dns):
    dns = dns.rstrip("\n")
    
    try:
        http_response = requests.head("http://" + dns, timeout=2.5)
    except:
        pass
    else:
        active_http.append("http://" + dns)
        print("http://" + dns)

def ping_httpsserver(dns):
    dns = dns.rstrip("\n")
    
    try:
        https_response = requests.head("https://" + dns, timeout=2.5)
    except:
        pass
    else:
        active_http.append("https://" + dns)
        print("https://" + dns)

# main
try:
    input_file = open(sys.argv[1], "r")
    output_file = sys.argv[2]
except:
    print("pyprobe.py expected arg[1], arg[2], got non-file or None!")
else:
    if sys.argv[1].lower() == "-h":
        print("pyprobe.py arg[1] input_file, arg[2] output_file. Example: python pyprobe.py ../test ../output")
        sys.exit()
    else:
        for line in input_file:
            line = line.rstrip("\n")
            ping_httpserver(line)
            ping_httpsserver(line)
        
        input_file.close()
        
        with open(output_file, "w") as write_to:
            for domain in active_http:
                write_to.write(domain + "\n")
