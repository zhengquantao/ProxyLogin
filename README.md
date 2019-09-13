# ProxyLogin    [![PyPI version](https://badge.fury.io/py/ProxyLogin.svg)](https://badge.fury.io/py/ProxyLogin)
A project for Third party login

目前只支持 腾讯QQ,微信,微博 第三方登录

安装 pip install AgentLogin


from AgentLogin import AgentLogin

qq_url = AgentLogin.qq_url(client_id, redirect_uri)

把这个qq_url链接放到你的<a href="{{ qq_url }}">QQ登录<a>

(user, user_id) = AgentLogin.qq(client_id, client_secret, redirect_uri, code)

code: 用户授权登录回调参数code
client_id:腾讯开放平台上app的APPID名
client_secret: 腾讯开放平台上app的secret名
redirect_uri: 腾讯开放平台上app的回调url
user: 返回qq的用户名


有使用AgentLogin的项目：http://120.78.176.77, http://101.132.132.181:8080


如有疑问不会使用 请联系作者:1483906080@qq.com
