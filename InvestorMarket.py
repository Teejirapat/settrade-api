from settrade_v2 import Investor
from settrade_v2.errors import SettradeError
import time


model = ''

class INVESTOR_MARKET:

    def __init__(self, time_out):
        self.time_out = time_out
        
    def get_quote_symbol(investor,symbol):
        try:
            market = investor.MarketData()
            res = market.get_quote_symbol(symbol)

            aumSize = res['aumSize']
            average = res['average']
            change = res['change']
            eps = res['eps']
            exchange = res['exchange']
            exercisePrice = res['exercisePrice']
            exerciseRatio = res['exerciseRatio']
            high = res['high']
            impliedVolatility = res['impliedVolatility']
            inav = res['inav']
            instrumentType = res['instrumentType']
            intrinsicValue = res['intrinsicValue']
            last = res['last']
            lastTradingDate = res['lastTradingDate']
            low = res['low']
            marketStatus = res['marketStatus']
            maturityDate = res['maturityDate']
            moneyness = res['moneyness']
            pbv = res['pbv']
            pe = res['pe']
            percentChange = res['percentChange']
            percentYield = res['percentYield']
            securityType = res['securityType']
            Symbol = res['symbol']
            theoretical = res['theoretical']
            toLastTrade = res['toLastTrade']
            totalVolume = res['totalVolume']
            underlying = res['underlying']
            underlyingPrice = res['underlyingPrice']
            print(res)
            return f'1,{aumSize},{average},{change},{eps},{exchange},{exercisePrice},{exerciseRatio},{high},{impliedVolatility},{inav},{instrumentType},{intrinsicValue},{last},{lastTradingDate},{low},{marketStatus},{maturityDate},{moneyness},{pbv},{pe},{percentChange},{percentYield},{securityType},{Symbol},{theoretical},{toLastTrade},{totalVolume},{underlying},{underlyingPrice}'
        except  SettradeError as e:
            return f'0,{e.code},{e}'
        
    
    def get_market_historical(investor,symbol,interval,limit,start,end):
        try:
            market = investor.MarketData()
            res = market.get_candlestick(
            symbol=symbol,
            interval=interval, #'1m', '3m', '5m', '10m', '15m', '30m', '60m', '1d', '1w', '1M'
            limit=limit,
            start=start,
            end=end,
            normalized=True,
            )
            return f'1'
        except  SettradeError as e:
            return f'0,{e.code},{e}'
    
    #real time
    def get_market_realtime(self,investor,symbol,interval,subscribe):
        try:
            def my_message(result):
                global model

                model = result
                return f'1'
    
            realtime = investor.RealtimeDataConnection()
            if(subscribe == 'price_info'):
                sub = realtime.subscribe_price_info(symbol, on_message = my_message)
                sub.start()
                while not model:
                    time.sleep(self.time_out)
                if model['is_success']:
                    high = model['data']['high']
                    low = model['data']['low']
                    last = model['data']['last']
                    total_volume = model['data']['total_volume']
                    projected_open_price = model['data']['projected_open_price']
                    change = model['data']['change']
                    total_value = model['data']['total_value']
                    market_status = model['data']['market_status']

                    return f'1,{symbol},{high},{low},{last},{total_volume},{projected_open_price},{change},{total_value},{market_status}'
                else:
                    return f'0,{model["is_success"]},{model["message"]}'
            elif(subscribe == 'bid_offer'):
                sub = realtime.subscribe_bid_offer(symbol, on_message = my_message)
                sub.start()
                while not model:
                    print('time_out:',self.time_out)
                    time.sleep(self.time_out)
                if model['is_success']:
                    bid_flag = model['data']['bid_flag']
                    ask_flag = model['data']['ask_flag']
                    bid_price1 = model['data']['bid_price1']
                    bid_price2 = model['data']['bid_price2']
                    bid_price3 = model['data']['bid_price3']
                    bid_price4 = model['data']['bid_price4']
                    bid_price5 = model['data']['bid_price5']
                    bid_price6 = model['data']['bid_price6']
                    bid_price7 = model['data']['bid_price7']
                    bid_price8 = model['data']['bid_price8']
                    bid_price9 = model['data']['bid_price9']
                    bid_price10 = model['data']['bid_price10']

                    ask_price1 = model['data']['ask_price1']
                    ask_price2 = model['data']['ask_price2']
                    ask_price3 = model['data']['ask_price3']
                    ask_price4 = model['data']['ask_price4']
                    ask_price5 = model['data']['ask_price5']
                    ask_price6 = model['data']['ask_price6']
                    ask_price7 = model['data']['ask_price7']
                    ask_price8 = model['data']['ask_price8']
                    ask_price9 = model['data']['ask_price9']
                    ask_price10 = model['data']['ask_price10']
                    
                    bid_volume1 = model['data']['bid_volume1']
                    bid_volume2 = model['data']['bid_volume2']
                    bid_volume3 = model['data']['bid_volume3']
                    bid_volume4 = model['data']['bid_volume4']
                    bid_volume5 = model['data']['bid_volume5']
                    bid_volume6 = model['data']['bid_volume6']
                    bid_volume7 = model['data']['bid_volume7']
                    bid_volume8 = model['data']['bid_volume8']
                    bid_volume9 = model['data']['bid_volume9']
                    bid_volume10 = model['data']['bid_volume10']

                    ask_volume1 = model['data']['ask_volume1']
                    ask_volume2 = model['data']['ask_volume2']
                    ask_volume3 = model['data']['ask_volume3']
                    ask_volume4 = model['data']['ask_volume4']
                    ask_volume5 = model['data']['ask_volume5']
                    ask_volume6 = model['data']['ask_volume6']
                    ask_volume7 = model['data']['ask_volume7']
                    ask_volume8 = model['data']['ask_volume8']
                    ask_volume9 = model['data']['ask_volume9']
                    ask_volume10 = model['data']['ask_volume10']
                    return f'1,{symbol},{bid_flag},{ask_flag},{bid_price1},{bid_price2},{bid_price3},{bid_price4},{bid_price5},{bid_price6},{bid_price7},{bid_price8},{bid_price9},{bid_price10},{ask_price1},{ask_price2},{ask_price3},{ask_price4},{ask_price5},{ask_price6},{ask_price7},{ask_price8},{ask_price9},{ask_price10},{bid_volume1},{bid_volume2},{bid_volume3},{bid_volume4},{bid_volume5},{bid_volume6},{bid_volume7},{bid_volume8},{bid_volume9},{bid_volume10},{ask_volume1},{ask_volume2},{ask_volume3},{ask_volume4},{ask_volume5},{ask_volume6},{ask_volume7},{ask_volume8},{ask_volume9},{ask_volume10}'
                else:
                    return f'0,{model["is_success"]},{model["message"]}'
                
            elif(subscribe == 'candlestick'):
                sub = realtime.subscribe_candlestick(symbol, interval=interval, on_message = my_message)
                sub.start()
                while not model:
                    time.sleep(self.time_out)
                if model['is_success']:
                    last_sequence = model['data']['last_sequence']
                    Time = model['data']['time']
                    open = model['data']['open']
                    high = model['data']['high']
                    low = model['data']['low']
                    close = model['data']['close']
                    volume = model['data']['volume']
                    value = model['data']['value']
                    return f'1,{symbol},{interval},{last_sequence},{Time},{open},{high},{low},{close},{volume},{value}'
                else:
                    return f'0,{model["is_success"]},{model["message"]}'
                
        except  SettradeError as e:
            return f'0,{e.code},{e}'
    
    def get_Equity_order(self,investor,account_no):
        try:
            realtime = investor.RealtimeDataConnection()
            sub = realtime.subscribe_Equity_order(
                account_no,
                on_message=INVESTOR_MARKET.my_message,
                )
            sub.start()
            while not model:
                time.sleep(self.time_out)
            if model['is_success']:
                order_no = model['data']['order_no']
                ext_order_no = model['data']['ext_order_no']
                account_no = model['data']['FT0009D']
                enter_id = model['data']['enter_id']
                entry_time = model['data']['entry_time']
                series_id = model['data']['series_id']
                side = model['data']['side']
                position = model['data']['position']
                price = model['data']['price']
                price_type = model['data']['price_type']
                volume = model['data']['volume']
                balance_volume = model['data']['balance_volume']
                matched_volume = model['data']['matched_volume']
                cancelled_volume = model['data']['cancelled_volume']
                valid = model['data']['valid']
                until = model['data']['until']
                status = model['data']['status']

                return f'1,{order_no},{ext_order_no},{account_no},{enter_id},{entry_time},{series_id},{side},{position},{price},{price_type},{volume},{balance_volume},{matched_volume},{cancelled_volume},{valid},{until},{status}'
            else:
                return f'0,{model["is_success"]},{model["message"]}'
            
        except  SettradeError as e:
            return f'0,{e.code},{e}'
        
    def get_equity_order(self,investor,account_no):
        try:
            realtime = investor.RealtimeDataConnection()
            sub = realtime.subscribe_equity_order(
                account_no,
                on_message=INVESTOR_MARKET.my_message,
                )
            sub.start()
            while not model:
                time.sleep(self.time_out)
            if model['is_success']:
                order_no = model['data']['order_no']
                ext_order_no = model['data']['ext_order_no']
                account_no = model['data']['FT0009D']
                enter_id = model['data']['enter_id']
                entry_time = model['data']['entry_time']
                series_id = model['data']['series_id']
                side = model['data']['side']
                position = model['data']['position']
                price = model['data']['price']
                price_type = model['data']['price_type']
                volume = model['data']['volume']
                balance_volume = model['data']['balance_volume']
                matched_volume = model['data']['matched_volume']
                cancelled_volume = model['data']['cancelled_volume']
                valid = model['data']['valid']
                until = model['data']['until']
                status = model['data']['status']

                return f'1,{order_no},{ext_order_no},{account_no},{enter_id},{entry_time},{series_id},{side},{position},{price},{price_type},{volume},{balance_volume},{matched_volume},{cancelled_volume},{valid},{until},{status}'
            else:
                return f'0,{model["is_success"]},{model["message"]}'
        except  SettradeError as e:
            return f'0,{e.code},{e}'