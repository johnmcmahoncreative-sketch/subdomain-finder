import random

CHROME_VERSIONS = ["120.0.0.0", "121.0.0.0", "122.0.0.0"]
FIREFOX_VERSIONS = ["118.0", "119.0", "120.0"]
EDGE_VERSIONS = ["120.0.2210.91", "121.0.2277.83"]
OPERA_VERSIONS = ["105.0.0.0", "106.0.0.0"]
BRAVE_VERSIONS = CHROME_VERSIONS

WINDOWS_VERSIONS = ["10.0", "11.0"]
MAC_VERSIONS = ["13_6", "14_0", "14_1"]
ANDROID_VERSIONS = ["11", "12", "13", "14"]
IOS_VERSIONS = ["16_6", "17_0", "17_1"]

class UA():
    def windows_chrome(self):
        return (
            f"Mozilla/5.0 (Windows NT {random.choice(WINDOWS_VERSIONS)}; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            f"Chrome/{random.choice(CHROME_VERSIONS)} Safari/537.36"
        )

    def windows_edge(self):
        return (
            f"Mozilla/5.0 (Windows NT {random.choice(WINDOWS_VERSIONS)}; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            f"Chrome/{random.choice(CHROME_VERSIONS)} "
            f"Edg/{random.choice(EDGE_VERSIONS)}"
        )

    def windows_firefox(self):
        v = random.choice(FIREFOX_VERSIONS)
        return (
            f"Mozilla/5.0 (Windows NT {random.choice(WINDOWS_VERSIONS)}; Win64; x64; rv:{v}) "
            f"Gecko/20100101 Firefox/{v}"
        )

    def linux_chrome(self):
        return (
            "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            f"Chrome/{random.choice(CHROME_VERSIONS)} Safari/537.36"
        )

    def linux_firefox(self):
        v = random.choice(FIREFOX_VERSIONS)
        return (
            f"Mozilla/5.0 (X11; Linux x86_64; rv:{v}) "
            f"Gecko/20100101 Firefox/{v}"
        )

    def mac_safari(self):
        return (
            f"Mozilla/5.0 (Macintosh; Intel Mac OS X {random.choice(MAC_VERSIONS)}) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) "
            "Version/17.0 Safari/605.1.15"
        )

    def mac_chrome(self):
        return (
            f"Mozilla/5.0 (Macintosh; Intel Mac OS X {random.choice(MAC_VERSIONS)}) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            f"Chrome/{random.choice(CHROME_VERSIONS)} Safari/537.36"
        )

    # ---------- MOBILE ----------

    def android_chrome(self):
        return (
            f"Mozilla/5.0 (Linux; Android {random.choice(ANDROID_VERSIONS)}; Mobile) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            f"Chrome/{random.choice(CHROME_VERSIONS)} Mobile Safari/537.36"
        )

    def ios_safari(self):
        return (
            f"Mozilla/5.0 (iPhone; CPU iPhone OS {random.choice(IOS_VERSIONS)} like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) "
            "Version/17.0 Mobile/15E148 Safari/604.1"
        )

    def ios_firefox(self):  # Firefox on iOS uses WebKit
        return (
            f"Mozilla/5.0 (iPhone; CPU iPhone OS {random.choice(IOS_VERSIONS)} like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) "
            "FxiOS/120.0 Mobile/15E148 Safari/605.1.15"
        )
    def ua(self,):
        generators = [
            self.windows_chrome,
            self.windows_edge,
            self.windows_firefox,
            self.linux_chrome,
            self.linux_firefox,
            self.mac_chrome,
            self.mac_safari,
            self.android_chrome,
            self.ios_safari,
            self.ios_firefox
        ]
        return random.choice(generators)()
ua_gen = UA()
header = {
    "Host":"",
    "User-Agent":f"{ua_gen.ua()}",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

