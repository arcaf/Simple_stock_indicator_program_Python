#Francisco Arca 95184171 Outside the Wall
import datetime
import stock_indicator
import download_url
import stock_signal
def console() -> None:
    '''Shows the user the first interface of the game, and
     downloads stock information.
    '''
    print("Welcome to OUTSIDE THE WALL")
    Ticker = input('Please enter the Ticker symbol: ').upper()
    print()
    Interf_one = Interface_one()
    
    Interf_two = Interface_two(Interf_one[1])
    url = ('http://ichart.yahoo.com/table.csv?s='+Ticker+
                           '&a='+str(int(Interf_one[0][1])-1)+'&b='+Interf_one[0][2]+
                           '&c='+Interf_one[0][0]+'&d='+str(int(Interf_two[1])-1)+
                           '&e='+Interf_two[2]+'&f='+Interf_two[0]+'&g=d')
    content = download_url.downloading_url(url)
    Interf_three = Interface_three(content)
    console_table(content, Ticker, Interf_three)
    
def Interface_one() -> list:
    ''' Allows the user to identify a Ticker Symbol,
    a start date, an end date, and a signal strategy.'''
    while True:
        try:
            while True:
                Start_date = input('Please enter the start date of the analysis (YYYY-MM-DD): ').split("-")
                print()
                if len(Start_date[0]) != 4:
                    raise ValueError
                elif len(Start_date[1]) != 2:
                    raise ValueError
                elif len(Start_date[2]) != 2:
                    raise ValueError
                else:
                    starting = datetime.date(int(Start_date[0]), int(Start_date[1]), int(Start_date[2]))
                    if starting <= datetime.date.today():
                        return [Start_date, starting]
                        break
                    else:
                        raise ValueError
                break
            break
    
        except ValueError:
            print("Please try a new start date")
            print()
        except IndexError:
            print("Please try a new start date")
            print()

def Interface_two(date: 'date') -> list:
    '''Asks the user for an end date to his/her analysis.'''
    while True:
        try:
            while True:
                End_date = input('Please enter the end date of the analysis (YYYY-MM-DD): ').split("-")
                print()
                if len(End_date[0]) != 4:
                    raise ValueError
                else:
                    ending = datetime.date(int(End_date[0]), int(End_date[1]), int(End_date[2]))
                    if ending <= datetime.date.today() and ending > date:

                        return End_date
                        break
                    else:
                        raise ValueError
                break
            break
        
        except ValueError:
            print("Please try a new end date")
            print()

def Interface_three(content: list) -> list:
    '''Asks the User to provide a signal strategy'''
    while True:
        try:
            result = []
            for i in range(len(content)):
                result.append(content[i][0])
            print("Signal Strategies")
            Signal_Menu = '''s: N-day simple moving average(N: amount of days) \nd: N-day directional indicator
                            '''
            print(Signal_Menu)
            User_signal = str(input('What signal strategy would you like to use? '))
            User_days = int(input('For how many days? '))
            if User_days >= len(result):
                raise IndexError
            if User_signal == 'd':
                User_buy = int(input("What buy threshold would you like to use? "))
                User_sell = int(input("What sell threshold would you like to use? "))
    
                return [User_signal, User_days, User_buy, User_sell]
                break
            elif User_signal == 's':
                return [User_signal, User_days]
                break
            else:
                raise EOFError
        
        except EOFError:
            print('Strategy not acceptable, please try again')
        except ValueError:
            print('Please enter a valid number of days...')
        except IndexError:
            print("The amount of days must be smaller \nthan the amount of days of your analysis")

def console_table(table_content: list, Ticker_symbol: str, user_signal: list) -> None:
    '''Creates  table that will show all the values that belong to an specific
       ticker symbol'''
    result = []
    numbers = []
    new_numbers = []
    signal_list = []
    table_content=table_content[::-1]
    table_content.pop(-1)
    print('SYMBOL:', Ticker_symbol)
    if len(user_signal) == 2:
        print("Simple moving average ("+str(user_signal[1])+"-day)")
        
        for i in range(len(table_content)):
            result.append(table_content[i][4])
            signal_list.append(table_content[i][4])
        for i in range(len(table_content)):
            simp = stock_indicator.Simple_Moving(result[:user_signal[1]], user_signal[1]) 
            simple_avg = simp.execute()
            numbers.append(simple_avg)
            new_numbers.extend(numbers)
            result.pop(0)


        print('DATE          CLOSE    INDICATOR  SIGNAL')
        
        sign = stock_signal.Signal_Simple_moving(user_signal[1], signal_list, numbers, 0, 0)
        sign_simple = sign.execute()
        for i in range(len(table_content)):

            if numbers[i] != 0:
                print('{:10}   {:3}     {:5.2f}     {}'.format(table_content[i][0], table_content[i][4], numbers[i], sign_simple[i]))

            else:
                print('{:10}   {:3}    {}      {}'.format(table_content[i][0], table_content[i][4], '    ', '    '))


    elif len(user_signal) == 4:
        print('Directional ('+str(user_signal[1])+'-day), buy above '+str(user_signal[2])+', sell below '+str(user_signal[3]))
        for i in range(len(table_content)):
            result.append(table_content[i][4])
        x = stock_indicator.Directional_Moving(result, user_signal[1])
        direct_ind = x.execute()
        sign = stock_signal.Signal_Directional(user_signal[1], direct_ind, signal_list, user_signal[2], user_signal[3])
        signal_direct = sign.execute()

        print('DATE          CLOSE    INDICATOR  SIGNAL')
        for i in range(len(table_content)):
            if direct_ind[i] > 0:
                print('{:10}   {:7}     +{:1}        {:4}'.format(table_content[i][0], table_content[i][4], direct_ind[i], signal_direct[i]))
            else:
                print('{:10}   {:7}     {:2}        {:4}'.format(table_content[i][0], table_content[i][4], direct_ind[i], signal_direct[i]))
 


    
if __name__=='__main__':
    console()

