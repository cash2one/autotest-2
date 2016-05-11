import pymysql
import time
# 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
conn = pymysql.connect(host='180.150.179.136', user='qa',
                       passwd='fgd@gG513$FD1',
                       db='marstv_www', port=4040, charset='utf8')
cur = conn.cursor()  # 获取一个游标
cur.execute("SELECT uid FROM ms_ucenter_members WHERE username LIKE 'dhswg555'")
data = cur.fetchall()
print(data)
print(data[0][0])
cur.close()  # 关闭游标
conn.close()  # 释放数据库资源
print('test'+str(int(time.time())))