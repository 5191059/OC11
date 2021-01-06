import json
import os

# https://qiita.com/FPC_COMMUNITY/items/c3bad2c95a577fcc9c9d
# Third-party libraries
from flask import Flask, redirect, request, url_for, Response, abort, render_template
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
    UserMixin
)
from oauthlib.oauth2 import WebApplicationClient
from collections import defaultdict
import requests
import pymysql.cursors
from argparse import ArgumentParser
from User import User
from secret import secret
from db_con import get_info
from db_con import get_table

secret()

# Configuration
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

# Flask app setup
app = Flask(__name__)
# app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)
app.secret_key = os.urandom(24)

# User session management setup
# https://flask-login.readthedocs.io/en/latest
login_manager = LoginManager()
login_manager.init_app(app)

# Naive database setup
# try:
#     init_db_command()
# except sqlite3.OperationalError:
#     # Assume it's already been created
#     pass

# OAuth 2 client setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)

# Flask-Login helper to retrieve a user from our db



def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index', methods=['GET'])
def home2():
    return render_template('index.html')

main_html_list = [
    '01m',
    '02m',
    '03m',
    '04m',
    '05m',
    '06m',
    '07m',
    '08m',
    '09m',
    '10m'
]

sub_html_list = [
    '01s',
    '02s',
    '03s',
    '04s',
    '05s',
    '06s',
    '07s',
    '08s',
    '09s',
    '10s'
]


def ret_html(html):
    lst= {
        '01m': '01m_cpu.html',
        '02m': '02m_cooler.html',
        '03m': '03m_memory.html',
        '04m': '04m_mother.html',
        '05m': '05m_graphic.html',
        '06m': '06m_ssd.html',
        '07m': '07m_hdd.html',
        '08m': '08m_case.html',
        '09m': '09m_fan.html',
        '10m': '10m_power.html',
        '01s': '01s_cpu.html',
        '02s': '02s_cooler.html',
        '03s': '03s_memory.html',
        '04s': '04s_mother.html',
        '05s': '05s_graphic.html',
        '06s': '06s_ssd.html',
        '07s': '07s_hdd.html',
        '08s': '08s_case.html',
        '09s': '09s_fan.html',
        '10s': '10s_power.html'
    }
    return lst[html]


def ret_lst(html):
    parts_lst = get_info()
    name_lst = [
        'Cpu',
        'cpuCooler',
        'Memory',
        'Motherboard',
        'GPU',
        'SSD',
        'HDD', 
        'Cases', 
        'caseCooler', 
        'Power', 
        ]
    lst = {}
    for i in range(1, 11):
        lst['{}{}'.format(str(i).zfill(2), 'm')] = parts_lst[name_lst[i-1]]
        lst['{}{}'.format(str(i).zfill(2), 's')] = parts_lst[name_lst[i-1]]

    return lst[html]


@app.route('/<html>', methods=['GET'])
def hello_main(html):
    if html in main_html_list:
        return render_template('/main/' + ret_html(html), lst=ret_lst(html))

    return render_template('index.html')


@app.route('/sub/<html>', methods=['GET'])
def hello_sub(html):
    if html in sub_html_list:
        return render_template('/sub/' + ret_html(html), lst=ret_lst(html))

    return render_template('index.html')


@app.route('/master')
def master():
    return render_template('about/master.html')


@app.route('/user', methods=['GET'])
def user():
    return render_template('user.html')

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/account")
def index():
    if current_user.is_authenticated:
        render_template('user/account.html', user_icom=current_user.profile_pic, user_name=current_user.name)
    else:
        return render_template('user/account.html')

@app.route("/login")
def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=(request.base_url).replace('http','https') + "/callback", #redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

@app.route("/login/callback")
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

# Find out what URL to hit to get tokens that allow you to ask for
# things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

# Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=(request.url).replace('http','https'),
        redirect_url=(request.base_url).replace('http','https'),#request.base_url
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )


# Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

# Now that you have tokens (yay) let's find and hit the URL
# from Google that gives you the user's profile information,
# including their Google profile image and email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

# You want to make sure their email is verified.
# The user authenticated with Google, authorized your
# app, and now you've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

# Create a user in your db with the information provided
# by Google
# user = User(
#     id_=unique_id, name=users_name, email=users_email, profile_pic=picture
# )
    user = User(
        id_=unique_id, name=users_name, email=users_email, profile_pic=picture
    )

# Doesn't exist? Add it to the database.
    if not User.get(unique_id):
        User.create(unique_id, users_name, users_email, picture)

# Begin user session by logging the user in
    login_user(user)

# Send user back to homepage
    return redirect(url_for("index"))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

