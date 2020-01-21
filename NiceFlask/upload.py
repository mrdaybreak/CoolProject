# coding:utf-8

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from flask_socketio import SocketIO, emit
print(os.system('ifconfig | grep -w inet'))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/IM', methods=['POST', 'GET'])
def IM():
    return render_template('publicIM.html')


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        print(request.files)
        f = request.files['file']
        print(f)
        # 获取当前py文件目录
        basepath = os.path.dirname(__file__)
        uploadpath = os.path.join(basepath, 'static/uploadfile', secure_filename(f.filename))
        f.save(uploadpath)
    return render_template('upload.html')


@socketio.on('imessage', namespace='/test_conn')
def message_info(message):
    print(message)
    emit('message', {'data': message['data']}, broadcast=True)


@app.route('/')
def index():
    return redirect(url_for('IM'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    socketio.run(app=app, host="0.0.0.0", port=5000, debug=True)