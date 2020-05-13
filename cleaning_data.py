import pandas as pd

def data_loans():
    data_loans = pd.read_csv('bank_loans_clean_data.csv')
    data_loans.drop('Unnamed: 0', axis=1, inplace=True)
    return data_loans

def new_data_loans():
    data_loans = pd.read_csv('bank_loans_clean_data.csv')
    x = list(data_loans['Loan Status'].value_counts().index)
    y = list(data_loans['Loan Status'].value_counts().values)

    new_data_loans_status = pd.DataFrame({
        'Loan Status': x,
        'Total' : y
    })
    return new_data_loans_status


