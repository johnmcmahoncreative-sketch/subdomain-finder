# from src.os_detector import Detect
# from rich.console import Console
# from rich.panel import Panel
# from src.request import Request 
from src.request import Request
from src.header_gen import UA
from src.Reader import SubReader
from requests.exceptions import RequestException
call = Request("linka.ir","api")
print(call.get_req( ))
# console = Console()
# OS_info = Panel.fit(f"[blue]OS:{Detect()}")
# console.print(OS_info)
