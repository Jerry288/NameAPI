import json
import random
from flask import *

app = Flask(__name__)

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

if __name__ =='__main__':
  app.run(port=7777)
