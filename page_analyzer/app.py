from flask import Flask, request, render_template, redirect, url_for, flash
import psycopg2
import os
import validators
from dotenv import load_dotenv
from .formatting import parsed_url, format_date
from .db import open_db_connection, close_db_connection, check_if_url_exists, insert_url


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def home():
    return render_template('index.html')
