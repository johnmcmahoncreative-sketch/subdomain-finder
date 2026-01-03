import platform
from src.utils.errors import OSDetectErr
from src.utils.colors import fg


def Detect():
    call = platform.system()
    if call == "Linux":
        return "Linux"
    elif call == "Windows":
        return "Windows"
    elif call == "Darwin":
        return "Mac"
    else:
        raise OSDetectErr(fg.RED + "[!]Invalid OS Detected")