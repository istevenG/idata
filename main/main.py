# -*-coding:utf-8-*-
from flask import Blueprint, render_template, redirect, url_for, jsonify, request

bp_main = Blueprint('main', __name__, static_folder='../static')


@bp_main.route('/')
@bp_main.route('/index')
def index():
    return render_template('index.html')
