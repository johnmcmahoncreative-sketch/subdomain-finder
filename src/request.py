import requests
from dns.resolver import Resolver as dr
from src.Reader import HeadFormat
from src.utils.errors import SubError
from src.utils.colors import fg
from dns.exception import DNSException
import socket

class Request:
    def __init__(self, domain: str, subdomain):
        self.domain = domain
        self.sub = subdomain
        if not self.sub:
            raise SubError(fg.RED + "[!]An Error has occured!") + fg.RESET

    def __URLBuilder(self):
        base = f"http://{self.sub}.{self.domain}"
        return base

    def __HostBuilder(self):
        base = f"{self.sub}.{self.domain}"
        if self.sub is None:
            base = f"{self.domain}"
        return base

    def get_req(self, header: dict|None = None, Timeout: int = 10):
        try:
            # if not header:
            #     header = HeadFormat()
            url = self.__URLBuilder()
            res = requests.get(url, timeout=Timeout)
            return res.status_code
        except requests.exceptions.RequestException as e:
            return fg.RED + "[!] An Error has occured: " + str(e) + fg.RESET

    def Validate(self, nameserver: list|None = None):
        try:
            if nameserver is None:
                nameserver = ["8.8.8.8"]
            call = dr()
            call.nameservers = nameserver
            res = call.resolve(self.__HostBuilder(), "A")
            return res
        except DNSException as e:
            return fg.RED + "[!] An Error has occured: " + str(e) + fg.RESET
    def exists(self):
        try:
            sock = socket.gethostbyname(self.__HostBuilder())
            return True
        except socket.gaierror:
            return False
    # def close(self):
    #     self.get_req().