import hashlib

def gen_secret(passwd, flag):
    md5 = hashlib.md5()
    md5.update(passwd.encode(flag))
    ret = md5.hexdigest()
    return ret, passwd
