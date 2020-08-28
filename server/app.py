from flask_cors import CORS
from flask import Flask,jsonify,request,make_response,redirect,send_file
import pandas as pd 
import os
#=============================================================================================#

app = Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True
app.config['BASE_URL'] = 'http://127.0.0.1:5000'


#=============================================================================================#

#API calls


@app.route('/calculate',methods=['POST'])
def calculate():
    try:
        req_data = request.form
        op1=float(req_data['op1'])
        op2=float(req_data['op2'])
        operator=req_data['operator']
        result=calc_fuc(op1,op2,operator)
        db['Operand_1'].append(op1)
        db['Operand_2'].append(op2)
        db['Operator'].append(operator)
        db['Result'].append(result)
        return jsonify({'result':result})
    except:
        return jsonify({'result':None})


@app.route('/download',methods=['GET'])
def download():
    try:
        df=pd.DataFrame.from_dict(db)
        df.to_csv('results.csv')
        db={
            'Operand_1':[],
            'Operand_2':[],
            'Operator':[],
            'Result':[]
        }
        return send_file('results.csv', as_attachment=True)
    except:
        return None


#=============================================================================================#

#Utitlity Functions
def calc_fuc(op1,op2,operator):
    if operator=='/':
        if op2!=0:
            return op1/op2;
        else:
            return None;
    elif operator=='+':
        return op1+op2
    elif operator=='-':
        return op1-op2
    elif operator=='x':
        return op1*op2
    elif operator=='%':
        return op1/op2;

#=============================================================================================#

#Command to run the app
if __name__ == '__main__':
    db={
        'Operand_1':[],
        'Operand_2':[],
        'Operator':[],
        'Result':[]
    }
    app.config['SECRET_KEY']='secret123'
    app.run(debug=True)