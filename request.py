import requests
from dns.resolver import Resolver as dr
from Reader import HeadFormat
from utils.errors import SubError
from utils.colors import fg
from header_gen import header
class Request():
    def __init__(self,domain:str,subdomain):
          self.domain = domain
          self.sub = subdomain
          if not self.sub:
                raise SubError(fg.RED+"[!]An Error has occured!")
    def __URLBuilder(self):
            base = f"http://{self.sub}.{self.domain}"
            return base
    def __HostBuilder(self):
        base = f"{self.sub}.{self.domain}"
        if self.sub is None:
            base = f"{self.domain}" 
        return base
    def get_req(self,header:dict = None, Timeout:int = 1):
        if not header:
            header = HeadFormat()
        url = self.__URLBuilder()
        res = requests.get(url,headers=header,timeout=Timeout)
        return res.status_code
    def Validate(self,nameserver:list = None):
        if nameserver is None:
            nameserver = ['8.8.8.8']
        call = dr()
        call.nameservers = nameserver
        res = call.resolve(self.__HostBuilder(),'A')
        return res.response

d = Request("trexmine.com","api")
print(d.get_req())