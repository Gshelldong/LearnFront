from flask import Flask, request

app = Flask(__name__)

@app.route('/index/',methods=['GET','POST'])
def index():
    print(request.form)
    print(request.files)
    file_obj = request.files.get('avatar')
    file_obj.save('xxx.pdf')
    return '收到了'

app.run()