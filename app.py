from flask import Flask,render_template,request
import sqlite3 as sql
import requests

app=Flask("__name__")

@app.route("/",methods=["post","get"])
def fun():
    if request.method == "POST":
        id=request.form["id"]
        scheme_name=request.form["scheme_name"]
        nav=request.form["nav"]
        conn = sql.connect("insert.db")
        cur =conn.cursor()
        cur.execute("insert into db (id,scheme_name,nav) values (?,?,?)", (id,scheme_name,nav))
        conn.commit()

    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)