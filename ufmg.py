import requests
from time import sleep, strftime
from pushbullet import Pushbullet
import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def ufmg():
    return 'Working!!'

headers = {
    'headers': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
url = "https://www.ufmg.br/copeve/Arquivos/2018/trob_edital_ufmg2019.pdf"
pb = Pushbullet("o.XlhLt0s4KzfMsQg0oDwFF98IkAAzD3tG")

r = requests.get(url, headers=headers, timeout=5)

while r.status_code != 200:
    time = strftime('%X')
    print(time, r.status_code)
    sleep(28800)

print("Saiu o edital!")
os.system('ntfy -t "SITE UP!!" send "%s"' % url)
pb.push_note("UFMG", "Saiu EDITAL")
