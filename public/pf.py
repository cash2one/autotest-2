# -*- coding:utf-8 -*-
import urllib
import http.cookiejar
import time
import pymysql


class configs():
    # 网站url
    url = 'http://qf.huomaotv.com.cn'
    # 万能验证码
    yzm = 'lxy1'
    # 通用密码
    pwd = 'test123456'
    # 用例路径
    filepath = 'E:\selenium\\autotest\\testcase\data\case_data.xlsx'
    # 浏览器Chrome/Firefox/Ie
    llq = 'Chrome'

# 全局数据库参数设置
host = '180.150.179.136',
user = 'qa',
passwd = 'fgd@gG513$FD1',
db = 'marstv_www',
port = 4040,
charset = 'utf8'


def dyfj(uid, roomid):
        # 订阅房间
    conn = pymysql.connect(
        host=host,
        user=user,
        passwd=passwd,
        db=db,
        port=port,
        charset=charset)
    cur = conn.cursor()  # 获取一个游标
    time1 = int(time.time())
    data = [uid, roomid]
    cur.execute(
        "SELECT count(1) FROM mtv_subscribe WHERE user_id = %s and channel_id = %s", data)
    data1 = cur.fetchall()
    if data1[0][0] == 0:
        data = [uid, roomid, time1]
        cur.execute(
            "INSERT INTO mtv_subscribe(user_id,channel_id,time) VALUES(%s, %s, %s)", data)
    conn.commit()  # 提交
    cur.close()  # 关闭游标
    conn.close()  # 释放数 据库资源


def zbzt(status, roomid):
    # 直播间状态
    conn = pymysql.connect(
        host=host,
        user=user,
        passwd=passwd,
        db=db,
        port=port,
        charset=charset)
    data = [status, roomid]
    cur = conn.cursor()  # 获取一个游标
    cur.execute("UPDATE mtv_channel SET is_live= %s WHERE id = %s", data)
    conn.commit()  # 提交
    cur.close()  # 关闭游标
    conn.close()  # 释放数 据库资源


def cleardy(uid):
    # 清除用户订阅信息
    conn = pymysql.connect(
        host=host,
        user=user,
        passwd=passwd,
        db=db,
        port=port,
        charset=charset)
    cur = conn.cursor()  # 获取一个游标
    cur.execute(
        "SELECT count(1) FROM mtv_subscribe WHERE user_id = %s", (uid))
    data = cur.fetchall()
    if data[0][0] != 0:
        cur.execute(
            "DELETE FROM mtv_subscribe WHERE user_id = %s", (uid))
    conn.commit()  # 提交
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源


def yzyx(testemail):
    # 验证邮箱
    conn = pymysql.connect(
        host=host,
        user=user,
        passwd=passwd,
        db=db,
        port=port,
        charset=charset)
    cur = conn.cursor()  # 获取一个游标
    cur.execute(
        "SELECT uid FROM ms_ucenter_members WHERE email = %s", (testemail))
    data = cur.fetchone()
    uid = data[0]
    cur.execute(
        "UPDATE mtv_user SET email_is_check = 1 WHERE uid LIKE %s", uid)
    conn.commit()  # 提交
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源


# 插入cookie登录
def cookieLogin(uid, token, ts, self):
    self.add_cookie({'name': 'huomaotvhjhdwq_u_ID', 'value': uid})
    self.add_cookie({'name': 'huomaotvhjhdwq_u_token', 'value': token})
    self.add_cookie({'name': 'huomaotvhjhdwq_u_ts', 'value': ts})
    self.refresh()


# 封装find_elemet_by_?
def findE(self, how, value):
    if how == 'id':
        self.find_element_by_id(value)
    elif how == 'name':
        self.find_element_by_name(value)
    elif how == 'class_name':
        self.find_element_by_class_name(value)
    elif how == 'tag_name':
        self.find_element_by_tag_name(value)
    elif how == 'link_text':
        self.find_element_by_link_text(value)
    elif how == 'prtial_link_text':
        self.find_element_by_prtial_link_text(value)
    elif how == 'xpath':
        self.find_element_by_xpath(value)
    elif how == 'css_selector':
        self.find_element_by_css_selector(value)
    else:
        return False


