
#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
#=============================================================================
#
#     FileName: api.py
#         Desc: MSDK的API
#
#=============================================================================
'''

import copy
import json

from lib.sns_network import SNSNetwork
from lib.sns_sig import hmac_sha1_sig, mk_msdk_sig
from random import choice
from time import time
import urllib


try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


OPEN_HTTP_TRANSLATE_ERROR = 1801


class Api(object):
    _appid = 0
    _appkey = ''
    _api = None
    _format = 'json'
    _sdk_version = 'Python MSDK V1.0.0'

    def __init__(self, appid, appkey, iplist):
        super(Api, self).__init__()
        self._appid = appid
        self._appkey = appkey
        self._api = SNSNetwork(iplist)

    def api_msdk(self, url_path, params, qs, method='post', protocol='http'):
        '''
        调用接口，并将数据格式转化成json
        只需要传入pf, openid, openkey等参数即可，不需要传入sig
        format即使传xml也没有用，会被强制改为json
        '''
        cp_params = copy.deepcopy(params)

        cp_params.update(
            {
                'version': self._sdk_version,
            }
        )

        cp_params = json.dumps(cp_params)

        uri = SNSNetwork.mk_send_data(qs)
        url_path = url_path + '?' + uri
        url = '%s://%s%s' % (protocol, choice(self._api._iplist), url_path)

        self.print_request(url, cp_params, method)
        try:
            data = self._api.open(method, url_path, cp_params, '', protocol)
        except Exception, e:
            msg = 'exception occur.msg[%s], traceback[%s]' % (str(e), __import__('traceback').format_exc())
            return {'ret': OPEN_HTTP_TRANSLATE_ERROR, 'msg': msg}
        else:
            self.print_response(data)
            return json.loads(data)

    def api_pay(self, url_path, params, cookie, method='post', protocol='http'):
        '''
        调用接口，并将数据格式转化成json
        format即使传xml也没有用，会被强制改为json
        '''

        cp_params = copy.deepcopy(params)

        cp_params.update(
            {
                'appid': self._appid,
                'format': self._format,
            }
        )

        secret = '%s&' % self._appkey

        sig = hmac_sha1_sig(method, url_path, cp_params, secret)
        cp_params.update(
            {
                'sig': sig,
            }
        )

        cookie.update(
            {
            'org_loc': urllib.quote(url_path, ''),
            }
        )

        uri = 'http://%s%s' % (choice(self._api._iplist), url_path)

        self.print_request(uri, cp_params, method)

        try:
            data = self._api.open(method, url_path, cp_params, cookie, protocol)
        except Exception, e:
            msg = 'exception occur.msg[%s], traceback[%s]' % (str(e), __import__('traceback').format_exc())
            return {'ret': OPEN_HTTP_TRANSLATE_ERROR, 'msg': msg}
        else:
            self.print_response(data)
            return json.loads(data)

    @staticmethod
    def print_request(url, params, method):
        print "============= request info ================"
        print "method: %s" % (method)
        print "url: %s" % (url)
        print "params: "
        print params

    @staticmethod
    def print_response(params):
        print "============= response info ================"
        print params


def main():
    appid = 100703379
    appkey = '4578e54fb3a1bd18e0681bc1c734514e'
    iplist = ('msdktest.qq.com',)

    openid = '0EF80D52AE52324D51958FE6EDC3DBF3'
    openkey = '5FCBE90E15DF85CC093E3267481962E2'

    pf = 'desktop_m_qq-73213123-iap-1001-qq-1103557609-BDEDBB41B187CC7456BC9A85C5685C43'

    api = Api(appid, appkey, iplist)

    jdata = api.open('/v3/user/get_info', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    print jdata


if __name__ == '__main__':
    main()
