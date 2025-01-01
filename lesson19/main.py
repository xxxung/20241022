from flask import Flask
import os
from dotenv import load_dotenv
import google.generativeai as genai

app = Flask(__name__)   #這裡是網頁的起點
genai.configure(api_key=os.environ['Gemini_API_KEY'])         #your api key
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
@app.route("/<string:question>")         #/ 根目錄首頁  #/<string:name>
def index(question:str = ""):
    response = model.generate_content(f"{question},回應結果請輸出成為html格式")
    html_format = response.text
    html_format = html_format.replace("```html","").replace("```","")
    return html_format 

@app.route('/hello')    #/hello 那頁
def hello():
    return '<h1>Hello, World</h1>'

#flask --app main run--debug
#pip gunicorn (正式的)
#gunicorn -w 4main:app