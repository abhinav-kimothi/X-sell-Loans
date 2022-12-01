from flask import Flask, request, jsonify, render_template
import loan_predictor
import json

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',pred='Borrow Now and Save Later',keys='Get a Personal Loan at an Incredible Discount!')


@app.route('/kim/v1/personal-loan',methods=['POST','GET'])
def lpredict():
    args_data=request.get_data()
    data=json.loads(args_data)
    income=data.get('income')
    ccavg=data.get('ccavg')
    cd_account=int(data.get('cd'))
    education=data.get('education')
    family=int(data.get('family'))

    print(data)

    response=jsonify(loan_predictor.prediction(float(income),float(ccavg),cd_account,education,family))

    return response

@app.route('/predict',methods=['POST','GET'])
def predict():
    
    int_features=[x for x in request.form.values()]
    income=int_features[1]
    ccavg=int_features[2]
    cd_account=int_features[3]
    education=int_features[4]
    family=int_features[5]

    outcome=loan_predictor.prediction(float(income),float(ccavg),int(cd_account),education,int(family))

    if outcome=="Likely":
        pred="Congratulations "+int_features[0]+"! You've unlocked the key to great savings!"
        keys="Visit your nearest branch or talk to our representative to claim your discount"
    else:
        pred="We're sorry, we wish you could have taken advantage of this offer!"
        keys="Visit your nearest branch or talk to our representative for the best rates for you"


    return render_template('index.html',pred=pred,keys=keys)

if __name__=='__main__':
    app.run(debug=True)


