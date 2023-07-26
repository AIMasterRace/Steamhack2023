import json
from models.model import Inserttable, db
from services.service import insert_logic, create_logic
from flask import render_template, redirect, url_for

def home_page():
    return render_template('index.html')

def map_page():
    pass

def rank_page():
    pass

def about_page():
    pass

def create_db():
    create_logic()

def insert_db():
    insert_logic() 