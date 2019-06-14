import json
import requests


class ProxyLogin(object):

    def weibo_url(self, client_id, redirect_url):
        """
        WEIBO URL
        :param client_id: your weibo appID
        :param redirect_url: your weibo redirect_url
        :return: WEIBO URL
        """
        weibo = "https://api.weibo.com/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_uri}".format(
            client_id=client_id, redirect_uri=redirect_url)
        return weibo

    def qq_url(self, client_id, redirect_url):
        """
        QQ URL
        :param client_id: your qq appID
        :param redirect_url: your qq redirect_url
        :return: QQ URL
        """
        qq = "https://graph.qq.com/oauth2.0/authorize?response_type=code&client_id={client_id}\
        &redirect_uri={redirect_uri}&scope=get_user_info".format(client_id=client_id, redirect_uri=redirect_url)
        return qq

    def weixin_url(self, client_id, redirect_url):
        """
        WEIXIN URL
        :param client_id: your weixin appID
        :param redirect_url: your weixin redirect_url
        :return: WEIXIN URL
        """
        weixin = "https://open.weixin.qq.com/connect/qrconnect?appid={client_id}&redirect_uri={redirect_uri}\
        &response_type=code&scope=SCOPE&state=STATE#wechat_redirect".format(
            client_id=client_id, redirect_uri=redirect_url
        )
        return weixin

    def weibo(self, client_id, client_secret, url, code):
        """
        微博登录
        :param client_id: appID
        :param client_secret: appSecret
        :param url:  your weibo redirect_url
        :param code: 从微博服务器得到code
        :return: 用户名
        """
        get_access_token_url = "https://api.weibo.com/oauth2/access_token"

        get_message_url = "https://api.weibo.com/2/users/show.json"

        response = requests.post(url=get_access_token_url, data={
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": url,
            "code": code
        }).text

        response_loads = json.loads(response)
        access_token = response_loads['access_token']
        uid = response_loads['uid']
        # 请求得到用户信息

        info_message = requests.get(url=get_message_url, params={
            'access_token': access_token,
            'uid': uid
        }).text
        info_message_loads = json.loads(info_message)
        userinfo = info_message_loads['name']
        return userinfo

    def all_weibo(self, client_id, client_secret, url, code):
        """
        微博登录
        :param client_id: appID
        :param client_secret:  appSecret
        :param url:  your weibo redirect_url
        :param code: 从微博服务器得到code
        :return: 返回所有信息 可以自定制
        """
        get_access_token_url = "https://api.weibo.com/oauth2/access_token"

        get_message_url = "https://api.weibo.com/2/users/show.json"

        response = requests.post(url=get_access_token_url, params={
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": url,
            "code": code
        }).text
        response_loads = json.loads(response)
        access_token = response_loads['access_token']
        uid = response_loads['uid']
        # 请求得到用户信息

        info_message = requests.get(url=get_message_url, params={
            'access_token': access_token,
            'uid': uid
        }).text
        info_message_loads = json.loads(info_message)
        all_info = info_message_loads
        return all_info

    def qq(self, client_id, client_secret, url, code):
        """
        qq登录
        :param client_id: appID
        :param client_secret: appSecret
        :param url:  your qq redirect_url
        :param code: 从QQ服务器得到code
        :return: 用户名
        """
        get_access_token_url = "https://graph.qq.com/oauth2.0/token"
        get_open_id_url = "https://graph.qq.com/oauth2.0/me"
        get_user_info_url = "https://graph.qq.com/user/get_user_info"
        # 请求得到access_token
        response = requests.get(url=get_access_token_url, params={
            'grant_type': 'authorization_code',
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uri': url,
            'code': code
        }).text

        # FFFB91C30F6F87EA5BF9570AEC2E23F & expires_in = 7776000 & refresh_token = 7
        # F135B51779C7595DED58D85C87419CE
        # print(access_token)
        access_token = response.split('&')[0]
        access_token = access_token[13:]

        # 获取openid
        # get_open_id_url = "https://graph.qq.com/oauth2.0/me?access_token={}".format(access_token)
        response_open_id = requests.get(url=get_open_id_url, params={
            'access_token': access_token
        }).text
        # print(response_open_id)
        # callback({"client_id": "101576925", "openid": "B3F2C9D7A081D39936017FF97166052A"});
        response_open_id_dict = eval(response_open_id[9:-3])
        open_id = response_open_id_dict.get('openid')
        # 获取个人信息

        response_user_info = requests.get(url=get_user_info_url, params={
            'access_token': access_token,
            'oauth_consumer_key': client_id,
            'openid': open_id
        }).text
        response_user_info = json.loads(response_user_info)
        userinfo = response_user_info['nickname']

        return userinfo

    def all_qq(self, client_id, client_secret, url, code):
        """
        qq登录
        :param client_id: appID
        :param client_secret: appSecret
        :param url:  your qq redirect_url
        :param code: 从QQ服务器得到code
        :return: 返回所用信息
        """
        get_access_token_url = "https://graph.qq.com/oauth2.0/token"
        get_open_id_url = "https://graph.qq.com/oauth2.0/me"
        get_user_info_url = "https://graph.qq.com/user/get_user_info"
        # 请求得到access_token
        response = requests.get(url=get_access_token_url, params={
            'grant_type': 'authorization_code',
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uri': url,
            'code': code
        }).text

        # FFFB91C30F6F87EA5BF9570AEC2E23F & expires_in = 7776000 & refresh_token = 7
        # F135B51779C7595DED58D85C87419CE
        # print(access_token)
        access_token = response.split('&')[0]
        access_token = access_token[13:]

        # 获取openid
        # get_open_id_url = "https://graph.qq.com/oauth2.0/me?access_token={}".format(access_token)
        response_open_id = requests.get(url=get_open_id_url, params={
            'access_token': access_token
        }).text
        # print(response_open_id)
        # callback({"client_id": "101576925", "openid": "B3F2C9D7A081D39936017FF97166052A"});
        response_open_id_dict = eval(response_open_id[9:-3])
        open_id = response_open_id_dict.get('openid')
        # 获取个人信息

        response_user_info = requests.get(url=get_user_info_url, params={
            'access_token': access_token,
            'oauth_consumer_key': client_id,
            'openid': open_id
        }).text
        response_user_info = json.loads(response_user_info)
        all_info = response_user_info

        return all_info

    def weixin(self, client_id, client_secret, code):
        """
        weixin登录
        :param client_id: appID
        :param client_secret: appSecret
        :param code: 从WEIXIN服务器得到code
        :return: 返回所用信息
        """
        get_access_token_url = "https://api.weixin.qq.com/sns/oauth2/access_token"
        # 请求得到access_token

        response = requests.get(url=get_access_token_url, params={
            'appid': client_id,
            'secret': client_secret,
            'code': code
        }).text
        # 获取openid
        response_open_id = json.loads(response)
        open_id = response_open_id['openid']
        return open_id
