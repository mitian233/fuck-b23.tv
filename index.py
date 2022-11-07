from flask import Flask, redirect, render_template, request
from urllib.parse import urlparse
import requests

ua = {'User-Agent': 'Mozilla/5.0'}

app = Flask(__name__)

def getB23Url(url):
    r = requests.get(url, allow_redirects=False, headers=ua)
    url_result = urlparse(r.headers['Location'])
    genUrl = 'https://' + url_result.hostname + url_result.path
    return genUrl

@app.route('/')
def homePage():  # put application's code here
    return render_template('index.html')

@app.route('/<string:b23Id>',methods=['POST','GET'])
def dispBVNum(b23Id):
    url = 'https://b23.tv/' + b23Id
    genUrl = getB23Url(url)
    return redirect(genUrl)

@app.route('/geturl',methods=['POST','GET'])
def getUrlGUI():
    if request.method == 'POST':
        print(1)
        url = request.form['url']
        if not url.startswith('http'):
           url = "https://" + url
        genUrl = getB23Url(url)
    else:
        print(2)
        url = request.args.get('url')
        if not url.startswith('http'):
           url = "https://" + url
        genUrl = getB23Url(url)
    return render_template('result.html',url=genUrl)

if __name__ == '__main__':
    app.run()