# 判断元素是否存在,存在返回true
def existE(self, how, value):
    try:
        findE(self, how, value)
    except:
        return False
    return True


# div弹层判断
def divtc(self):
    a = ''
    allelements = self.find_elements_by_xpath("//div[@class='l-text']")
    for allelement in allelements:
        a = a + allelement.text
    return a


# 注册
def reglogin(self, type, a, b, c, d):
    # type:user/mail/phone
    time.sleep(1)
    self.find_element_by_link_text('注册').click()
    time.sleep(1)
    self.find_element_by_class_name(type).click()
    time.sleep(1)
    self.find_element_by_id('email_login').send_keys(a)
    time.sleep(1)
    self.find_element_by_id('pwd_login').send_keys(b)
    time.sleep(1)
    self.find_element_by_id('pwd_login2').send_keys(c)
    time.sleep(1)
    self.find_element_by_id('vcode_login').send_keys(d)
    time.sleep(1)
    self.find_element_by_id('reg_login').click()
    time.sleep(1)


# 注册手机输入函数
def regphone(self, a, b, c, d, e):
    self.find_element_by_id('email_login').send_keys(a)
    time.sleep(1)
    self.find_element_by_id('pwd_login').send_keys(b)
    time.sleep(1)
    self.find_element_by_id('pwd_login2').send_keys(c)
    time.sleep(1)
    self.find_element_by_id('vcode_login').send_keys(d)
    time.sleep(1)
    self.find_element_by_id('mobile_login').send_keys(e)


# 正常登录
def login(self, a, b, c, type=0):
    if type == 0:
        time.sleep(1)
        self.find_element_by_link_text('登录').click()
        time.sleep(1)
        self.find_element_by_id('email_login').send_keys(a)
        time.sleep(1)
        self.find_element_by_id('pwd_login').send_keys(b)
        time.sleep(1)
        self.find_element_by_id('vcode_login').send_keys(c)
        time.sleep(1)
        self.find_element_by_id('new_login').click()
        time.sleep(1)
    else:
        self.find_element_by_id('email_login').send_keys(a)
        time.sleep(1)
        self.find_element_by_id('pwd_login').send_keys(b)
        time.sleep(1)
        self.find_element_by_id('vcode_login').send_keys(c)


# 模拟用户房间发言
def talk(uid, token, ts, room, data):
    def make_cookie(name, value):
        return http.cookiejar.Cookie(
            version=0,
            name=name,
            value=value,
            port=None,
            port_specified=False,
            domain="qf.huomaotv.com.cn",
            domain_specified=True,
            domain_initial_dot=False,
            path="/",
            path_specified=True,
            secure=False,
            expires=None,
            discard=False,
            comment=None,
            comment_url=None,
            rest=None
        )
    # 声明一个CookieJar对象实例来保存cookie
    cookie = http.cookiejar.CookieJar()
    cookie.set_cookie(make_cookie("huomaotvhjhdwq_u_ID", uid))
    cookie.set_cookie(
        make_cookie("huomaotvhjhdwq_u_token", token))
    cookie.set_cookie(make_cookie("huomaotvhjhdwq_u_ts", ts))
    cjhdr = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(cjhdr)
    urllib.request.install_opener(opener)
    url = "http://www.huomaotv.com/index.php?c=live&a=send_msg"
    postdata = urllib.parse.urlencode(
        {'data': data, 'cid': room, 'phone': '1'})
    postdata = postdata.encode('utf-8')

    res = urllib.request.urlopen(url, postdata)
    dict1 = eval(bytes.decode(res.read()))
    if dict1['error'] == 0:
        return True
    else:
        return False


# 用户名快速注册
def regnamef(tv_email):
    url = "http://qf.huomaotv.com.cn/index.php?c=ajax&a=new_user_do"
    postdata = urllib.parse.urlencode(
        {'tv_email': tv_email, 'tv_pwd': 'test1234',
         'tv_name': '', 'tv_vcode': 'lxy1',
         'tv_agr': 1, 'state': 'vcode', 'ac': 'username'})
    postdata = postdata.encode('utf-8')
    res = urllib.request.urlopen(url, postdata)
    dict1 = eval(bytes.decode(res.read()))
    if dict1['msg'] == '1':
        return True
    else:
        return False
