# -*- coding: utf-8 -*-
import sys
import uuid
import requests
import base64
import hashlib
import time
import importlib
import json
importlib.reload(sys)
YOUDAO_URL_IMAGE = 'https://openapi.youdao.com/correct_writing_image'
YOUDAO_URL_TEXT = 'https://openapi.youdao.com/correct_writing_text'

APP_KEY = 'xxx'                                              # app  key
APP_SECRET = 'xxx'                                           # secret


def truncate(q):
    if q is None:
        return None
    size = len(q)
    if size<=20:
        return q
    else:
        return  q[0:10].decode() + str(size) + q[size - 10:size].decode()


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def do_request(data,url):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(url, data=data, headers=headers)


def connect_pic(pic_path,grade):
    f = open(pic_path, 'rb')  # 二进制方式打开图文件
    q = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
    f.close()
    data = {}

    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    #print(q)
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['salt'] = salt
    data['q'] = q
    data['sign'] = sign
    data['grade'] = grade
    data['signType'] = 'v3'

    response = do_request(data,YOUDAO_URL_IMAGE)
    result=json.loads(str(response.content,'utf-8'))['Result']
    return result


def connect_context(file_path,grade):
    f=open(file_path,'rb')
    q=f.read()
    f.close()
    data = {}
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign
    data['signType'] = "v3"
    data['grade'] = grade
    response = do_request(data,YOUDAO_URL_TEXT)
    print(response.content)
    result = json.loads(str(response.content, 'utf-8'))['Result']
    print(result)
    return result

