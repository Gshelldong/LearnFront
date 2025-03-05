from flask import Flask, request

app = Flask(__name__)

@app.route('/index/',methods=['GET','POST'])
def index():
    print(request.form.to_dict())


    file_obj = request.files.get('avatar')
    if file_obj:
        file_obj.save('xxx.pdf')
    with open('01.第一个html页面.html','r',encoding='utf-8') as f:
        conent = f.read()
    return conent

app.run()