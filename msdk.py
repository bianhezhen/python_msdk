
def verify_login(sdk, params, qs):
    """

    Wiki links::
        http://wiki.dev.4g.qq.com/v2/ZH_CN/router/index.html#!qq.md#2.1.1/auth/verify_login

    Usage::
        >>> sdk = Api('100703379', '4578e54fb3a1bd18e0681bc1c734514e', 'msdktest.qq.com')
        >>> verify_login(sdk, params, qs)
    """
    method = 'POST'
    url_path = '/auth/verify_login'
    return sdk.api_msdk(url_path, params, qs, method)


def load_vip(sdk, params, qs):
    """

    Wiki links::
        http://wiki.dev.4g.qq.com/v2/ZH_CN/router/index.html#!qq.md#2.4.1_/profile/load_vip

    Usage::
        >>> sdk = Api('100703379', '4578e54fb3a1bd18e0681bc1c734514e', 'msdktest.qq.com')
        >>> load_vip(sdk, params, qs)
    """
    method = 'POST'
    url_path = '/profile/load_vip'
    return sdk.api_msdk(url_path, params, qs, method)


def qqprofile(sdk, params, qs):
    """

    Wiki links::
        http://wiki.dev.4g.qq.com/v2/ZH_CN/router/index.html#!qq.md#2.4.1_/profile/load_vip

    Usage::
        >>> sdk = Api('100703379', '4578e54fb3a1bd18e0681bc1c734514e', 'msdktest.qq.com')
        >>> qqprofile(sdk, params, qs)
    """
    method = 'POST'
    url_path = '/relation/qqprofile'
    return sdk.api_msdk(url_path, params, qs, method)


def qqfriends_detail(sdk, params, qs):
    """

    Wiki links::
        http://wiki.dev.4g.qq.com/v2/ZH_CN/router/index.html#!qq.md#2.3.2/relation/qqfriends_detail

    Usage::
        >>> sdk = Api('100703379', '4578e54fb3a1bd18e0681bc1c734514e', 'msdktest.qq.com')
        >>> qqfriends_detail(sdk, params, qs)
    """
    method = 'POST'
    url_path = '/relation/qqfriends_detail'
    return sdk.api_msdk(url_path, params, qs, method)


def get_gift(sdk, params, qs):
    """

    Wiki links::
        http://wiki.dev.4g.qq.com/v2/ZH_CN/router/index.html#!qq.md#2.4.2_/profile/get_gift

    Usage::
        >>> sdk = Api('100703379', '4578e54fb3a1bd18e0681bc1c734514e', 'msdktest.qq.com')
        >>> get_gift(sdk, params, qs)
    """
    method = 'POST'
    url_path = '/profile/get_gift'
    return sdk.api_msdk(url_path, params, qs, method)


def get_wifi(sdk, params, qs):
    """

    Wiki links::
        http://wiki.dev.4g.qq.com/v2/ZH_CN/router/index.html#!qq.md#2.4.2_/profile/get_gift

    Usage::
        >>> sdk = Api('100703379', '4578e54fb3a1bd18e0681bc1c734514e', 'msdktest.qq.com')
        >>> get_wifi(sdk, params, qs)
    """
    method = 'POST'
    url_path = '/profile/get_wifi'
    return sdk.api_msdk(url_path, params, qs, method)


def qqscore_batch(sdk, params, qs):
    """

    Wiki links::
        http://wiki.dev.4g.qq.com/v2/ZH_CN/router/index.html#!qq.md#2.4.2_/profile/get_gift

    Usage::
        >>> sdk = Api('100703379', '4578e54fb3a1bd18e0681bc1c734514e', 'msdktest.qq.com')
        >>> qqscore_batch(sdk, params, qs)
    """
    method = 'POST'
    url_path = '/profile/qqscore_batch'
    return sdk.api_msdk(url_path, params, qs, method)


def wx_refresh_token(sdk, params, qs):
    """

    Wiki links::
        http://wiki.dev.4g.qq.com/v2/ZH_CN/router/index.html#!qq.md#2.4.2_/profile/get_gift

    Usage::
        >>> sdk = Api('100703379', '4578e54fb3a1bd18e0681bc1c734514e', 'msdktest.qq.com')
        >>> wx_refresh_token(sdk, params, qs)
    """
    method = 'POST'
    url_path = '/auth/refresh_token'
    return sdk.api_msdk(url_path, params, qs, method)


def wx_check_token(sdk, params, qs):
    """

    Wiki links::
        http://wiki.dev.4g.qq.com/v2/ZH_CN/router/index.html#!qq.md#2.4.2_/profile/get_gift

    Usage::
        >>> sdk = Api('100703379', '4578e54fb3a1bd18e0681bc1c734514e', 'msdktest.qq.com')
        >>> wx_check_token(sdk, params, qs)
    """
    method = 'POST'
    url_path = '/auth/check_token'
    return sdk.api_msdk(url_path, params, qs, method)


def wxfriends_profile(sdk, params, qs):
    """

    Wiki links::
        http://wiki.dev.4g.qq.com/v2/ZH_CN/router/index.html#!qq.md#2.4.2_/profile/get_gift

    Usage::
        >>> sdk = Api('100703379', '4578e54fb3a1bd18e0681bc1c734514e', 'msdktest.qq.com')
        >>> wxfriends_profile(sdk, params, qs)
    """
    method = 'POST'
    url_path = '/relation/wxfriends_profile'
    return sdk.api_msdk(url_path, params, qs, method)


