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

            aumSize = res.get('aumSize')
            average = res.get('average')
            change = res.get('change')
            eps = res.get('eps')
            exchange = res.get('exchange')
            exercisePrice = res.get('exercisePrice')
            exerciseRatio = res.get('exerciseRatio')
            high = res.get('high')
            impliedVolatility = res.get('impliedVolatility')
            inav = res.get('inav')
            instrumentType = res.get('instrumentType')
            intrinsicValue = res.get('intrinsicValue')
            last = res.get('last')
            lastTradingDate = res.get('lastTradingDate')
            low = res.get('low')
            marketStatus = res.get('marketStatus')
            maturityDate = res.get('maturityDate')
            moneyness = res.get('moneyness')
            pbv = res.get('pbv')
            pe = res.get('pe')
            percentChange = res.get('percentChange')
            percentYield = res.get('percentYield')
            securityType = res.get('securityType')
            Symbol = res.get('symbol')
            theoretical = res.get('theoretical')
            toLastTrade = res.get('toLastTrade')
            totalVolume = res.get('totalVolume')
            underlying = res.get('underlying')
            underlyingPrice = res.get('underlyingPrice')
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
            close = res.get('close')
            high = res.get('high')
            lastSequence = res.get('lastSequence')
            low = res.get('low')
            open = res.get('open')
            Time = res.get('time')
            value = res.get('value')
            volume = res.get('volume')
            return f'1,{close},{high},{lastSequence},{low},{open},{Time},{value},{volume}'
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
                    print('time_out:',self.time_out)
                    time.sleep(self.time_out)
                if model.get('is_success'):
                    high = model.get('data').get('high')
                    low = model.get('data').get('low')
                    last = model.get('data').get('last')
                    total_volume = model.get('data').get('total_volume')
                    projected_open_price = model.get('data').get('projected_open_price')
                    change = model.get('data').get('change')
                    total_value = model.get('data').get('total_value')
                    market_status = model.get('data').get('market_status')

                    return f'1,{symbol},{high},{low},{last},{total_volume},{projected_open_price},{change},{total_value},{market_status}'
                else:
                    return f'0,{model.get("is_success")},{model.get("message")}'
            elif(subscribe == 'bid_offer'):
                sub = realtime.subscribe_bid_offer(symbol, on_message = my_message)
                sub.start()
                while not model:
                    print('time_out:',self.time_out)
                    time.sleep(self.time_out)
                if model.get('is_success'):
                    
                    bid_flag = model.get('data').get('bid_flag')
                    ask_flag = model.get('data').get('ask_flag')
                    bid_price1 = model.get('data').get('bid_price1')
                    bid_price2 = model.get('data').get('bid_price2')
                    bid_price3 = model.get('data').get('bid_price3')
                    bid_price4 = model.get('data').get('bid_price4')
                    bid_price5 = model.get('data').get('bid_price5')
                    bid_price6 = model.get('data').get('bid_price6')
                    bid_price7 = model.get('data').get('bid_price7')
                    bid_price8 = model.get('data').get('bid_price8')
                    bid_price9 = model.get('data').get('bid_price9')
                    bid_price10 = model.get('data').get('bid_price10')

                    ask_price1 = model.get('data').get('ask_price1')
                    ask_price2 = model.get('data').get('ask_price2')
                    ask_price3 = model.get('data').get('ask_price3')
                    ask_price4 = model.get('data').get('ask_price4')
                    ask_price5 = model.get('data').get('ask_price5')
                    ask_price6 = model.get('data').get('ask_price6')
                    ask_price7 = model.get('data').get('ask_price7')
                    ask_price8 = model.get('data').get('ask_price8')
                    ask_price9 = model.get('data').get('ask_price9')
                    ask_price10 = model.get('data').get('ask_price10')
                    
                    bid_volume1 = model.get('data').get('bid_volume1')
                    bid_volume2 = model.get('data').get('bid_volume2')
                    bid_volume3 = model.get('data').get('bid_volume3')
                    bid_volume4 = model.get('data').get('bid_volume4')
                    bid_volume5 = model.get('data').get('bid_volume5')
                    bid_volume6 = model.get('data').get('bid_volume6')
                    bid_volume7 = model.get('data').get('bid_volume7')
                    bid_volume8 = model.get('data').get('bid_volume8')
                    bid_volume9 = model.get('data').get('bid_volume9')
                    bid_volume10 = model.get('data').get('bid_volume10')

                    ask_volume1 = model.get('data').get('ask_volume1')
                    ask_volume2 = model.get('data').get('ask_volume2')
                    ask_volume3 = model.get('data').get('ask_volume3')
                    ask_volume4 = model.get('data').get('ask_volume4')
                    ask_volume5 = model.get('data').get('ask_volume5')
                    ask_volume6 = model.get('data').get('ask_volume6')
                    ask_volume7 = model.get('data').get('ask_volume7')
                    ask_volume8 = model.get('data').get('ask_volume8')
                    ask_volume9 = model.get('data').get('ask_volume9')
                    ask_volume10 = model.get('data').get('ask_volume10')
                    return f'1,{symbol},{bid_flag},{ask_flag},{bid_price1},{bid_price2},{bid_price3},{bid_price4},{bid_price5},{bid_price6},{bid_price7},{bid_price8},{bid_price9},{bid_price10},{ask_price1},{ask_price2},{ask_price3},{ask_price4},{ask_price5},{ask_price6},{ask_price7},{ask_price8},{ask_price9},{ask_price10},{bid_volume1},{bid_volume2},{bid_volume3},{bid_volume4},{bid_volume5},{bid_volume6},{bid_volume7},{bid_volume8},{bid_volume9},{bid_volume10},{ask_volume1},{ask_volume2},{ask_volume3},{ask_volume4},{ask_volume5},{ask_volume6},{ask_volume7},{ask_volume8},{ask_volume9},{ask_volume10}'
                else:
                    return f'0,{model.get("is_success")},{model.get("message")}'
                
            elif(subscribe == 'candlestick'):
                sub = realtime.subscribe_candlestick(symbol, interval=interval, on_message = my_message)
                sub.start()
                while not model:
                    print('time_out:',self.time_out)
                    time.sleep(self.time_out)
                if model.get('is_success'):
                    last_sequence = model.get('data').get('last_sequence')
                    Time = model.get('data').get('time')
                    open = model.get('data').get('open')
                    high = model.get('data').get('high')
                    low = model.get('data').get('low')
                    close = model.get('data').get('close')
                    volume = model.get('data').get('volume')
                    value = model.get('data').get('value')
                    return f'1,{symbol},{interval},{last_sequence},{Time},{open},{high},{low},{close},{volume},{value}'
                else:
                    return f'0,{model.get("is_success")},{model.get("message")}'
                
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
            if model.get('is_success'):
                order_no = model.get('data').get('order_no')
                ext_order_no = model.get('data').get('ext_order_no')
                account_no = model.get('data').get('FT0009D')
                enter_id = model.get('data').get('enter_id')
                entry_time = model.get('data').get('entry_time')
                series_id = model.get('data').get('series_id')
                side = model.get('data').get('side')
                position = model.get('data').get('position')
                price = model.get('data').get('price')
                price_type = model.get('data').get('price_type')
                volume = model.get('data').get('volume')
                balance_volume = model.get('data').get('balance_volume')
                matched_volume = model.get('data').get('matched_volume')
                cancelled_volume = model.get('data').get('cancelled_volume')
                valid = model.get('data').get('valid')
                until = model.get('data').get('until')
                status = model.get('data').get('status')

                return f'1,{order_no},{ext_order_no},{account_no},{enter_id},{entry_time},{series_id},{side},{position},{price},{price_type},{volume},{balance_volume},{matched_volume},{cancelled_volume},{valid},{until},{status}'
            else:
                return f'0,{model.get("is_success")},{model.get("message")}'
        except  SettradeError as e:
            return f'0,{e.code},{e}'