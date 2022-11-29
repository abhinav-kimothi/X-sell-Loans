from flask import Flask, request, jsonify
import loan_predictor
import json

app=Flask(__name__)

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

if __name__=='__main__':
    app.run(debug=True)


