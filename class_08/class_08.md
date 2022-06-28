# 第八课: VNPY数据库配置和数据爬取


## 币安邀请码
没有开通币安或者交易所的可以通过下面链接去开通，有手续费减免:
**https://www.binancezh.pro/cn/futures/ref/51bitquant**
合约邀请码：**51bitquant**


## 答疑: 安装vnpy的错误
1. MacOS系统，要记得安装Xcode开发工具，主要是Xcode会帮你把一些构建工具和库安装好,
   window系统不需要安装Xcode开发工具，因为没有这个软件。
2. 安装通过pip install git+https://github.com/51bitquant/howtrader.git
3. 如果没有安装git工具的，记得去安装，具体百度下。

## 支持的数据库类型
1. 支持sqlite3数据库(默认使用)
2. mongodb数据库
3. mysql

## 配置文件

1. mongodb 需要安装 先启动数据库
> mongod --dbpath /Users/wanglin/mongodb/data/db(替换成你的路径, replace
> with your own database path)


配置文件的详细信息请参考: howtrader/trader/setting.py文件
```python

SETTINGS: Dict[str, Any] = {
    "font.family": "Arial",
    "font.size": 12,

    "log.active": True,
    "log.level": CRITICAL,
    "log.console": True,
    "log.file": True,

    "email.server": "smtp.qq.com",
    "email.port": 465,
    "email.username": "",
    "email.password": "",
    "email.sender": "",
    "email.receiver": "",

    "database.timezone": get_localzone().zone,
    "database.driver": "sqlite",                # see database.Driver
    "database.database": "database.db",         # for sqlite, use this as filepath
    "database.host": "localhost",
    "database.port": 3306,
    "database.user": "root",
    "database.password": "",
    "database.authentication_source": "admin",  # for mongodb
}

```

``` json
{
    "font.family": "Arial",
    "font.size": 12,

    "log.active": true,
    "log.level": "CRITICAL",
    "log.console": true,
    "log.file": true,

    "email.server": "smtp.qq.com",
    "email.port": 465,
    "email.username": "",
    "email.password": "",
    "email.sender": "",
    "email.receiver": "",

    "database.driver": "mongodb",               
    "database.database": "howtrader",
    "database.host": "localhost",
    "database.port": 3306,
    "database.user": "root",
    "database.password": "",
    "database.authentication_source": "admin"
}


```
1. database.driver : 填写的值有: sqlite, mysql, mongodb 
2. database.database: 数据库名称,
   howtrader,随便填写，如果默认用sqlite.db就不用修改。
3. host 主机, user用户， passwordm密码 

默认的sqlite的配置
```json

{
     "database.driver": "sqlite",               
    "database.database": "database.db"
}


```
使用mongodb的配置
``` json
{
    "database.driver": "mongodb",               
    "database.database": "howtrader",
    "database.host": "localhost",
    "database.port": 27017,
    "database.authentication_source": "admin"
}

```




可能的报错： 
``` 
pymongo.errors.ServerSelectionTimeoutError: Got response
id 3158574 but expected 996497972, Timeout: 30s, Topology Description:
<TopologyDescription id: 5fb9f86c773b82991c1df7fb, topology_type:
Single, servers:
[<ServerDescription ('localhost', 3306) server_type: Unknown, rtt: None, error=ProtocolError('Got response id 3158574 but expected 996497972')>]>

```


## 关于连接交易所的配置

1. 现货

```json
{
    "key": "xxxxxx",
    "secret": "xxx",
    "session_number": 3,
    "proxy_host": "127.0.0.1",
    "proxy_port": 1087
}

```

2. 合约

```json
{
    "key": "xxxx",
    "secret": "xxxx",
    "会话数": 3,
    "服务器": "REAL",
    "合约模式": "正向",
    "代理地址": "127.0.0.1",
    "代理端口": 1087
}

```

记得合约代理的proxy_host或者代理地址:
只能写ip地址，不能写http://xxx.xxx.xxx.xxx, 不包含http或者https协议头


## 数据批量爬取数据
具体参考crawl_data.py脚本,修改成自己需要的交易对，填写具体的交易对就可以了。记得修改对应的爬取时间
1. download_spot(), 这个方法是爬取现货的数据.

2. download_future(), 这是合约的数据

记得下载好BTCUSDT和ETHUSDT的数据，后面的课程会用到。
