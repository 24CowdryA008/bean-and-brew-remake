import os

from flask import Flask, render_template, url_for
app=Flask(__name__)

@app.route("/")
def Home():
    return render_template("Home.HTML")

@app.route("/website2")
def website2():
    return render_template("Website2.HTML")

@app.route("/Hamper")
def HamperPurchasing():
    return render_template("HamperPurchasing.HTML")

@app.route("/Lesson")
def BakingLessons():
    return render_template("BakingLessons.HTML")

@app.route("/Login")
def LoginPage():
    return render_template("LoginPage.HTML")

@app.route("/RegisterPage")
def RegisterPage():
    return render_template("RegisterPage.HTML")

@app.route("/BakedGoods")
def BakedGoods():
    return render_template("BakedGoods.HTML")

@app.route("/Support")
def Support():
    return render_template("Support.HTML")

@app.route("/RestaurantBooking")
def RestaurantBooking():
    return render_template("RestaurantBooking.HTML")

@app.route("/TermsAndConditions")
def TermsAndConditions():
    return render_template("TermsAndConditions.html")

if __name__=="__main__": # Make's it so when you run the website and make changes, you don't have to restart it
    app.run(debug=True)

