# -- coding: utf-8 --
# @Time : 2021/1/26 14:43

import execjs


with open('password.js', 'r') as f:
    js = f.read()
    f.close()

comp = execjs.compile(js)
password = '77777777'
en_password = comp.call('pwd_encryptedString', password)

print('len(en_password):', len(str(en_password)))
print('en_password:', en_password)