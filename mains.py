from flask import Flask,render_template,request,jsonify

from utils import MedicalInsurance

app = Flask(__name__)

@app.route('/')

def hello_flask():
    
    print('Medical Charges Prediction...')
    return render_template('index.html')

@app.route('/predict_charges',methods=['POST','GET'])

def charges_info():
    
    if request.method == 'GET':
        print('GET Method')
        
        # data = request.form
        # age = eval(data['age'])
        # sex = data['sex']
        # bmi = eval(data['bmi'])
        # children = eval(data['children'])
        # smoker = data['smoker']
        # region = data['region']
        
        age = eval(request.args.get('age'))
        sex = request.args.get('sex')
        bmi = eval(request.args.get('bmi'))
        children = eval(request.args.get('children'))
        smoker = request.args.get('smoker')
        region = request.args.get('region')
        
        med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
        
        charges = med_ins.get_predicted_charges()
        
        return render_template('index.html',prediction=round(charges,2))

        # return jsonify({'Result':f'Medical Charges : {round(charges,2)} Rs. /-'})

print('__name__ :',__name__) 
   
if __name__ == '__main__':
    
    app.run()