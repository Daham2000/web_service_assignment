from application import app
from flask import render_template,request
from application import db_ctrl

@app.route("/")
def index():
    return render_template("index.html", index=True)

@app.route('/', methods=['POST'])
def my_form_post():
    u_id = request.form['u_id']
    load_amount = request.form['load_amount']
    user = db_ctrl.UserLoan()
    user.u_id = u_id
    user.load_amount = load_amount
    user.getSingleUserIfValid()
    return "Your request in process..."