import datetime
from flask import request, render_template, redirect, url_for
from flask import Flask
from api import send_request
from data.db import *


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/article/post_table/")
def table():
    return render_template('send_post.html')


@app.route("/article/post_table/", methods=['POST'])
def table_post():
    if request.method == "POST":
        page = request.form['page']
        from_date = int(datetime.strptime(request.form['from_date'], "%Y-%m-%d").timestamp())
        to_date = int(datetime.strptime(request.form['to_date'], "%Y-%m-%d").timestamp())
        tagged = request.form['tagged']
        user = send_request(page, from_date, to_date, tagged)
        post_data(user)
    return redirect(url_for('get_table'))


@app.route("/article/get_table")
def get_table():
    articles = get_data()
    return render_template('table.html', requst=articles)


@app.route("/article/delete_table")
def delete_table():
    delete_data()
    return redirect(url_for('home'), code=302)


@app.route("/modal/")
def modal():
    return render_template('modal.html')


if __name__=="__main__":
    app.run(debug=True)