def wxprofile(sdk, params):
    """

    Wiki links::
        http://wiki.dev.4g.qq.com/v2/ZH_CN/router/index.html#!qq.md#2.4.2_/profile/get_gift

    Usage::
        >>> sdk = Api('100703379', '4578e54fb3a1bd18e0681bc1c734514e', 'msdktest.qq.com')
        >>> wxprofile(sdk, params)
    """
    method = 'POST'
    url_path = '/relation/wxprofile'
    return sdk.api_msdk(url_path, params, qs, method)


def wxfriends(sdk, params, qs):
    """

    Wiki links::
        http://wiki.dev.4g.qq.com/v2/ZH_CN/router/index.html#!qq.md#2.4.2_/profile/get_gift

    Usage::
        >>> sdk = Api('100703379', '4578e54fb3a1bd18e0681bc1c734514e', 'msdktest.qq.com')
        >>> wxfriends(sdk, params, qs)
    """
    method = 'POST'
    url_path = '/relation/wxfriends'
    return sdk.api_msdk(url_path, params, qs, method)


def wxuserinfo(sdk, params):
    """

    Wiki links::
        http://wiki.dev.4g.qq.com/v2/ZH_CN/router/index.html#!qq.md#2.4.2_/profile/get_gift

    Usage::
        >>> sdk = Api('100703379', '4578e54fb3a1bd18e0681bc1c734514e', 'msdktest.qq.com')
        >>> wxuserinfo(sdk, params)
    """
    method = 'POST'
    url_path = '/relation/wxuserinfo'
    return sdk.api_msdk(url_path, params, method)


def wxscore(sdk, params, qs):
    """

    Wiki links::
        http://wiki.dev.4g.qq.com/v2/ZH_CN/router/index.html#!qq.md#2.4.2_/profile/get_gift

    Usage::
        >>> sdk = Api('100703379', '4578e54fb3a1bd18e0681bc1c734514e', 'msdktest.qq.com')
        >>> get_gift(sdk, params, qs)
    """
    method = 'POST'
    url_path = '/profile/wxscore'
    return sdk.api_msdk(url_path, params, qs, method)


def wxbattle_report(sdk, params, qs):
    """

    Wiki links::
        http://wiki.dev.4g.qq.com/v2/ZH_CN/router/index.html#!qq.md#2.4.2_/profile/get_gift

    Usage::
        >>> sdk = Api('100703379', '4578e54fb3a1bd18e0681bc1c734514e', 'msdktest.qq.com')
        >>> wxbattle_report(sdk, params, qs)
    """
    method = 'POST'
    url_path = '/profile/wxbattle_report'
    return sdk.api_msdk(url_path, params, qs, method)


def wxget_vip(sdk, params, qs):
    """

    Wiki links::
        http://wiki.dev.4g.qq.com/v2/ZH_CN/router/index.html#!qq.md#2.4.2_/profile/get_gift

    Usage::
        >>> sdk = Api('100703379', '4578e54fb3a1bd18e0681bc1c734514e', 'msdktest.qq.com')
        >>> get_gift(sdk, params, qs)
    """
    method = 'POST'
    url_path = '/profile/get_gift'
    return sdk.api_msdk(url_path, params, qs, method)


def guest_check_token(sdk, params, qs):
    """

    Wiki links::
        http://wiki.dev.4g.qq.com/v2/ZH_CN/router/index.html#!qq.md#2.4.2_/profile/get_gift

    Usage::
        >>> sdk = Api('100703379', '4578e54fb3a1bd18e0681bc1c734514e', 'msdktest.qq.com')
        >>> guest_check_token(sdk, params, qs)
    """
    method = 'POST'
    url_path = '/auth/guest_check_token'
    return sdk.api_msdk(url_path, params, qs, method)


def share_qq(sdk, params, qs):
    """

    Wiki links::
        http://wiki.dev.4g.qq.com/v2/ZH_CN/router/index.html#!qq.md#2.4.2_/profile/get_gift

    Usage::
        >>> sdk = Api('100703379', '4578e54fb3a1bd18e0681bc1c734514e', 'msdktest.qq.com')
        >>> wxget_vip(sdk, params, qs)
    """
    method = 'POST'
    url_path = '/share/qq'
    return sdk.api_msdk(url_path, params, qs, method)


def upload_wx(sdk, params, qs):
    """

    Wiki links::
        http://wiki.dev.4g.qq.com/v2/ZH_CN/router/index.html#!qq.md#2.4.2_/profile/get_gift

    Usage::
        >>> sdk = Api('100703379', '4578e54fb3a1bd18e0681bc1c734514e', 'msdktest.qq.com')
        >>> upload_wx(sdk, params, qs)
    """
    method = 'POST'
    url_path = '/share/upload_wx'
    return sdk.api_msdk(url_path, params, qs, method)


def share_wx(sdk, params, qs):
    """

    Wiki links::
        http://wiki.dev.4g.qq.com/v2/ZH_CN/router/index.html#!qq.md#2.4.2_/profile/get_gift

    Usage::
        >>> sdk = Api('100703379', '4578e54fb3a1bd18e0681bc1c734514e', 'msdktest.qq.com')
        >>> wxget_vip(sdk, params, qs)
    """
    method = 'POST'
    url_path = '/share/wx'
    return sdk.api_msdk(url_path, params, qs, method)
