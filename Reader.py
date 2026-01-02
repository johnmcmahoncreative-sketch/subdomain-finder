import os
from header_gen import header
FILENAME = "headers.txt"
def HeadFormat(filename: str = FILENAME):
    headers = {}

    search_paths = [
        os.getcwd(),                 # پوشه فعلی
        os.path.expanduser("~")      # home user
    ]

    for base in search_paths:
        for root, dirs, files in os.walk(base):
            if filename in files:
                path = os.path.join(root, filename)

                with open(path, "w") as f:
                    f.write(str(header))

                return headers   # ⬅️ بعد از پیدا شدن فایل خارج شو

    return headers  # اگر فایل پیدا نشد → dict خالی
def SubReader(file):
    pass

print(HeadFormat())