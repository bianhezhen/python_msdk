def verify_login(sdk, params, qs):

    method = 'POST'
    url_path = '/auth/verify_login'
    return sdk.api_msdk(url_path, params, qs, method)


def load_vip(sdk, params, qs):
    
    method = 'POST'
    url_path = '/profile/load_vip'
    return sdk.api_msdk(url_path, params, qs, method)
