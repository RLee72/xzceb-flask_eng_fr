from machinetranslation import translator
from deep_translator import MyMemoryTranslator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    french_text = MyMemoryTranslator(source='english',target='french').translate(textToTranslate)
    # Write your code here
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    english_text = MyMemoryTranslator(source='french',target='english').translate(textToTranslate)
    return english_text
@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
