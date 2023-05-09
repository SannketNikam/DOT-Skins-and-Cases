from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dote.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Index Page Table
class Login(db.Model): #type: ignore
    sno = db.Column(db.Integer, primary_key = True, autoincrement = True)
    fullname = db.Column(db.String(50), nullable = True)
    email = db.Column(db.String(50), nullable = True)
    password = db.Column(db.String(50), nullable = True)

    def __repr__(self) -> str:
        return f"{self.fullname} - {self.email} - {self.password}"

# Feedback Page Table
class Feedback(db.Model): #type: ignore
    sno = db.Column(db.Integer, primary_key = True, autoincrement = True)
    fname = db.Column(db.String(20), nullable = True)
    lname = db.Column(db.String(20), nullable = True)
    phone = db.Column(db.Integer, nullable = True)
    emailID = db.Column(db.String(50), nullable = True)
    message = db.Column(db.Text, nullable = True)
    address = db.Column(db.String(500), nullable = True)

    def __repr__(self) -> str:
        return f"""
        Name: {self.fname} {self.lname} -
        Phone {self.phone} -
        Email: {self.emailID} -
        Message: {self.message} -
        Address: {self.address}
        """
# Checkout Page Table
class Checkout(db.Model): #type: ignore
    sno = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50), nullable = True)
    phone = db.Column(db.Integer, nullable = True)
    address = db.Column(db.String(500), nullable = True)
    product = db.Column(db.String(100), nullable = True)
    
    def __repr__(self) -> str:
        return f"{self.name} - {self.phone} - {self.address} - {self.product}"

# Index Page / Sign-up Page
@app.route("/")
@app.route("/sign-up", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]
        login = Login(fullname = fullname, email = email, password = password)
        db.session.add(login)
        db.session.commit()

    allLogin = Login.query.all()
    return render_template("sign_up.html", allLogin = allLogin)
app.add_url_rule("/sign_up", "signup", signup)

# Log In Page
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]
        login = Login(fullname = fullname, email = email, password = password)
        db.session.add(login)
        db.session.commit()

    allLogin = Login.query.all()
    return render_template("login.html", allLogin = allLogin)
app.add_url_rule("/login", "login", login)

# Homepage
@app.route("/homepage", methods=["GET","POST"])
def homepage():
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]
        login = Login(fullname = fullname, email = email, password = password)
        db.session.add(login)
        db.session.commit()

    allLogin = Login.query.all()
    return render_template("homepage.html", allLogin = allLogin)
app.add_url_rule("/homepage", "homepage", homepage)

# Products Page
def products():
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]
        login = Login(fullname = fullname, email = email, password = password)
        db.session.add(login)
        db.session.commit()

    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        emailID = request.form["emailID"]
        phone = request.form["phone"]
        message = request.form["message"]
        feedback = Feedback(fname = fname, lname = lname, emailID = emailID, phone = phone, message = message)
        db.session.add(feedback)
        db.session.commit()
    
    allLogin = Login.query.all()
    allFeedback = Feedback.query.all()
    return render_template("/products.html", allLogin = allLogin, allFeedback = allFeedback)
app.add_url_rule("/products", "products", products)

# Contact Page
@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]
        login = Login(fullname = fullname, email = email, password = password)
        db.session.add(login)
        db.session.commit()

    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        emailID = request.form["emailID"]
        phone = request.form["phone"]
        message = request.form["message"]
        feedback = Feedback(fname = fname, lname = lname, emailID = emailID, phone = phone, message = message)
        db.session.add(feedback)
        db.session.commit()

    allLogin = Login.query.all()
    allFeedback = Feedback.query.all()
    return render_template("/contact.html", allLogin = allLogin, allFeedback = allFeedback)
app.add_url_rule("/contact", "contact", contact)

# About Page
def aboutus():
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]
        login = Login(fullname = fullname, email = email, password = password)
        db.session.add(login)
        db.session.commit()
    
    allLogin = Login.query.all()
    return render_template("/aboutus.html", allLogin = allLogin)
app.add_url_rule("/aboutus", "about", aboutus)

# Google Page
def google():
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]
        login = Login(fullname = fullname, email = email, password = password)
        db.session.add(login)
        db.session.commit()
    
    allLogin = Login.query.all()
    return render_template("/googledetails.html", allLogin = allLogin)
app.add_url_rule("/googledetails", "google", google)

# iPhone Page
def iphone():
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]
        login = Login(fullname = fullname, email = email, password = password)
        db.session.add(login)
        db.session.commit()
    
    allLogin = Login.query.all()
    return render_template("/iphonedetails.html", allLogin = allLogin)
app.add_url_rule("/iphonedetails", "iphone", iphone)

# Oneplus Page
def oneplus():
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]
        login = Login(fullname = fullname, email = email, password = password)
        db.session.add(login)
        db.session.commit()
    
    allLogin = Login.query.all()
    return render_template("/oneplusdetails.html", allLogin = allLogin)
app.add_url_rule("/oneplusdetails", "oneplus", oneplus)

# Cart Page
def cart_page():
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]
        login = Login(fullname = fullname, email = email, password = password)
        db.session.add(login)
        db.session.commit()
    
    allLogin = Login.query.all()
    return render_template("/cart-page.html", allLogin = allLogin )
app.add_url_rule("/cart-page", "cart_page", cart_page)

# Checkout Page
@app.route("/checkout", methods=["GET","POST"])
def checkout():
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]
        login = Login(fullname = fullname, email = email, password = password)
        db.session.add(login)
        db.session.commit()
    

    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        address = request.form["address"]
        product = 'Oneplus 10r Skin'
        checkout = Checkout(name = name, phone = phone, address = address, product = product)
        db.session.add(checkout)
        db.session.commit()

    allLogin = Login.query.all()
    allCheckout = Checkout.query.all()
    return render_template("/checkout-page.html", allLogin = allLogin, allCheckout = allCheckout)
app.add_url_rule("/checkout-page", "checkout", checkout)

@app.route("/tp1", methods=["GET","POST"])
def tp1():
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        emailID = request.form["emailID"]
        phone = request.form["phone"]
        message = request.form["message"]
        feedback = Feedback(fname = fname, lname = lname, emailID = emailID, phone = phone, message = message)
        db.session.add(feedback)
        db.session.commit()

    allFeedback = Feedback.query.all()
    return render_template("/tp1.html", allFeedback = allFeedback)
app.add_url_rule("/tp1", "tp1", tp1)

@app.route("/tp2", methods=["GET","POST"])
def tp2():
    if request.method == "POST":
        name = request.form.get("name")
        # name = request.form["name"]
        phone = request.form["phone"]
        address = request.form["address"]
        product = 'Oneplus 10r Skin'
        checkout = Checkout(name = name, phone = phone, address = address, product = product)
        db.session.add(checkout)
        db.session.commit()
        
    allCheckout = Checkout.query.all()
    return render_template("/tp2.html", allCheckout = allCheckout)
app.add_url_rule("/tp2", "tp2", tp2)

@app.route("/delete")
def delete():
    db.session.query(Login).delete()
    db.session.commit()
    return redirect("/")

# Deployment

if __name__ == "__main__":

    if not path.exists("./instace/dote.db"):
        app.app_context().push()
        db.create_all()
        # Creating database if it doesn't exist
    
    else:
        pass
        # Ignoring the query as database already exists

    # app.run(debug = False, host = '0.0.0.0')
    app.run(debug = False, host = '0.0.0.0', port = 6969)