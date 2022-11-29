import pickle
import numpy as np
import pandas as pd

scaler=pickle.load(open('./Model_Objects/scaler.pkl','rb'))
model=pickle.load(open('./Model_Objects/pl_prediction_model.pkl','rb'))

def prediction(Income, CCAvg, cd_account, education, family_size):
    income_log=np.log(Income)
    ccavg_log=np.log(CCAvg)
    if education=='undergrad':
        ed_undergrad=1
        ed_postgrad=0
        ed_advanced=0
    elif education == 'postgrad':
        ed_undergrad=0
        ed_postgrad=1
        ed_advanced=0
    elif education == 'advanced':
        ed_undergrad=0
        ed_postgrad=0
        ed_advanced=1   
    else:
        ed_undergrad=0
        ed_postgrad=0
        ed_advanced=0

    if family_size==1:
        family_1=1
        family_2=0
        family_3=0
        family_4=0
    elif family_size==2:
        family_1=0
        family_2=1
        family_3=0
        family_4=0
    elif family_size==3:
        family_1=0
        family_2=0
        family_3=1
        family_4=0
    elif family_size>=4:
        family_1=0
        family_2=0
        family_3=0
        family_4=1
    else:
        family_1=0
        family_2=0
        family_3=0
        family_4=0
    obj=np.array([Income,CCAvg,cd_account,income_log,ccavg_log,ed_undergrad,ed_postgrad,ed_advanced,family_1,family_2,family_3,family_4]).reshape(1,-1)
    obj_df=pd.DataFrame(obj, columns=['Income', 'CCAvg', 'CD Account', 'Income_log', 'CCAvg_log',
       'ed_undergrad', 'ed_postgrad', 'ed_advanced', 'family_1', 'family_2',
       'family_3', 'family_4'])
    obj_scl=scaler.transform(obj_df)
    outcome=pd.DataFrame(model.predict(obj_scl))
    prob=pd.DataFrame(model.predict_proba(obj_scl))
    if outcome.iloc[0][00]==0:
        offer="Not likely"
        probability=str(prob.iloc[0][0])
    else:
        offer="Likely"
        probability=str(round(prob.iloc[0][1]*100,2))+"%"
    

    response={
        "data":{
            "outcome":offer,
            "probability":probability
        }
    }

    return response

print(prediction(79, 3.6, 1, 'postgrad', 1))


 
