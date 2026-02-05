from flask import Flask, request, make_response
import argostranslate.package
import argostranslate.translate
import json

def make_error(error_message = ""):
  return json.dumps({ "status": "error", "message": str(error_message), "data": None })

def make_ok(data = {}):
  return json.dumps({ "status": "ok", "message": None, "data": data })

# argostranslate
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
  pkg for pkg in available_packages if pkg.from_code == "en" and pkg.to_code == "pt"
)
download_path = package_to_install.download()
argostranslate.package.install_from_path(download_path)

# flask
app = Flask(__name__)

@app.get("/")
def index():
  return "Translate API v1"

@app.get("/api/v1")
def apiv1():
  return "Translate API v1"

@app.get("/api/v1/translate")
def translate_get():
  resp = make_response()
  resp.data = make_ok({ "text": request.args.get("text") })
  return resp

@app.post("/api/v1/translate")
def translate_post():
  json_data = request.get_json()
  resp = make_response()
  if request.headers["Content-Type"] != "application/json":
    resp.data = make_error("Not a JSON request")
  else:
    resp.data = make_ok({ "text": "none" if json_data is None else json_data["text"] })
  return resp

@app.post("/api/v1/languages")
def languages_post():
  resp = make_response()
  resp.data = make_ok({ "languages": list() })
  return resp
