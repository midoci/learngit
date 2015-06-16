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
    "city": "����",
    "province": "�㶫",
    "country": "�й�",
    "headimgurl":    "http://wx.qlogo.cn/mmopen/g3MonUZtNHkdmzicIlibx6iaFqAc56vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbERQQ4eMsv84eavHiaiceqxibJxCfHe/0",
   "subscribe_time": 1382694957,
   "unionid": " o6_bmasdasdsad6_2sgVt7hMZOPfL"
}
    '''
    # state = request.args.get("state")
    userinfo = {}
    try:
        # ��ȡaccess_token
        url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&redirect_uri&secret=%s&code=%s&grant_type=authorization_code'
        url = url % (appid, secret, code)
        response = urllib.urlopen(url)
        #ͨ�������url  (���ýӿ�)��ȡ��
        result = response.read().decode("utf8")
        response.close()
        #<----�������url �� result ��ȡ�� ��ȷʱ���ص�JSON���ݰ�  �������ʱҲ�᷵��json ���ݰ� ��Ҫ�ж� ��Ҫע��----->
        result_dict = json.loads(result)
        #<-----�ڶ���  over-------->
        # ʹ��access_token��ȡ�û���Ϣ
        #<--------��������ˢ�� ����б�Ҫ����ˢ�� �������Ҫ���е��Ĳ�------->
        #<--------���Ĳ�����ȡ�û���Ϣ(��scopeΪ snsapi_userinfo) ��ʼ --------->
        userinfo_url = 'https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s'
        userinfo_url = userinfo_url % (result_dict["access_token"], result_dict['openid'])
        response = urllib.urlopen(userinfo_url)
        userinfo = response.read().decode("utf8")
        #��ȡ���� ��ȷʱ���ص�JSON���ݰ�
        userinfo = json.loads(userinfo)
        #<--------���Ĳ�����-------------->
        response.close()
        #userinfo ��������û�����Ϣ
        return userinfo
    except Exception, e:
        print e
        return {}
        # �����û���Ϣ
