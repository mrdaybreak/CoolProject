from flask import Flask, render_template, url_for

# 生成Flask实例
app = Flask(__name__)


@app.route('/')
def my_echart():
    # 在浏览器上渲染chart.html模板
    memory_x = [i for i in range(100)]
    memory = [i for i in range(100, 200)]
    return render_template('singleIM.html', memory=memory, memory_xa=memory_x)


if __name__ == "__main__":
    # 运行项目
    app.run(debug=True)
