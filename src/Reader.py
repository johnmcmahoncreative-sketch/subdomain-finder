import os
FILENAME = "headers.txt"
FILENAME2 = "Subdomain.txt"
def FileFinder(filename: str = FILENAME):
    search_paths = [os.getcwd(), os.path.expanduser("~")]

    for base in search_paths:
        for root, dirs, files in os.walk(base):
            if filename in files:
                path = os.path.join(root, filename)
    return path 

def SubReader(filename:str = FILENAME2):
    data = []
    search_paths = [
        os.getcwd(),                 # پوشه فعلی
        os.path.expanduser("~")      # home user
    ]

    for base in search_paths:
        for root, dirs, files in os.walk(base):
            if filename in files:
                path = os.path.join(root, filename)
                with open(path, "r") as f:
                    data = f.readlines()
                    
    return data