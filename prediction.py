import pickle
from pandas import DataFrame, get_dummies

model = pickle.load(open('finalized_model.sav','rb'))
one_hot_columns = pickle.load(open('featuressm_dummies_colomn.sav','rb'))
real_columns = pickle.load(open('real_colomn.sav','rb'))

def hasilresult(x):
    if x == 0 :
        return 'Sorry you dont get approve'
    else :
        return 'You get approve'

def prediction(data):
    df = DataFrame(data,index=[0])
    df = get_dummies(df)
    df = df.reindex(columns=one_hot_columns, fill_value=0)
    hasil = model.predict(df)
    hasilnya = hasilresult(hasil)
    return hasilnya

