#countY.py

from flask import Flask, render_template, session
app = Flask(__name__)

# Include the extra two lines below
app.secret_key = 'secr3t'
app.config['SESSION_TYPE'] = 'filesystem'
@app.route('/')
def home():
  y = session.get('y', None)
  if not y:
    session['y'] = 1
  elif y>=10:
    session.clear()
    return "The Session is clear"
  else:
    session['y']+=1
    return "The Total Number of refreshes for this user is: "+str(session['y'])
    
if __name__ == '__main__':
  app.run(host='0.0.0.0')