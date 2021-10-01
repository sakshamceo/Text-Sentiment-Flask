from flask import Flask, render_template,request
import numpy as np
from textblob import TextBlob
application = Flask(__name__)

@application.route("/")
def my_form():
    return render_template('index.html')

@application.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    blob1=TextBlob(text)
    if blob1.sentiment[0]>0:
     label = "\U0001f600 Positive"
     return(render_template('index.html', variable= label))

    elif blob1.sentiment[0]==0:
     label = "\U0001F636 Nuetral"
     return(render_template('index.html', variable= label))

    else:
     label= "\U0001F614 Negative"

     return(render_template('index.html', variable= label))    
  


if __name__ == "__main__":
     application.run(debug=True)   