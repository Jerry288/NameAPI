import json
import random
from flask import Flask
from threading import Thread
app = Flask('')

@app.route('/')
def home():
	return  "I'm alive"

def run():
	app.run(host='0.0.0.0',port=8080)

t = Thread(target=run)
t.start()

@app.route("/name/", methods=['GET'])
def getName():
  names = json.loads(open('names.json').read())
  return(names[random.randint(0, len(names))])

@app.route("/lastname/", methods=['GET'])
def lastName():
  lastnames = json.loads(open('lastname.json').read())
  return(lastnames[random.randint(0, len(lastnames))])

@app.route("/fullname/", methods=['GET'])
def fullname():
  lastnames = json.loads(open('lastname.json').read())
  lastname = lastnames[random.randint(0, len(lastnames))]

  names = json.loads(open('names.json').read())
  name = names[random.randint(0, len(names))]

  return(name + " " + lastname)
