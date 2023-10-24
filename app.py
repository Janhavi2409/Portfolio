from flask import Flask, render_template, request
from form import ContactForm
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = '99b2aaa6a6532aa1a0b4c8abf0dd78a9db46a03fcb8b80f3'

app.config['MAIL_SERVER'] = "smtp.googlemail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'janhavidahatonde@gmail.com'
app.config['MAIL_PASSWORD'] = 'nfdb ocvf kcou zfvk'
mail = Mail(app)

@app.route("/home", methods = ['POST', 'GET'])
def home():
    form = ContactForm()
    if request.method == 'POST':
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        message = form.message.data
        msg = Message(subject, sender = 'janhavidahatonde@gmail.com', recipients=[email])
        msg.body = 'Name: '+name+'\nMessage: '+message
        mail.send(msg)
    return render_template('index.html', form = form)

@app.route("/about")
def about():
    return render_template('/about')

@app.route("/contact")
def contact():
    return render_template('/contact')

if __name__ == "__main__":
    app.run(debug=True)