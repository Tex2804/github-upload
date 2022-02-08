from flask import Flask, render_template, request
import calculator
import cmath
from math import sqrt
import math
import collections
app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def start():
  errors = []
  if request.method == "POST":
    a = None
    b = None
    c = None
    
    #calc = None
    try:
      a = float(request.form["a"])
    except:
      errors.append("{!r} is not a number.\n".format(request.form["a"]))
    try:
      b = float(request.form["b"])
    except:
      errors.append("{!r} is not a number.\n".format(request.form["b"]))
      error = "{!r} is not a number.".format(request.form["b"])
      errors.append(error)
    try:
      c = float(request.form["c"])
    except:
      errors.append("{!r} is not a number.\n".format(request.form["c"]))
    if a is not None and b is not None and c is not None:
      result = calculator.main1(a,b,c)
      return render_template("index.html", result=result)
    return render_template("index.html", result=errors)
  return render_template("index.html", result=errors)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
