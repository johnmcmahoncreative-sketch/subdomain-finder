import platform
from utils.errors import OSDetectErr
from utils.colors import fg
def Detect():
    call = platform.system()
    if call == "Linux":
        return "Linux"
    elif call == "Windows":
        return "Windows"
    elif call == "Darwin":
        return "Mac"
    else:
        raise OSDetectErr(fg.RED+"[!]Invalid OS Detected")