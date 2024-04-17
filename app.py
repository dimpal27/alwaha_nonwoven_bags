from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
app = Flask(__name__)


# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'alwahabags@gmail.com'
app.config['MAIL_PASSWORD'] = 'alwaha@123'
app.config['MAIL_DEFAULT_SENDER'] = 'alwahabags@gmail.com'
mail = Mail(app)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form['first_name']
        print("====>",first_name)
        phone = request.form['phone']
        print("email", phone)
        email_address = request.form['email_address']
        contact_subject = request.form['contact_subject']
        message = request.form['message']
        print("message", email_address)
        # Send email
        recipients = ['alwahabags@gmail.com']
        msg = Message('New Contact Form Submission', recipients=recipients)
        msg.body = f'Name: {first_name}\nSubject:{contact_subject}\nEmail: {email_address}\nMessage: {message}'
        print(msg)
        mail.send(msg)

        # Send WhatsApp message (using Twilio)
        # Code for sending WhatsApp message goes here

        return redirect(url_for('index'))

    return render_template('contact-us.html')


@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

# Define route for the homepage


@app.route('/')
def index():
    return render_template('index.html')

# Define route for other pages


@app.route('/about')
def about():
    return render_template('about-us.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/product')
def product():
    return render_template('product.html')


if __name__ == '__main__':
    app.run(debug=True)
