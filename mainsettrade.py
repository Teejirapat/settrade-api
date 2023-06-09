import configparser
import pyfiglet
import traceback
import time
import socket
import json
#api settrade
from InvestorLogin import INVESTOR_LOGIN
from InvestorDerivatives import INVESTOR_DERIVATIVES
from InvestorEquity import INVESTOR_EQUITY
from InvestorMarket import INVESTOR_MARKET

def main_serv(client,port,pin,account_no,type,time_out):
    host='127.0.0.1'
    port = int(port)
    s=socket.socket()
    s.bind((host,port))
    s.listen(10)
    print('waiting connect')
    print(f'Port : {port}')

    while True :
        cli,addr =s.accept()
        data=cli.recv(1023).decode('utf-8')
        if not data :
            break
        print('message from client : '+data)
        rec=json.loads(data)

        if type == '0': #tfex
            if rec['type']=='account_info': #"{\"type\": \"account_info\"}"
                data=INVESTOR_DERIVATIVES.account_info(client,account_no)
            
            elif rec['type']=='get_order': #"{\"type\": \"get_order\",\"order_no\":0}"
                data=INVESTOR_DERIVATIVES.get_order(client,account_no,rec['order_no'])
            
            elif rec['type']=='get_orders':#"{\"type\": \"get_orders\"}"
                data=INVESTOR_DERIVATIVES.get_orders(client,account_no)
            
            elif rec['type']=='place_order':#"{\"type\": \"place_order\",\"symbol\":\"PTT\",\"side\":\"Long\",\"position\":\"Open\",\"price_type\":\"MP-MTL\",\"price\":0,\"volume\":100}"
                data=INVESTOR_DERIVATIVES.palce_order(client,account_no,pin,rec['symbol'],rec['side'],rec['position'],rec['price_type'],rec['price'],rec['volume'])
            
            elif rec['type']=='change_order':#"{\"type\": \"change_order\",\"order_no\":ตัวเลข,\"new_price\":ราคาใหม่,\"new_volume\":วอลลุ่มใหม่}"
                data=INVESTOR_DERIVATIVES.change_order(client,account_no,pin,rec['order_no'],rec['new_price'],rec['new_volume'])
            
            elif rec['type']=='cancel_order':#"{\"type\": \"cancel_order\",\"order_no\":ตัวเลข}"
                data=INVESTOR_DERIVATIVES.change_order(client,account_no,pin,rec['order_no'])
            
            elif rec['type']=='cancel_orders':#"{\"type\": \"cancel_orders\",\"order_no\":[ตัวเลข,ตัวเลข,ตัวเลข,ตัวเลข]}"
                data=INVESTOR_DERIVATIVES.cancel_orders(client,account_no,pin,rec['order_no'])
        
        
        elif type == '1': #ซื้อหุ้น
            if rec['type']=='account_info':#"{\"type\": \"account_info\"}"
                data=INVESTOR_EQUITY.account_info(client,account_no)
            
            elif rec['type']=='get_order':#"{\"type\": \"get_order\",\"order_no\":\"string\"}"
                data=INVESTOR_EQUITY.get_order(client,account_no,rec['order_no'])
            
            elif rec['type']=='get_orders':#"{\"type\": \"get_orders\"}"
                data=INVESTOR_EQUITY.get_orders(client,account_no)
            
            elif rec['type']=='place_order':#"{\"type\": \"place_order\",\"symbol\":\"PTT\",\"side\":\"Buy\",\"price_type\":\"MP-MTL\",\"price\":0,\"volume\":100}"
                data=INVESTOR_EQUITY.palce_order(client,account_no,pin,rec['symbol'],rec['side'],rec['price_type'],float(rec['price']),float(rec['volume']),rec['validity_type'])
            
            elif rec['type']=='change_order':#"{\"type\": \"change_order\",\"order_no\":\"string\",\"new_price\":ราคาใหม่,\"new_volume\":วอลลุ่มใหม่}"
                data=INVESTOR_EQUITY.change_order(client,account_no,pin,rec['order_no'],rec['new_price'],rec['new_volume'])
            
            elif rec['type']=='cancel_order':#"{\"type\": \"cancel_order\",\"order_no\":\"string\"}"
                data=INVESTOR_EQUITY.cancel_order(client,account_no,pin,rec['order_no'])
            
            elif rec['type']=='cancel_orders':#"{\"type\": \"cancel_orders\",\"order_no\":[\"string\",\"string\",\"string\",\"string\"]}"
                data=INVESTOR_EQUITY.cancel_orders(client,account_no,pin,rec['order_no'])

        if rec['type']=='get_quote_symbol':#"{\"type\": \"get_quote_symbol\",\"symbol\":\"PTT\"}"

            data=INVESTOR_MARKET.get_quote_symbol(client,rec['symbol'])

        elif rec['type']=='get_market_historical':#"{\"type\": \"get_market_historical\",\"symbol\":\"PTT\",\"interval\":\"1d\",\"limit\":1,\"start\":\"YYYY-mm-ddTHH:MM\",\"end\":\"YYYY-mm-ddTHH:MM\"}"
            #market=INVESTOR_MARKET(time_out)
            data=INVESTOR_MARKET.get_market_historical(client,rec['symbol'],rec['interval'],int(rec['limit']),rec['start'],rec['end'])
        

        #"{\"type\": \"get_market_realtime\",\"symbol\":\"PTT\",\"interval\":0,\"subscribe\":\"price_info\"}"
        #"{\"type\": \"get_market_realtime\",\"symbol\":\"PTT\",\"interval\":0,\"subscribe\":\"bid_offer\"}"
        #"{\"type\": \"get_market_realtime\",\"symbol\":\"PTT\",\"interval\":\"1d\",\"subscribe\":\"candlestick\"}"
        elif rec['type']=='get_market_realtime':
            market=INVESTOR_MARKET(time_out)
            data=market.get_market_realtime(client,rec['symbol'],rec['interval'],rec['subscribe'])

        print('client send data : ',data)
        cli.send(data.encode('utf-8'))
        cli.close()

if __name__=="__main__":
    fig = pyfiglet.Figlet(font='slant')
    print(fig.renderText('Mr.ROBOT \n Settrade'))
    while True:
        try:
            config = configparser.ConfigParser()
            config.read('config.txt')
            config.sections()

            app_id=config['default']['app_id']
            app_secret=config['default']['app_secret']
            broker_id=config['default']['broker_id']
            app_code=config['default']['app_code']
            account_no=config['default']['account_no']
            pin=config['default']['pin']
            port=config['default']['port']
            type=config['default']['type']
            time_out=float(1)
            
            client = INVESTOR_LOGIN.login(app_id,app_secret,broker_id,app_code)

            if(client['message'] == 'Success'):
                if(type == '0'):
                    print(fig.renderText('Derivatives \n TFEX'))
                elif(type == '1'):
                    print(fig.renderText('Equity'))

                main_serv(client['code'],port,pin,account_no,type,time_out)
            else:
                raise Exception("error login settrade :",client['message'])
        except:
            print("Error Delay 10 Sec")
            hang_error = traceback.format_exc()
            print(hang_error)
            f = open("error.txt", "w")
            f.write(hang_error)
            f.close()
            time.sleep(10)