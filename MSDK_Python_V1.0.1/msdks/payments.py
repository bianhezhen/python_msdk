
import copy
from urllib import quote

def get_balance(sdk, params, cookie):
    """

    Wiki links::
        http://wiki.dev.4g.qq.com/v2/ZH_CN/router/index.html#!qq.md#2.1.1/auth/verify_login

    Usage::
        >>> sdk = Api('100703379', '4578e54fb3a1bd18e0681bc1c734514e', 'msdktest.qq.com')
        >>> get_balance(sdk, params, cookie)
    """
    method = 'GET'
    url_path = '/mpay/get_balance_m'

    cookie = copy.deepcopy(cookie)
    cookie.update(
        {
            'org_loc': quote(url_path, '')
        })
    return sdk.api_pay(url_path, params, cookie, method)


def pay_m(sdk, params, cookie):
    """
    """
    method = 'GET'
    url_path = '/mpay/pay_m'

    cookie = copy.deepcopy(cookie)
    cookie.update(
        {
            'org_loc': quote(url_path, '')
        })
    return sdk.api_pay(url_path, params, cookie, method)


def present_m(sdk, params, cookie):
    """
    """
    method = 'GET'
    url_path = '/mpay/present_m'

    cookie = copy.deepcopy(cookie)
    cookie.update(
        {
            'org_loc': quote(url_path, '')
        })
    return sdk.api_pay(url_path, params, cookie, method)
