import os
import psycopg2
from psycopg2 import extras
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')


def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    conn.cursor_factory = extras.DictCursor
    return conn


def open_db_connection():
    conn = get_db_connection()
    cur = conn.cursor()
    return conn, cur


def close_db_connection(conn, cur):
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


def check_url_exists(cur, url):
    cur.execute('SELECT id FROM urls WHERE name = %s', (url,))
    return cur.fetchone()


def insert_url(cur, url):
    cur.execute(
        'INSERT INTO urls (name, created_at) VALUES (%s, %s) RETURNING id',
        (url, datetime.now())
    )
    return cur.fetchone()['id']


def get_url_by_id(conn, id):
    cur = conn.cursor()
    cur.execute('SELECT name FROM urls WHERE id = %s', (id,))
    result = cur.fetchone()
    cur.close()
    return result['name'] if result else None
