#-*- coding:utf-8 -*-
from  PIL import Image
from io import BytesIO
def get_captcha_by_user(data):
    #人工识别验证码
    img=Image.open(BytesIO(data))
    img.show()
    capcha=input(u'输入验证码')
    img.close()
    return capcha