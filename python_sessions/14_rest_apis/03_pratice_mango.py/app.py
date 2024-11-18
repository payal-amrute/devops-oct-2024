from flask import Flask, request
import json
app = Flask(__name__)

@app.get("/welcome")
def welcome():
    return "Welcome to class"
