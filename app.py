import os
from flask import Flask, render_template, send_from_directory, url_for

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
    return "This will be the SQL Chatbot page"  # Placeholder for the SQL Chatbot page

@app.route('/pdf-narrator')
def pdf_narrator():
    return redirect("https://gen-ai-web-app.azurewebsites.net/document_insight_via_chat")

if __name__ == '__main__':
    app.run(debug=True)
