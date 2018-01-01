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
'''
'''
Todos:
# Fix import pip


'''

import os
import pip
import platform
import importlib

'''going to be deleted'''
import bs4, requests


global windows, safe
windows = True
def systemPrint(msg):
    if windows:
        print(msg)
    else:
        avalon_framework

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
    libs = ['requests','avalon_framework','bs4','errno']
    if platform.system().lower() == "windows":
        libs.pop(1)
    else:
        windows = False

    def import_m(p):
        try:
            import p 
        except:
            pip.main(['install', p])
            globals()[p] = importlib.import_module(p)
    for i in libs:
        import_m(i)
        print("Done importing %s." % i)

    try:
        os.makedirs('/Download/Safe')
        os.makedirs('/Download/NSFW')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    
    systemPrint("\n\n\nDone importing necessary parts.")
    
def work():
    systemPrint('Please input the link to the page which has the picture from Konachan.')
    url = raw_input('Input:')
    analyze(url)

def analyze(url):
    page = requests.get(url).content
    soup = bs4.BeautifulSoup(page, "html.parser")
    element = soup.find_all(id="highres")
    tag = element[0]
    photoURL = tag["href"]
    elementSafe = soup.find_all(class_="vote-desc")[0]
    elementSafe = elementSafe.parent
    safe = elementSafe.get_text()
    if safe.lower() == "rating: safe ":
        safe = True
    else:
        safe = False
    download(photoURL,safe)

def download(url,safe):
    filename = url
    filename = filename.split('/')[-1]
    img_data = requests.get(url).content
    if safe:
        f = open('/Download/Safe/%s' % filename, 'w')
    else:
        f = open('/Download/NSFW/%s' % filename, 'wb')
    f.write(img_data)
    f.close()
    if __name__ == "__main__":
        work()
    else:
        exit()



if __name__ == "__main__":
    main()