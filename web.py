from flask import Flask, render_template, redirect, url_for, request
 
app = Flask(__name__)

#test 1
    
@app.route('/', methods=['GET', 'POST'])
def main():
    print("one")
    if request.method == 'POST':
        print("aa")
        return redirect(url_for('test'))
    return render_template('main.html')

@app.route('/test')
def test():
    return "test page"
 
if __name__ == '__main__':
    app.run(host="192.168.0.82", port=80, debug=True)
