'''





$$\   $$\                                        $$\                                   $$$$$$\                                          
$$ | $$  |                                       $$ |                                 $$  __$$\                                         
$$ |$$  / $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$$\ $$$$$$$\   $$$$$$\  $$$$$$$\         $$ /  \__| $$$$$$\ $$\    $$\  $$$$$$\   $$$$$$\  
$$$$$  / $$  __$$\ $$  __$$\  \____$$\ $$  _____|$$  __$$\  \____$$\ $$  __$$\ $$$$$$\\$$$$$$\   \____$$\\$$\  $$  |$$  __$$\ $$  __$$\ 
$$  $$<  $$ /  $$ |$$ |  $$ | $$$$$$$ |$$ /      $$ |  $$ | $$$$$$$ |$$ |  $$ |\______|\____$$\  $$$$$$$ |\$$\$$  / $$$$$$$$ |$$ |  \__|
$$ |\$$\ $$ |  $$ |$$ |  $$ |$$  __$$ |$$ |      $$ |  $$ |$$  __$$ |$$ |  $$ |       $$\   $$ |$$  __$$ | \$$$  /  $$   ____|$$ |      
$$ | \$$\\$$$$$$  |$$ |  $$ |\$$$$$$$ |\$$$$$$$\ $$ |  $$ |\$$$$$$$ |$$ |  $$ |       \$$$$$$  |\$$$$$$$ |  \$  /   \$$$$$$$\ $$ |      
\__|  \__|\______/ \__|  \__| \_______| \_______|\__|  \__| \_______|\__|  \__|        \______/  \_______|   \_/     \_______|\__|      
                                                                                                                                        
                                                                                                                                        
                                                                                                                                        





__Author__: 'Momoblydblk'
__InitialRelease__: 'https://github.com/momoblydblk/konachan-saver'
__Compatibility__: 'Python3'
'''
'''
Todos:
# Fix import pip


'''

import os
import pip
import platform
import importlib



global safe


def main():
    init()
    work()
    
def init():
    print('''


    $$\   $$\                                        $$\                                   $$$$$$\                                          
    $$ | $$  |                                       $$ |                                 $$  __$$\                                         
    $$ |$$  / $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$$\ $$$$$$$\   $$$$$$\  $$$$$$$\         $$ /  \__| $$$$$$\ $$\    $$\  $$$$$$\   $$$$$$\  
    $$$$$  / $$  __$$\ $$  __$$\  \____$$\ $$  _____|$$  __$$\  \____$$\ $$  __$$\ $$$$$$\\$$$$$$\   \____$$\\$$\  $$  |$$  __$$\ $$  __$$\ 
    $$  $$<  $$ /  $$ |$$ |  $$ | $$$$$$$ |$$ /      $$ |  $$ | $$$$$$$ |$$ |  $$ |\______|\____$$\  $$$$$$$ |\$$\$$  / $$$$$$$$ |$$ |  \__|
    $$ |\$$\ $$ |  $$ |$$ |  $$ |$$  __$$ |$$ |      $$ |  $$ |$$  __$$ |$$ |  $$ |       $$\   $$ |$$  __$$ | \$$$  /  $$   ____|$$ |      
    $$ | \$$\\$$$$$$  |$$ |  $$ |\$$$$$$$ |\$$$$$$$\ $$ |  $$ |\$$$$$$$ |$$ |  $$ |       \$$$$$$  |\$$$$$$$ |  \$  /   \$$$$$$$\ $$ |      
    \__|  \__|\______/ \__|  \__| \_______| \_______|\__|  \__| \_______|\__|  \__|        \______/  \_______|   \_/     \_______|\__|      



        ''')
    print("Please wait for Konachan-Saver imports necessary modules.")
    
    #Try to import the necessary parts, or install them.
    libs = ['requests','avalon_framework','bs4','urllib']
    
    def import_m(p):
        try:
            import p 
        except:
            pip.main(['install', p])
            globals()[p] = importlib.import_module(p)
    for i in libs:
        import_m(i)
        print("Done importing %s." % i)
    print("\n\n\nDone importing necessary parts.")

    try:
        os.makedirs(".\Download\Safe")
        os.makedirs(".\Download\\NSFW")
    except (OSError, IOError) as e:
        pass
    print()

    
def work():
    print('Please input the link to the page from Konachan which has the picture in it.')
    url = input('Input:')
    analyze(url)

def analyze(url):
    page = requests.get(url).content
    soup = bs4.BeautifulSoup(page, "html.parser")
    element = soup.find_all(id="highres")
    tag = element[0]
    photoURL = tag["href"]
    if photoURL[0] == '/':
        photoURL = 'https:' + photoURL
    elementSafe = soup.find_all(class_="vote-desc")[0]
    elementSafe = elementSafe.parent
    safe = elementSafe.get_text()
    if safe.lower() == "rating: safe ":
        safe = True
    else:
        safe = False
    download(photoURL,safe)

def download(url, safe):
    
    filename = url
    filename = filename.split('/')[-1]
    def cbk(a, b, c):
        per = 100.0 * a * b / c 
        if per > 100: 
            per = 100 
        print ('%.2f%%' % per)
    if safe:
        filePath = '.\Download\safe\\' + filename
        print('Find your file here: %s' % filePath)
    else:
        filePath = '.\Download\\NSFW\\' + filename
        print('Find your file here: %s' % filePath)
    urllib.request.urlretrieve(url,filePath,cbk)
      
        if __name__ == "__main__":
        work()
    else:
        exit()

if __name__ == "__main__":
    main()