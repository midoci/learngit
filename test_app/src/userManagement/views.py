#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib
from django.http import HttpResponse
def hello (request):
    return HttpResponse('hello')


class Weixin():
    token = 'your_token'
    def validate(self, request):
        signature = request.REQUEST.get('signature', '')
        timestamp = request.REQUEST.get('timestamp', '')
        nonce = request.REQUEST.get('nonce',  '')
        tmp_str = hashlib.sha1(''.join(sorted([self.token, timestamp, nonce]))).hexdigest()
        if tmp_str == signature:
            return True
        return False
    def get(self, request):
        if self.validate(request):
            return HttpResponse(request.REQUEST.get('echostr', ''))
        #raise PermissionDenied