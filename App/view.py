from flask import Blueprint, render_template, request

from App.models import Employer, User
from Tools.Tools import check_args
from ext import db

blue = Blueprint('first_blue', __name__)


@blue.route('/', methods=['POST','GET'])
def login():
    return render_template('login.html')

@blue.route('/index/', methods=['POST','GET'])
@check_args
def index():
    if request.method == 'POST':
        return render_template('index.html',user=request.form.get('user'),
                               password=request.form.get('password'))
    else:
        return render_template('index.html')

@blue.route('/add/',methods=['POST','GET'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        db.create_all()
        t = []
        for i in request.form.values():
            t.append(i)
        user,password,fullname,sex,phone,role,department,post=t
        en = Employer(fullname,sex,phone,role,department,post)
        us = User(user,password)
        db.session.add(en)
        db.session.add(us)
        db.session.commit()
        return 'ok'

