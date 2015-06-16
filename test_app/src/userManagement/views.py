#!/usr/bin/env python
# -*- coding:utf-8 -*-
from _models.models import *
from django.http import HttpResponse
from django.shortcuts import redirect


def hello (request):
    user_info = {}
    state = request.args.get("state")
    return index(openid=user_info["openid"], key=state)

def index(request,openid=None, key=None):
    if not openid:
        openid = request.objects.get("openid")   #如果没有传过openid  那么 获取这个id
    user = UserInfo.objects.filter(open_id=openid) #获取第一个user_info 
    if not user:#如果没获取到 那么进行授权 获取user
        url = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s&response_type=code&scope=snsapi_userinfo&state=%s#wechat_redirect'
        url = url % (APPID, "http://p1.midoci.com:8080/hello", key)
        return redirect(url)#重定向到这个页面 
    