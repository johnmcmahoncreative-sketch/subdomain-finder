# from src.os_detector import Detect
# from rich.console import Console
# from rich.panel import Panel
# from src.request import Request 
from src.request import Request
from src.header_gen import UA
from src.Reader import SubReader
from requests.exceptions import RequestException
class Req():
    def __init__(self,domain):
        self.domain = domain
    def Headergen(self):
        call = UA()
        headers = {
            "Host": f"{self}",
            "User-Agent": f"{call.ua()}",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }
        return headers

    def Req(self,domain,header=Headergen(),timeout:int = 10):
            for i in SubReader():
                try:
                    call = Request(domain=domain,subdomain=i)
                    respone = call.get_req(header=header,Timeout=10)
                    print(respone)
                except RequestException as err:
                    continue

# console = Console()
# OS_info = Panel.fit(f"[blue]OS:{Detect()}")
# console.print(OS_info)
print(Req("trexmine.com"))