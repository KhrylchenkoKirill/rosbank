import datetime
import numpy as np

def cashflow(user): 
    info = sorted(user[['trx_category', 'amount', 'date', 'time', 'MCC']].to_dict('records'), 
                     key = lambda x: (x['date'], x['time']))

    history = {}
    curr_transaction = info[0]
    curr_date = curr_transaction['date']
    curr_category = curr_transaction['trx_category']
    curr_mcc = curr_transaction['MCC']

    history[curr_date] = {}
    history[curr_date][curr_category] = {}
    history[curr_date][curr_category][curr_mcc] = [curr_transaction['amount']]

    for transaction in np.arange(1, len(info)):
        curr_transaction = info[transaction]
        curr_date = curr_transaction['date']
        curr_category = curr_transaction['trx_category']
        curr_mcc = curr_transaction['MCC']

        if history.get(curr_date, 0) == 0:
            history[curr_date] = {}
            history[curr_date][curr_category] = {}
            history[curr_date][curr_category][curr_mcc] = [curr_transaction['amount']]
        else:
            if history[curr_date].get(curr_category, 0) == 0:
                history[curr_date][curr_category] = {}
                history[curr_date][curr_category][curr_mcc] = [curr_transaction['amount']]
            else:
                if history[curr_date][curr_category].get(curr_mcc, 0) == 0:
                    history[curr_date][curr_category][curr_mcc] = [curr_transaction['amount']]
                else:
                    history[curr_date][curr_category][curr_mcc] += [curr_transaction['amount']]
    return history

