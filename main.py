from flask import Flask, request, render_template, redirect, url_for
import pyshorteners
import qrcode
from io import BytesIO
import base64

app = Flask(__name__, static_folder='static')
shortener = pyshorteners.Shortener()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['url']
    shortened_url = shortener.tinyurl.short(original_url)
    qr = qrcode.make(shortened_url)
    buffered = BytesIO()
    qr.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return render_template('result.html', shortened_url=shortened_url, qr_code=img_str)


if __name__ == '__main__':
    app.run(debug=True)