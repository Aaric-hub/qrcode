# imports...
import qrcode
from PIL import Image
from flask import Flask, request, render_template, redirect
from flask_cors import cross_origin
import base64
import io

app = Flask(__name__)

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/qrgenerator", methods = ["GET", "POST"])
@cross_origin()
def main():
    print("enterned 1")
    if request.method == 'POST' and request.files:
        if request.files:
            print("enterned 2")
            file = request.files['File']
            file = file.filename
            #print(file.filename)
            #print(type(file.filename))
            print("enterned 3")
            img = qrcode.make(file)
            file = file.split('.')[0]
            img.save(f'output/result.png')
            i = Image.open('output/result.png')
            data = io.BytesIO()
            i.save(data,'JPEG')
            encode_img_data = base64.b64encode(data.getvalue())
            return render_template('home.html',file=encode_img_data.decode("UTF-8"))
            #return redirect(request.url)
    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)