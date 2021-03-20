import os
import json
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash
import datetime

db = SQLAlchemy()

DB_CONFIGURACION = "./dbconfig.json"


