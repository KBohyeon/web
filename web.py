from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template('start.html')

@app.route('/start', methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        app.start = True
        return render_template('main.html')
    return redirect(url_for('main_page'))

@app.route('/test1', methods=['GET', 'POST'])
def test1():
    if request.method == 'POST':
        app.test2 = 1  
    pass
    
@app.route('/test2', methods=['GET', 'POST'])
def test2():
    if request.method == 'POST':
        app.test2 = 2
    pass

if __name__ == '__main__':
    app.run(host="192.168.0.82", port=80, debug=True)
