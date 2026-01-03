import os
from src.header_gen import UA


FILENAME = "headers.txt"
FILENAME2 = "Subdomain.txt"

def HeadFormat(filename: str = FILENAME):
    call = UA()
    headers = header = {
    "Host": "",
    "User-Agent": f"{call.ua()}",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

    search_paths = [os.getcwd(), os.path.expanduser("~")]  # پوشه فعلی  # home user

    for base in search_paths:
        for root, dirs, files in os.walk(base):
            if filename in files:
                path = os.path.join(root, filename)

                with open(path, "w") as f:
                    f.write(str(header))

                return headers  # ⬅️ بعد از پیدا شدن فایل خارج شو

    return headers  # اگر فایل پیدا نشد → dict خالی
print(HeadFormat())

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