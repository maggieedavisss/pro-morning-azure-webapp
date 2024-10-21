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

@app.route('/sql-chatbot')
def sql_chatbot():
    return redirect("https://python-flask-sqlbot-app.azurewebsites.net/")

@app.route('/pdf-narrator')
def pdf_narrator():
    return redirect("https://gen-ai-web-app.azurewebsites.net/document_insight_via_chat")  

@app.route('/power-bi-demo')
def power_bi_demo():
    return redirect("https://app.powerbi.com/groups/me/apps/1f7cd510-8c93-4e5f-8cef-312f3bbf0d01/reports/363ee684-634c-43da-b040-8539933cbf13/42ba0471426783ecc124?ctid=978794b6-9c6b-4307-ada4-42e472e0e336&experience=power-bi")

@app.route('/azure-etf-ratings-chatbot')
def azure_etf_ratings_chatbot():
    return redirect("https://morningstar-ratings.azurewebsites.net/")

@app.route('/azure-etf-returns-chatbot')
def azure_etf_returns_chatbot():
    return redirect("https://morningstar-returns.azurewebsites.net/")  

@app.route('/financial-literacy-chatbots')
def azure_etf_returns_chatbot():
    return redirect("https://financial-literacy.azurewebsites.net/")

if __name__ == '__main__':
    app.run(debug=True) 
