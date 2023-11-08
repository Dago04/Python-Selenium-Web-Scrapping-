from twocaptcha import TwoCaptcha
import sys
import os


def solveRecaptcha(sitekey, url):
    # https://github.com/2captcha/2captcha-python

    sys.path.append(os.path.dirname(
        os.path.dirname(os.path.realpath(__file__))))

    api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
            sitekey=sitekey,
            url=url)

    except Exception as e:
        print(e)

    else:
        return result
