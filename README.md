A project for Third party login

目前只支持 腾讯QQ,微信,微博 第三方登录

如有疑问不会使用 请联系作者:1483906080@qq.com

"""
code: 用户授权登录回调参数code
client_id:腾讯开放平台上app的APPID名
client_secret: 腾讯开放平台上app的secret名
redirect_uri: 腾讯开放平台上app的回调url
"""

from AgentLogin import AgentLogin

@redirect_url.route("/login/qq")
def redirect_qq():
    code = request.args.get('code')
    user = AgentLogin.qq(client_id, client_secret, redirect_uri, code)
    is_user = fetch_one("select * from user where username=%s", user)
    if is_user:
        token = str(uuid.uuid4())
        update_one("update user set password=%s where username=%s", (token, user))
    else:
        token = str(uuid.uuid4())
        insert_one("insert into user (username, password) values(%s, %s)", (user, token))
    redirect_url = redirect("/home")
    redirect_url.set_cookie("name", user)
    redirect_url.set_cookie("token", token)
    return redirect_url
