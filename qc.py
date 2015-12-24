# -*- coding: utf-8 -*-
import easygui as g
import qrcode


# MRNAA0039940-A00399-1540-151030-0001-000:00007200
msg = "请认真按格式要求填写二维码相关数据"
title = "大连崇达电子有限公司二维码专用程序"
fieldNames = ["产品型号", "供应商代码", "生产周期", "发货日期", "总共箱数", "每箱PCS数"]
fieldValues = []
fieldValues = g.multenterbox(msg, title, fieldNames)

while 1:
    if fieldValues is None:
        break
    errmsg = ""

    sst = ''
    for i in range(len(fieldNames))[::-1]:
        if i == 4:
            ss2 = int(fieldValues[i])
            ss1 = 'xxxx'
        else:
            ss1 = fieldValues[i]
        sst = ss1 + '-' + sst
    if errmsg == "":
        break
    fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)

sst = sst[:-1]
for ii in range(1, ss2 + 1):
    ss3 = str(ii).zfill(4)
    ss4 = sst.replace('xxxx', ss3)
    print("正在生成二维码：%s" % ss4)
    ewimg = qrcode.make(ss4)
    ewimg.save('d:/001/' + str(ii) + '.png')
    ii += 1
