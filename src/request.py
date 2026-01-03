import requests
from dns.resolver import Resolver as dr
from Reader import HeadFormat
from utils.errors import SubError
from utils.colors import fg
from header_gen import header
from dns.exception import DNSException


class Request:
    def __init__(self, domain: str, subdomain):
        self.domain = domain
        self.sub = subdomain
        if not self.sub:
            raise SubError(fg.RED + "[!]An Error has occured!" + fg.RESET)

    def __URLBuilder(self):
        base = f"http://{self.sub}.{self.domain}"
        return base

    def __HostBuilder(self):
        base = f"{self.sub}.{self.domain}"
        if self.sub is None:
            base = f"{self.domain}"
        return base

    def get_req(self, header: dict | None = None, Timeout: int = 1):
        try:
            if not header:
                header = HeadFormat()
            url = self.__URLBuilder()
            res = requests.get(url, headers=header, timeout=Timeout)
            return res.status_code
        except requests.exceptions.RequestException as e:
            return fg.RED + "[!] An Error has occured: " + str(e) + fg.RESET

    def Validate(self, nameserver: list | None = None):
        try:
            if nameserver is None:
                nameserver = ["8.8.8.8"]
            call = dr()
            call.nameservers = nameserver
            res = call.resolve(self.__HostBuilder(), "A")
            return res.response
        except DNSException as e:
            return fg.RED + "[!] An Error has occured: " + str(e) + fg.RESET


d = Request("google.com", "mail")
print(d.get_req())
