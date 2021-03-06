# coding=utf-8
import sys
import flask_restful
import  base64
import  re
import  requests
import urllib3
import urllib
import urllib.parse
import json
import time
import codecs
import api.subconverter
import api.aff

from flask import Flask,render_template,request
urllib3.disable_warnings()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        sub = request.form['left']
        sub = sub.replace('\n','|').replace('\r','')
        if sub.split('|')[-1]== '':
            sub = sub[:-1]

        if '://' in sub:
            n=request.form['name']           
            c=request.form['custom']
            method = request.form['custommethod']
            name = urllib.parse.quote(n)
            custom = urllib.parse.quote(c)
            custommethod = urllib.parse.quote(method) 

            len1 = len(str(n).split('@'))
            len2 = len(str(c).split('@'))
            len3 = len(str(method).split('@'))

            if len1 != len2 or len1 != len3:
                return('检查分组是否一一对应')

            try:
                tool=str(request.values.get('tool'))
            except :
                pass

            if tool == 'clash':
                    CustomGroupvmess = 'http://{ip}/api/clash?sublink={sub}&name={name}&gp={custom}&gpm={custommethod}'.format(ip=api.aff.apiip,sub=str(sub),name=str(name),custom=str(custom),custommethod=str(custommethod))
                    return render_template('clash.html',sub = sub,custom=n+c+method,api=CustomGroupvmess)

            if tool == 'clashr':
                    CustomGroupvmess = 'http://{ip}/api/clashr?sublink={sub}&name={name}&gp={custom}&gpm={custommethod}'.format(ip=api.aff.apiip,sub=str(sub),name=str(name),custom=str(custom),custommethod=str(custommethod))
                    return render_template('clashr.html',sub = sub,custom=n+c+method,api=CustomGroupvmess)
            if tool == 'surge':
                    CustomGroupvmess = 'http://{ip}/api/surge?sublink={sub}&name={name}&gp={custom}&gpm={custommethod}'.format(ip=api.aff.apiip,sub=str(sub),name=str(name),custom=str(custom),custommethod=str(custommethod))
                    return render_template('surge.html',sub = sub,custom=n+c+method,api=CustomGroupvmess)


            else:
                return render_template('indexnew.html')    
        else:
            return '订阅不规范'
    return render_template('indexnew.html')

@app.route('/api/clash', methods=['GET', 'POST'])
def clashapigroup():
    try:
        sub = request.args.get('sublink')
        try:
            name = request.args.get('name')
        except Exception as e:
            name = ''

        try:
            custom = request.args.get('gp')
        except Exception as e:
            custom = ''

        try:
            custommethod = request.args.get('gpm')
        except Exception as e:
            custommethod = ''
        api.subconverter.writeini(name,custom,custommethod)
        return api.subconverter.Retry_request('http://127.0.0.1:10010/clash?url='+sub)        
    except Exception as e:
        return '检测调用格式是否正确'+ api.aff.aff

@app.route('/api/clashr', methods=['GET', 'POST'])
def clashr():
    try:
        sub = request.args.get('sublink')
        try:
            name = request.args.get('name')
        except Exception as e:
            name = ''

        try:
            custom = request.args.get('gp')
        except Exception as e:
            custom = ''

        try:
            custommethod = request.args.get('gpm')
        except Exception as e:
            custommethod = ''
        api.subconverter.writeini(name,custom,custommethod)
        return api.subconverter.Retry_request('http://127.0.0.1:10010/clashr?url='+sub)        
    except Exception as e:
        return '检测调用格式是否正确'+ api.aff.aff

@app.route('/api/surge', methods=['GET', 'POST'])
def surge():
    try:
        sub = request.args.get('sublink')
        try:
            name = request.args.get('name')
        except Exception as e:
            name = ''

        try:
            custom = request.args.get('gp')
        except Exception as e:
            custom = ''

        try:
            custommethod = request.args.get('gpm')
        except Exception as e:
            custommethod = ''
        api.subconverter.writeini(name,custom,custommethod)
        return api.subconverter.Retry_request('http://127.0.0.1:10010/surge?url='+sub)        
    except Exception as e:
        return '检测调用格式是否正确'+ api.aff.aff

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False,port=10086)            #自定义端口