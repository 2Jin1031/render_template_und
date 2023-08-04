from flask import Flask, render_template

app = Flask(__name__)

@app.route('/goto_a_page')
def goto_a_page():
    return render_template('a_page.html')

@app.route('/b_page')
def goto_b_page():
    return render_template('b_page.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="9999")