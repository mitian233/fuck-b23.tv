from flask import Flask,redirect,url_for,render_template
from urllib.parse import urlparse
import requests

app = Flask(__name__)

@app.route('/')
def checkWorking():  # put application's code here
    return 'Working'

@app.route('/<string:b23Id>')
def dispBVNum(b23Id):
    url = 'https://b23.tv/'+b23Id
    r = requests.get(url, allow_redirects=False)
    url_result = urlparse(r.headers['Location'])
    genUrl = 'https://www.bilibili.com' + url_result.path
    return redirect(genUrl)

if __name__ == '__main__':
    app.run()
