from src.Reader import SubReader
from src.request import Request
from requests.exceptions import RequestException

def Req(domain, headfile=None, timeout=10):
    for sub in SubReader():
        sub = sub.strip()  # Remove whitespace/newlines
        if not sub:
            continue
        try:
            call = Request(domain=domain, subdomain=sub)
            response = call.get_req(header=headfile, timeout=timeout)
            if response:
                return response
        except RequestException as err:
            print(f"[!] Could not reach {sub}.{domain}: {err}")
            continue
    return None

# Test
result = Req("trexmine.com")
print(result)
