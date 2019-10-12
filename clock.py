from apscheduler.schedulers.blocking import BlockingScheduler
import requests
from time import strftime
from pushbullet import Pushbullet

sched = BlockingScheduler()


@sched.scheduled_job('interval', hours=8)
def checkWebPage():

    headers = {
        'headers': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
    url = "https://www.ufmg.br/copeve/Arquivos/2018/trob_edital_ufmg2019.pdf"
    pb = Pushbullet("pushbullet-key")
    r = requests.get(url, headers=headers, timeout=5)

    time = strftime('%X')
    print(time, r.status_code)
    if r.status_code == 200:
        print("Saiu o edital!")
        # os.system('ntfy -t "SITE UP!!" send "%s"' % url)
        pb.push_note("UFMG", "Saiu EDITAL")


sched.start()
