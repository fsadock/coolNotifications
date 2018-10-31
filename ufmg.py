import requests
from time import sleep, strftime
from pushbullet import Pushbullet
import os
from flask import Flask
app = Flask(__name__)


@app.route('/')
def homepage():

    the_time = strftime("%A, %d %b %Y %H:%M")

    return """
    <h1>Oi, aqui é o sadogo</h1>
    <p>Hoje é: {time}.</p>
    <style>
        body{{
            background-color: pink;
    }}</style>
    <img src="http://loremflickr.com/600/400/dog" />
    """.format(time=the_time)

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


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
