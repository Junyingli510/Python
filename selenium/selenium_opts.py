from selenium import webdriver
# from selenium.webdriver.chrome.options import Options


class SeleniumOpts:
    def __init__(self):
        options = webdriver.ChromeOptions()
        arg_list = [
            "--no-sandbox",
            "--disable-impl-side-painting",
            "--disable-setuid-sandbox",
            "--disable-seccomp-filter-sandbox",
            "--disable-breakpad",
            "--disable-client-side-phishing-detection",
            "--disable-cast",
            "--disable-cast-streaming-hw-encoding",
            "--disable-cloud-import",
            "--disable-popup-blocking",
            "--ignore-certificate-errors",
            "--disable-session-crashed-bubble",
            "--disable-ipv6",
            "--allow-http-screen-capture",
            "--start-maximized"
        ]
        self.options = options
        self.arg_list = arg_list

    def __call__(self):
        return self.options

    def option_list(self):
        return self.arg_list

    def set_option(self, option):
        return 0


# ########## Additional options ########################################################################################


def build_chrome_options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.accept_untrusted_certs = True
    chrome_options.assume_untrusted_cert_issuer = True
    # chrome configuration
    # More: https://github.com/SeleniumHQ/docker-selenium/issues/89
    # And: https://github.com/SeleniumHQ/docker-selenium/issues/87
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-impl-side-painting")
    chrome_options.add_argument("--disable-setuid-sandbox")
    chrome_options.add_argument("--disable-seccomp-filter-sandbox")
    chrome_options.add_argument("--disable-breakpad")
    chrome_options.add_argument("--disable-client-side-phishing-detection")
    chrome_options.add_argument("--disable-cast")
    chrome_options.add_argument("--disable-cast-streaming-hw-encoding")
    chrome_options.add_argument("--disable-cloud-import")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-session-crashed-bubble")
    chrome_options.add_argument("--disable-ipv6")
    chrome_options.add_argument("--allow-http-screen-capture")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        + 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')

    return chrome_options
