from flask import render_template, request
# import json
import os
from src.config import app  #, db_content


@app.route('/logout/')
def logout():
    return render_template('')