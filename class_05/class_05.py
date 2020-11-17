##1. list,列表, 两边是方括号[], 可以通过下标和遍历取值

# a = [1,3,0, 6, 4,5]   #
# print(a)
# print(type(a))

# 下标获取
# print(a[0])

# 遍历
# for i in a:
#     # print(i)
#     if i % 2 == 0:
#         print(i)

# 排序
# a = sorted(a, reverse=True)
# a = sorted(a)
# print(a)

# 增
# a.append(10)
# print(a)
# a.insert(0, 100)
# print(a)

# 删除

# a = [1,3,3,5, 6]
# a.remove(3)  # 删除某个具体的数, 要求先判断在不在，然后再移除
# print(a)
# a.remove(100)
# print(a)

# value = 100  # 为了防止报错，需要对删除的元素进行检验
# if value in a:
#     a.remove(value)
# print(a)

# try:
#     a.remove(100)
#
# except Exception as error:
#     print(error)
# finally:
#     print(a)

# del a[0]
# print(a)

# a.pop(1)  # 通过下标
# print(a)

# 改

# a[0] = 100
# print(a)

# 查, 通过下标访问
# print(a[0])
# 遍历


# dict 字典, 两边是花括号{}, 他们成对出现,通过key获取值
# d = {'a': 10, 'b': 10}  # 钥匙和锁
# print(d)
# print(type(d))

# 字典和字符串的区别
# d1 = '{"a": "1"}'
# print(type(d1))
# import json
# d2 = json.loads(d1)
# print(d2, type(d2))


# print(d.get('a'))
# print(d.get('c'))
# print(d['c'])

# 增
# d['c'] = 100
# print(d)

# 删
# del d['a']
# print(d)

# del d['c']

# if 'c' in d:
#     del d['c']

# 改
# d['a'] = 1000
# print(d)

# 查

# data = {'a': '1', 'b': 2}
# for key, value in data.items():
#     print(key, value)


# for key in data.keys():
#     print(key)
#
# for value in data.values():
#     print(value)

# for key in data.keys():
#     print(data.get(key))


## 元祖, 两边是小括号(), 不可变, 通过下标获取值

# b = 1
# t = 1,
#
# t0 = (1,)
# print(type(b))
# print(type(t))
# print(type(t0))

# 主要用在函数返回值，可以返回多个值
def func(a, b, c):
    return a + b, a + c, b + c


# a,b,c = func(1,2,3)
# print(a,b,c)

# 查询操作
# t1 = (1,3,4)
# print(t1[0], t1[1])
# print(len(t1))

# t1 = (1,3,4)
# for i in t1:
#     print(i)

#
# ## 不定参数
# def hello(a, *args, **kwargs):
#     print(a,type(a))  # 10 <class 'int'>
#     print(args, type(args))  # (11,) <class 'tuple'>
#     print(kwargs, type(kwargs))  # {'name': 'helloworld'} <class 'dict'>
#
# hello(10,11, 12, name='helloworld', age=10)


## 组合用法

# a1 = [
#   {
#     "counterParty":"master",
#     "email":"master@test.com",
#     "type":1,
#     "asset":"BTC",
#     "qty":"1",
#     "status":"SUCCESS",
#     "tranId":11798835829,
#     "time":1544433325000
#   },
#   {
#     "counterParty": "subAccount",
#     "email": "sub2@test.com",
#     "type":  2,
#     "asset":"ETH",
#     "qty":"2",
#     "status":"SUCCESS",
#     "tranId":11798829519,
#     "time":1544433326000
#   }
# ]

# print(a1)

# print(a1[0])
# print(a1[0]['asset'])
# print(a1[0].get('asset'))


# a2 = {
#     "timezone": "UTC",
#     "serverTime": 1565246363776,
#     "rateLimits": [
#         {
#
#         }
#     ],
#     "exchangeFilters": [
#
#     ],
#     "symbols": [
#         {
#             "symbol": "ETHBTC",
#             "status": "TRADING",
#             "baseAsset": "ETH",
#             "baseAssetPrecision": 8,
#             "quoteAsset": "BTC",
#             "quotePrecision": 8,
#             "quoteAssetPrecision": 8,
#             "orderTypes": [
#                 "LIMIT",
#                 "LIMIT_MAKER",
#                 "MARKET",
#                 "STOP_LOSS",
#                 "STOP_LOSS_LIMIT",
#                 "TAKE_PROFIT",
#                 "TAKE_PROFIT_LIMIT"
#             ],
#             "icebergAllowed": True,
#             "ocoAllowed": True,
#             "isSpotTradingAllowed": True,
#             "isMarginTradingAllowed": True,
#             "filters": [
#             ],
#             "permissions": [
#               "SPOT",
#               "MARGIN"
#             ]
#         }
#     ]
# }


# print(a2)
# print(a2.get('symbols'))
# print(a2.get('symbols')[0])
# print(a2.get('symbols')[0]["orderTypes"])
# a21 = a2.get('symbols')[0]["orderTypes"]
# print(a21[1])


# a3 = {
#     "lastUpdateId": 1027024,
#     "bids": [
#         [
#             "4.00000000",
#             "431.00000000"
#
#         ],
#         [
#             "4.10000000",
#             "432.00000000"
#
#         ],
#
#     ],
#     "asks": [
#         [
#             "2.00000200",
#             "12.50000000"
#         ],
#         [
#             "4.50000200",
#             "13.00000000"
#         ]
#     ]
# }
#
# print(a3['bids'])
# print(a3['bids'][1])
# print(a3['bids'][1][0])
