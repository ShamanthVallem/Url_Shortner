from flask import Flask, render_template, request, redirect
import shortuuid
import database

app = Flask(__name__)
database.create_table()

serverAddress = 'localhost:5000'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/url-shortner", methods=['get', 'post'])
def url_shortner(): 
    mainUrl=request.form["mainUrl"]
    token_key = shortuuid.uuid()
    database.insert_url(mainUrl, token_key)
    short_url = f'http://{serverAddress}/{token_key}'
    return render_template("shortner.html",  mainUrl=mainUrl, short_url = short_url)


@app.route('/<token_key>')
def redirect_to_main_url(token_key):
    longUrl = database.fetch_long_url(token_key)
    print(longUrl)
    if longUrl:
        return redirect(longUrl)
    else:
        return "URL not found", 404

if __name__ == "__main__":
    app.run(debug=True)