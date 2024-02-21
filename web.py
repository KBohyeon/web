from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template('main.html')

@app.route('/test1', methods=['GET', 'POST'])
def test1():
    if request.method == 'POST':
        return "test page 1"
    else:
        return redirect(url_for('main'))

@app.route('/test2', methods=['GET', 'POST'])
def test2():
    if request.method == 'POST':
        return "test page 2"
    else:
        return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(host="192.168.0.82", port=80, debug=True)
