import os 
from flask import Flask,request,render_template

ALLOWER_EXTENSIONS={'png','jpg','jpeg','gif'}


app=Flask(__name__)