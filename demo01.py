import tools


passwd = tools.gen_secret('root', 'utf-8')
print(passwd)