# from src.os_detector import Detect
# from rich.console import Console
# from rich.panel import Panel
# from src.request import Request 
from src.request import Request
from src.header_gen import UA
from src.Reader import SubReader
from requests.exceptions import RequestException
from requests.exceptions import Timeout
from dns.exception import Timeout as t
def Req(domain):
    for i in SubReader():
        call = Request(domain,i.strip())
        if call.exists():
            try:
                print(f"Status code of :{i.strip()}:{call.get_req()}")
                print(f"Validation of IP:{call.Validate()}")
            except Timeout as err:
                print(f"An Error Occured!:{err}")
                continue
            except t as er:
                print(f"An Error Occured:{er}")
                continue
        else:
            continue
# console = Console()
# OS_info = Panel.fit(f"[blue]OS:{Detect()}")
# console.print(OS_info)
Req("trexmine.com")