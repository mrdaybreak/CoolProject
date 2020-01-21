from flask import Flask, render_template, request, redirect, url_for, flash
import pandas
import random
import threading
import os
from urllib.request import urlretrieve
import ssl

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asd123321'
R = threading.Lock()


@app.route('/', methods=['POST', 'GET'])
def error():
    return '你是猪么？？都不选完就点'


@app.route('/checklist', methods=['POST', 'GET'])
def get_checklist():
    total = ''
    result_list = []
    ssl._create_default_https_context = ssl._create_unverified_context
    if request.method == "POST":
        if request.form.getlist('hobbytab') == [] or request.form.getlist('hobby') == [] or request.form.getlist('hobbytoo') == []:
            return redirect(url_for("error"))
        R.acquire()
        try:
            os.remove('测试用例.xlsx')
        except FileNotFoundError:
            pass
        urlretrieve("xxx", '测试用例.xlsx')
        while True:
            if os.path.exists('测试用例.xlsx'):
                break
        pandas.set_option('display.max_rows', None)
        count_list = []
        sheet = request.form.getlist('hobbytab')
        people = request.form.getlist('hobby')
        random.shuffle(people)
        print(people)

        def count(sheetname):
            CP = request.form.getlist('hobbytoo')[0]
            df = pandas.DataFrame(pandas.read_excel('测试用例.xlsx', sheet_name=sheetname))
            if CP == 'C0':
                a = str(df[(df['checklist'] == 'C0') | (df['checklist'] == 'c0')]).split('\n')[1:-2]
            else:
                a = str(df[(df['优先级'] == 'P0') | (df['优先级'] == 'p0')]).split('\n')[1:-2]
            print(len(a))
            for number in a:
                number_count = sheetname + ' ' + str(int(number[:4].rstrip()) + 2)
                count_list.append(number_count)
            # print(count_list)

        for i in sheet:
            count(i)
        print(len(count_list))
        ave = (len(count_list) / len(people))
        print(ave)
        ave_list = [count_list[i:i + int(ave)] for i in range(0, len(count_list), int(ave))]
        print(ave_list)
        print(len(ave_list))
        for re in range(len(ave_list)):
            # global result_list
            try:
                result = str(ave_list[re][0]) + ' —— ' + str(ave_list[re][-1]) + ':  ' + people[re]
                result_list.append(result)
            except IndexError:
                result = str(ave_list[re][0]) + ' —— ' + str(ave_list[re][-1]) + ':  ' + people[re - 1]
                result_list.append(result)
        print(result_list)
        total = "用例总共 " + str(len(count_list)) + "条，每人 " + str(ave) + "条"
        R.release()
    return render_template('checklist.html', result="<br>".join(result_list), resulttotal=total)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)