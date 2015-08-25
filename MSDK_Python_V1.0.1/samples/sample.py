#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
#=============================================================================
#
#     FileName: sample.py
#
#=============================================================================
'''

from msdks.api import Api
import time

from msdks.msdks import verify_login, load_vip, qqprofile
from msdks.payments import get_balance

import sys
sys.path.append('../msdks')


appid = 'your appid'
appkey = 'your appkey'

iplist = ('msdktest.qq.com',)

openid = 'openid from mobile msdk'
openkey ='openkey from mobile msdk'

userip = 'client ip'
ts = int(time.time())

encode = 1

# 支付接口票据, 从android/ios移动客户端应用登录得到
pay_token='pay_token from mobile msdk';
pf='pf from mobile msdk';
pfkey= 'pfkey from mobile msdk';

# 支付分区
zoneid=''; # 注意是分区ID，默认为1，如果在平台配置了分区需要传入对应的分区ID！


# 一些其他参数
vip = ''



def main():
    sdk = Api(appid, appkey, iplist)
    qs = {
        'appid': appid,
        'timestamp': ts,
        'sig': mk_msdk_sig(appkey, ts),
        'encode': 1,
        'openid': openid,
    }

    cookie = {
        'session_id': 'openid',
        'session_type': 'kp_actoken',
        'org_loc': '',
    }

    params = {
        'appid': appid,
        'openid': openid,
        'openkey': openkey,
        'useip': userip,
    }
    verify_login(sdk, params, qs)

if __name__ == '__main__':
    main()
