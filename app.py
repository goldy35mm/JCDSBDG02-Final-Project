from flask import Flask, render_template, request
from cleaning_data import data_loans
from plots import graph1,graph2, graph3, graph4
from prediction import prediction
from data import purpose, years_in_current_job, term, homeowner



# Translate flask to python object
app = Flask(__name__)




@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')    

@app.route('/data')
def table_data():
    datal = data_loans()
    return render_template('table_data.html', data = datal)


@app.route('/graph1')
def visualization():
    data = graph1()
    return render_template('plots.html',data=data)

@app.route('/graph2')
def visualization2():
    data = graph2()
    data2 = graph4()
    return render_template('plots2.html',data=data, data2=data2)


@app.route('/graph3')
def visualization3():
    data = graph3()
    return render_template('plots3.html',data=data)
  

@app.route('/prediction', methods=['GET','POST'])
def index_prediction():
    if request.method == 'POST':
        data = request.form
        data = data.to_dict()
        data['Credit Score'] = float(data['Credit Score'])
        data['Current loan amount'] = float(data['Current loan amount'])
        data['Number of open accounts'] = float(data['Number of open accounts'])
        hasil = prediction(data)
       

        return render_template('result.html', hasil_prediction=hasil)

    return render_template('prediction.html',data_purpose=sorted(purpose), data_years_in_current_job = sorted(years_in_current_job))


if __name__ =='__main__':
    app.run(debug=True, port=3000)