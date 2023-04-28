from flask import Flask, render_template, request
from email_verifier import is_valid_email


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    # checking if the method is POST
    if request.method == 'POST':
        # getting the email from the form input
        email = request.form['email-address']
        if is_valid_email(email) == True:
            response = f'Your email, {email} is valid'
            return render_template('index.html', response=response)
        else:
            response = f'Your email, {email} is not valid'
            return render_template('index.html', response=response)
    return render_template('index.html')




if __name__ == '__main__':
    app.run()
