from flask import Flask, request
import argostranslate.package
import argostranslate.translate

# argostranslate
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
  pkg for pkg in available_packages if pkg.from_code == 'en' and pkg.to_code == 'pt'
)
download_path = package_to_install.download()
argostranslate.package.install_from_path(download_path)

# flask
app = Flask(__name__)

@app.get('/')
def index():
  return 'Translate API v1'

@app.get('/api/v1')
def apiv1():
  return 'Translate API v1'

@app.post('/api/v1/translate')
def translate():
  text = request.form['text']
  translated_text = argostranslate.translate.translate(text, 'en', 'pt')
  return { 'status': 'ok', 'message': None, 'data': translated_text }

@app.post('/api/v1/languages')
def translate():
  languages = argostranslate.translate.get_installed_languages()
  return { 'status': 'ok', 'message': None, 'data': languages }
