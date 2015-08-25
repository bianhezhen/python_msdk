#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
#=============================================================================
#
#     FileName: sample_test.py
#         Desc:
#
#=============================================================================
'''

from msdks.api import Api
import time

from msdks.msdks import verify_login, \
        load_vip, qqprofile, qqfriends_detail, get_gift

from msdks.payments import get_balance, pay_m, present_m

from msdks.lib.sns_sig import mk_msdk_sig


import sys
sys.path.append('../msdks')

appid = 1450001744
appkey = 'xAuVk9sPZXTpdYLH'

iplist = ('msdktest.qq.com',)

openid = '0EF80D52AE52324D51958FE6EDC3DBF3'
openkey ='5FCBE90E15DF85CC093E3267481962E2'

userip = '127.0.0.1'
ts = int(time.time())

encode = 1

# 支付接口票据, 从android/ios移动客户端应用登录得到
pay_token='28BE9293E1E1F61714CDD198C57FC7A9'
pf='desktop_m_qq-73213123-iap-1001-qq-1103557609-BDEDBB41B187CC7456BC9A85C5685C43'
pfkey= 'ef166c03f806bc3af2429d423e89ae05'

# 支付分区
zoneid = 60000001 # 注意是分区ID，默认为1，如果在平台配置了分区需要传入对应的分区ID！


flag = 1

amt = 50

discountid = 'UM140711160321549'
giftid = '1372507615PID201407111603215575'
presenttimes = 500


def main():
    sdk = Api(appid, appkey, iplist)
    qs = {
        'appid': appid,
        'timestamp': ts,
        'sig': mk_msdk_sig(appkey, ts),
        'encode': 1,
        'openid': openid,
    }

    # Android平台
    #cookie = {
    #    'session_id': 'openid',
    #    'session_type': 'kp_actoken',
    #    'org_loc': '',
    #}

    # IOS平台
    cookie = {
        'session_id': 'hy_gameid',
        'session_type': 'st_dummy',
        'org_loc': '',
    }


    params = {
        'appid': appid,
        'openid': openid,
        'openkey': openkey,
        'useip': userip,
    }
    verify_login(sdk, params, qs)

    params = {
        'appid': appid,
        'openid': openid,
        'login': 2,
        'uin': 0,
        'vip': 13,
        'accessToken': openkey,
    }
    # load_vip(sdk, params)

    params = {
        'appid': '',
        'openid': openid,
        'accessToken': openkey,
    }
    # qqprofile(sdk, params)

    params = {
        'appid': '',
        'openid': openid,
        'accessToken': openkey,
        'flag': flag
    }
    # qqfriends_detail(sdk, params)

    params = {
        'appid': '',
        'openid': openid,
    }
    # get_gift(sdk, params)

    params = {
        'appid': appid,
        'openid': openid,
        'openkey': openkey,
        'pay_token': pay_token,
        'ts': ts,
        'pf': pf,
        'pfkey': pfkey,
        'zoneid': zoneid,
    }
    # get_balance(sdk, params, cookie)

    params = {
        'appid': appid,
        'openid': openid,
        'openkey': openkey,
        'pay_token': pay_token,
        'ts': ts,
        'pf': pf,
        'pfkey': pfkey,
        'zoneid': zoneid,
        'amt' : amt
    }

    # pay_m(sdk, params, cookie)

    params = {
        'appid': appid,
        'openid': openid,
        'openkey': openkey,
        'pay_token': pay_token,
        'ts': ts,
        'pf': pf,
        'pfkey': pfkey,
        'zoneid': zoneid,
        'discountid':discountid,
        'giftid': giftid,
        'presenttimes': presenttimes
    }

    # present_m(sdk, params, cookie)




if __name__ == '__main__':
    main()
