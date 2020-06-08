from flask import Flask, render_template, session
app = Flask(__name__)

# 
app_secret_key = 'personal secret'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route("/")
def home():
  return render_template("home.html")
  
@app.route("/about")
def about():
  return render_template("about.html")
  
@app.route("/impressum")
def impressum():
  return render_template("impressum.html")

if __name__ == "__main__":
  app.run(debug=True)
