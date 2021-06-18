# vim app001/__init__.py

from flask import Flask

app = Flask (__name__)

from app001 import routes
