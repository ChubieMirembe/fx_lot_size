'''
Simple program to calculate lot size in forex
'''

ex_list = ['EURUSD', 'CHFJPY', 'EURJPY', 'NZDJPY', 'AUDUSD', 'CADJPY',
       'AUDJPY', 'NZDUSD', 'GBPUSD', 'GBPJPY', 'AUDNZD', 'AUDCAD',
       'AUDCHF', 'GBPCHF', 'GBPCAD', 'USDJPY', 'GBPNZD', 'EURCHF',
       'NZDCHF', 'CADCHF', 'NZDCAD', 'EURCAD', 'EURNZD', 'GBPAUD',
       'EURGBP', 'EURAUD', 'USDCAD', 'USDCHF']

pair_list = ['X', 'GBP', 'USD', 'JPY', 'EUR', 'CAD', 'AUD']

def basec():
    '''
    Calculates the lot size if the account currency is the same
    as the base currency of the pair
    '''
    global pip_value
    price = float(input("Enter the current price of the pair: \n"))
    pip_value = pip_value*price
    units = round((pip_value/multiplier), 0)
    lot_size = round((units/100000), 2)

    print("\nUnits: " + str(units))
    print("Lot Size: "+ str(lot_size))

def counterc():
    '''
    Calculates the lot size if the account currency is the same
    as the counter currency of the pair
    '''
    global pip_value
    units = round((pip_value/multiplier), 0)
    lot_size = round((units/100000), 2)

    print("\nUnits: " + str(units))
    print("Lot Size: "+ str(lot_size))

def neitherc():
    '''
    Calculates the lot size if the account currency is not the same
    as the base/counter currency of the pair
    '''
    global pip_value
    
    for i in ex_list:
        if str(account_currency) in str(i) and str(pair[3:6]) in str(i):
            calc_pair = i
            continue
    
    ex_rate = float(input(f"Enter the current price of {calc_pair}: \n"))
    pip_value = pip_value*ex_rate
    units = round((pip_value/multiplier), 0)
    lot_size = round((units/100000), 2)

    print("\nUnits: " + str(units))
    print("Lot Size: "+ str(lot_size))

print('1) GBP \t 4) EUR')
print('2) USD \t 5) CAD')
print('3) JPY \t 6) AUD')

account_currency = int(input("Select your account currency \n"))
account_currency = pair_list[account_currency]
print(account_currency)
capital = int(input("Enter you capital: \n"))
risk = int(input("How much would you like to risk(%): \n"))/100
stop_loss = int(input("How far away is your stop loss (pips): \n"))
pair = input("Enter the pair you would like to trade: \n").upper()

if 'JPY' in pair:
    multiplier = 0.01
else:
    multiplier = 0.0001

cash_risk = capital*risk
pip_value = cash_risk/stop_loss

if str(pair[0:3]) == str(account_currency):
    basec()
elif str(pair[3:6]) == str(account_currency):
    counterc()
else:
    neitherc()
