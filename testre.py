import re

stringtest = '{"result":"2","prompWord":"\u003cfont style=\u0027font-weight:bold;\u0027\u003e您申请的\u003cfont style=\u0027color:red\u0027\u003e【菁英公寓】【单身合租型卧室】\u003c/font\u003e房源目前暂无，公租房管理有限公司暂无法受理您的租房申请。\u003cbr\u003e您现被列入候租名单，您在\u003cfont style=\u0027color:red\u0027\u003e【本科及以上】【男】\u003c/font\u003e申请人中的排序号为：第\u003cfont style=\u0027color:red\u0027\u003e【3】\u003c/font\u003e位，\u003cbr\u003e\u003cfont style=\u0027color:#f16a07\u0027\u003e重要提醒：查询结果如出现与单位查询结果不一致的，以单位查询结果为准。\u003c/font\u003e\u003c/font\u003e"}'
status = stringtest[11]

location = stringtest[87:93]
category = stringtest[93:102]
education = stringtest[177:184]
sex = stringtest[184:187]
order = stringtest[229:232]

#print(stringtest[11])
#print(stringtest[87:93])
#print(stringtest[93:102])
#print(stringtest[177:184])
#print(stringtest[184:187])
#print(stringtest[229:232])

#print(status)
#print(location)
#print(category)
#print(education)
#print(sex)
#print(order)

#todo:string-dict???

#todo:status

if status == '2':
    dict = {'status':'2','location':location,'category':category,'education':education,'sed':sex,'order':order}
    print("dict['location']:",dict['location'])
    print("dict['category']",dict['category'])
elif status == '2':
    print("您已经通过申请")
else:
    print("这是一个测试")
#todi:dict-json
