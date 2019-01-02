from flask import Flask,redirect,request,url_for,render_template
import time
import re

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])

def trykare():
  if request.method == "GET":
    return render_template("indexJS.html")
  if request.method == "POST":
    if request.form["usn"] == "" or request.form["dob"] == "":
       msg="All form fields are required"
       return render_template("indexJS.html",msg=msg)
    try:
        time.strptime(request.form["dob"],"%d/%m/%Y")
    except ValueError:
        msg="Date is invalid"
        return render_template("indexJS.html",msg=msg)
    usn_pattern="^[0-9][A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]$"
    if not re.match(usn_pattern,request.form["usn"]):
        msg="usn is invalid"
        return render_template("indexJS.html",msg=msg)
    s1=int(request.form["m1"])
    s2=int(request.form["m2"])
    s3=int(request.form["m3"])
    avg=(s1+s2+s3)/3
  return render_template("success.html",avg=avg)
if __name__ == '__main__':
 app.run()
