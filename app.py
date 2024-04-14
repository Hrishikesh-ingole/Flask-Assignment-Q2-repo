from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('index.html')

@app.route('/page_1')
def page_1():
    return render_template('page_1.html')

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
