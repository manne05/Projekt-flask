#countRoute.py
from flask import Flask, session
app = Flask(__name__)

# Include the extra two lines below
app.secret_key = 'secr3t'
app.config['SESSION_TYPE'] = 'filesystem'
@app.route('/<int:y>')

def count(y):
  p = session.get('sum', None)
  if not p:
    session['sum'] = y
  else:
    session['sum']+=y
    return str(session['sum'])
    
@app.route('/')
def home():
  return 'Congratulations for successfully open this page. Kindly add /15 or some random number'
  
if __name__ == '__main__':
  app.run(host='0.0.0.0')