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
