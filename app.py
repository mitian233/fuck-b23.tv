from flask import Flask, redirect, url_for, render_template, request, session
from urllib.parse import urlparse
import requests

app = Flask(__name__)

def getB23Url(url):
    r = requests.get(url, allow_redirects=False)
    url_result = urlparse(r.headers['Location'])
    genUrl = 'https://' + url_result.hostname + url_result.path
    return genUrl

@app.route('/')
def homePage():  # put application's code here
    return render_template('index.html')

@app.route('/<string:b23Id>')
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
        return genUrl
    else:
        print(2)
        url = request.args.get('url')
        if not url.startswith('http'):
           url = "https://" + url
        genUrl = getB23Url(url)
        return genUrl

if __name__ == '__main__':
    app.run()
