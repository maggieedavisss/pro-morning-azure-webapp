import os
from flask import Flask, render_template, send_from_directory, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    print('Request for index page received')
    return render_template('index.html')  # Render the updated index.html with the buttons

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/etf-chatbot')
def sql_chatbot():
    return redirect("https://etf-beginners.azurewebsites.net/")

@app.route('/morningstar-chatbot')
def pdf_narrator():
    return redirect("https://learn-about-morningstar.azurewebsites.net/)  

@app.route('/financial-literacy-chatbot')
def powerbi_demo():
    return redirect("")

if __name__ == '__main__':
    app.run(debug=True)
