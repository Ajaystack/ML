from flask import Flask,request, url_for, redirect, render_template, request, jsonify
import pickle 
import numpy as np 

app = Flask(__name__)
pkl_filename='trained_model.pkl'
model=pickle.load(open(pkl_filename ,'rb'))

@app.route('/', methods=['POST','GET']) 
def housepredict():
    if request.method == 'POST':
        V1 = request.form['V1']
        V2 = request.form['V2']
        V4 = request.form['V4']
        V5 = request.form['V5']  
        V7 = request.form['V7']
        V8 = request.form['V8']
        V13 = request.form['V13']
        V17 = request.form['V17']
        V19 = request.form['V19']
        V20 = request.form['V20']
        V23 = request.form['V23']
        V24 = request.form['V24']
        V27 = request.form['V27']
        V33 = request.form['V33']
        V34 = request.form['V34']
        V35 = request.form['V35']
        V36 = request.form['V36']
        x3 = [[V1,V2, 110 ,V4,V5,4,V7,V8,5,2015,1,3,V13,3,2,1,V17,4,V19,V20,3,4,V23,V24,2015,1,V27,225,3,100,400,2,V33,V34,V35,V36]]
        res = 'Estimate price : INR ' + str(70 * int(model.predict(x3))) + '/-'
        return render_template('house_result.html', res=res)
    return render_template('house_predict.html')


if __name__ == '__main__': 
   app.run(debug=False)