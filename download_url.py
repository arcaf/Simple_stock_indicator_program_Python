import urllib.request
import urllib.error
import sys
def downloading_url(url):
    while True:
        try:
            result = []
            print('Downloading stock information...')
            table = urllib.request.urlopen(url)
            response = table.read()
            content = response.decode(encoding='utf-8').splitlines()
            
            for line in content:
                result.append(line.split(','))
            
            return result

            break
        except urllib.error.HTTPError:
            print("Sorry the ticker information you have provided does not represent \nany company, program shutting down")
            sys.exit(0)
        except urllib.error.URLError:
            print("There seems to be a problem with the internet connection, \nprogram shutting down...")
            sys.exit(0)
        
