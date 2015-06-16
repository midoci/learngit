import json
import urllib
def getUnionID(appid, secret, code):
    '''
    :param code:
    :return:userinfo dict
    {
    "subscribe": 1,
    "openid": "o6_bmjrPTlm6_2sgVt7hMZOPfL2M",
    "nickname": "Band",
    "sex": 1,
    "language": "zh_CN",
    "city": "广州",
    "province": "广东",
    "country": "中国",
    "headimgurl":    "http://wx.qlogo.cn/mmopen/g3MonUZtNHkdmzicIlibx6iaFqAc56vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbERQQ4eMsv84eavHiaiceqxibJxCfHe/0",
   "subscribe_time": 1382694957,
   "unionid": " o6_bmasdasdsad6_2sgVt7hMZOPfL"
}
    '''
    # state = request.args.get("state")
    userinfo = {}
    try:
        # 换取access_token
        url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&redirect_uri&secret=%s&code=%s&grant_type=authorization_code'
        url = url % (appid, secret, code)
        response = urllib.urlopen(url)
        #通过打开这个url  (调用接口)获取到
        result = response.read().decode("utf8")
        response.close()
        #<----打开上面的url 后 result 获取数 正确时返回的JSON数据包  如果错误时也会返回json 数据包 需要判断 需要注意----->
        result_dict = json.loads(result)
        #<-----第二步  over-------->
        # 使用access_token获取用户信息
        #<--------第三步、刷新 如果有必要可以刷新 如果不需要进行第四步------->
        #<--------第四步、拉取用户信息(需scope为 snsapi_userinfo) 开始 --------->
        userinfo_url = 'https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s'
        userinfo_url = userinfo_url % (result_dict["access_token"], result_dict['openid'])
        response = urllib.urlopen(userinfo_url)
        userinfo = response.read().decode("utf8")
        #获取数据 正确时返回的JSON数据包
        userinfo = json.loads(userinfo)
        #<--------第四步结束-------------->
        response.close()
        #userinfo 里面就是用户的信息
        return userinfo
    except Exception, e:
        print e
        return {}
        # 保存用户信息
