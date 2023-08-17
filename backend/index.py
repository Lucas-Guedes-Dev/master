from flask import Flask
from controllers.view_pessoa import ViewPessoa

import os
app = Flask(__name__)

SECRET_KEY = os.urandom(12).hex()
app.config['SECRET_KEY'] = SECRET_KEY

app.add_url_rule("/cadastro-pessoa", view_func=ViewPessoa.as_view('pessoa'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)